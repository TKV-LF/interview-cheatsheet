#!/usr/bin/env python3
"""Small helpers for editing _build/data/*.json from scripts.

    from cards import Site
    site = Site()
    card = site.get("new-php-index")          # the dict, edit it in place
    site.move("soft-g36", "debugging", "Find the layer")
    site.delete("cv-c20")
    site.add("javascript", "JavaScript", {...card...}, after="js-closure")
    site.save(only=["php", "debugging"])

Command line:
    python3 _build/cards.py show <id>
    python3 _build/cards.py list <page>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"


class Site:
    def __init__(self) -> None:
        self.pages: dict[str, dict] = {}
        for path in sorted(DATA.glob("*.json")):
            self.pages[path.stem] = json.loads(path.read_text(encoding="utf-8"))

    def find(self, card_id: str) -> tuple[str, dict, int]:
        for stem, page in self.pages.items():
            for sec in page["sections"]:
                for index, card in enumerate(sec["cards"]):
                    if card["id"] == card_id:
                        return stem, sec, index
        raise KeyError(card_id)

    def get(self, card_id: str) -> dict:
        _stem, sec, index = self.find(card_id)
        return sec["cards"][index]

    def section(self, stem: str, name: str, create: bool = True, before: str | None = None) -> dict:
        page = self.pages[stem]
        for sec in page["sections"]:
            if sec["name"] == name:
                return sec
        if not create:
            raise KeyError(f"{stem}/{name}")
        sec = {"name": name, "cards": []}
        if before:
            names = [s["name"] for s in page["sections"]]
            page["sections"].insert(names.index(before), sec)
        else:
            page["sections"].append(sec)
        return sec

    def delete(self, card_id: str) -> dict:
        _stem, sec, index = self.find(card_id)
        return sec["cards"].pop(index)

    def add(self, stem: str, section: str, card: dict, after: str | None = None, first: bool = False) -> None:
        sec = self.section(stem, section)
        ids = [c["id"] for c in sec["cards"]]
        if after and after in ids:
            sec["cards"].insert(ids.index(after) + 1, card)
        elif first:
            sec["cards"].insert(0, card)
        else:
            sec["cards"].append(card)

    def move(self, card_id: str, stem: str, section: str, after: str | None = None, first: bool = False) -> None:
        card = self.delete(card_id)
        self.add(stem, section, card, after=after, first=first)

    def drop_empty_sections(self) -> None:
        for page in self.pages.values():
            page["sections"] = [s for s in page["sections"] if s["cards"] or s.get("html")]

    def save(self, only: list[str]) -> None:
        """Write only the named pages, so two editors never overwrite each other."""
        for stem, page in self.pages.items():
            if stem not in only:
                continue
            (DATA / f"{stem}.json").write_text(json.dumps(page, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    site = Site()
    if len(sys.argv) >= 3 and sys.argv[1] == "show":
        print(json.dumps(site.get(sys.argv[2]), ensure_ascii=False, indent=1))
    elif len(sys.argv) >= 3 and sys.argv[1] == "list":
        for sec in site.pages[sys.argv[2]]["sections"]:
            print(f"## {sec['name']}")
            for card in sec["cards"]:
                print(f"  {card['id']}: {card['title']}")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
