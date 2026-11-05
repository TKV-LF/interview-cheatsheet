(function () {
  const root = document.documentElement;
  const themeBtn = document.querySelector("[data-theme-toggle]");
  const storedTheme = localStorage.getItem("cheat-theme");
  let theme = storedTheme || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

  function applyTheme(next) {
    theme = next;
    root.setAttribute("data-theme", theme);
    localStorage.setItem("cheat-theme", theme);
    if (themeBtn) themeBtn.textContent = theme === "dark" ? "☀" : "☾";
  }
  applyTheme(theme);
  themeBtn && themeBtn.addEventListener("click", function () {
    applyTheme(theme === "dark" ? "light" : "dark");
  });

  const topbar = document.querySelector(".topbar");
  const navToggle = document.querySelector("[data-nav-toggle]");
  const siteNav = document.getElementById("site-nav");
  const navQuery = window.matchMedia("(max-width: 860px)");

  function topbarHeight() {
    return topbar ? topbar.getBoundingClientRect().height : 0;
  }
  function syncTopbar() {
    root.style.setProperty("--topbar-h", Math.round(topbarHeight()) + "px");
  }
  syncTopbar();
  window.addEventListener("resize", syncTopbar);

  function setNavOpen(open) {
    if (!topbar || !navToggle) return;
    topbar.classList.toggle("is-nav-open", open);
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
    navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }

  if (navToggle) {
    navToggle.addEventListener("click", function () {
      setNavOpen(!topbar.classList.contains("is-nav-open"));
    });
  }
  if (siteNav) {
    siteNav.addEventListener("click", function (event) {
      const link = event.target.closest("a");
      if (!link || !navQuery.matches) return;
      const next = new URL(link.href, location.href);
      if (next.pathname === location.pathname) setNavOpen(false);
    });
  }
  if (typeof navQuery.addEventListener === "function") {
    navQuery.addEventListener("change", function () {
      if (!navQuery.matches) setNavOpen(false);
    });
  }

  const index = window.CHEAT_SEARCH || [];
  const pageId = document.body.getAttribute("data-page") || "";

  function norm(value) {
    return (value || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/\p{M}/gu, "");
  }

  function applyLang(lang) {
    document.querySelectorAll("[data-pane]").forEach(function (pane) {
      pane.hidden = pane.getAttribute("data-pane") !== lang;
    });
    document.querySelectorAll("[data-set-lang]").forEach(function (btn) {
      btn.classList.toggle("is-on", btn.getAttribute("data-set-lang") === lang);
    });
    localStorage.setItem("cheat-lang", lang);
  }

  applyLang(localStorage.getItem("cheat-lang") || "en");
  document.body.addEventListener("click", function (event) {
    const btn = event.target.closest("[data-set-lang]");
    if (!btn) return;
    applyLang(btn.getAttribute("data-set-lang"));
  });

  const input = document.querySelector("[data-search]");
  const hits = document.querySelector("[data-hits]");
  const meta = document.querySelector("[data-search-meta]");
  const cards = Array.from(document.querySelectorAll("details.q"));

  function setOpenFromHash() {
    const id = (location.hash || "").replace("#", "");
    if (!id) return;
    const el = document.getElementById(id);
    if (el && el.tagName === "DETAILS") {
      el.open = true;
      requestAnimationFrame(function () { el.scrollIntoView({ block: "start", behavior: "instant" }); });
    }
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (ch) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch];
    });
  }
  function matches(text, tokens) {
    for (let i = 0; i < tokens.length; i += 1) {
      if (!text.includes(tokens[i])) return false;
    }
    return true;
  }
  cards.forEach(function (card) {
    card._blob = norm(card.getAttribute("data-blob") || "");
  });
  index.forEach(function (item) {
    item._text = norm(item.title + " " + item.text);
  });

  function filter(raw) {
    const query = norm(raw.trim());
    const tokens = query.split(/\s+/).filter(Boolean);
    let shown = 0;
    cards.forEach(function (card) {
      const match = !query || matches(card._blob, tokens);
      card.hidden = !match;
      if (match) shown += 1;
      if (query && match) card.open = true;
    });
    document.querySelectorAll("[data-sec]").forEach(function (link) {
      const id = link.getAttribute("href").slice(1);
      const block = document.getElementById(id);
      if (!block) return;
      const any = block.querySelectorAll("details.q:not([hidden])").length > 0;
      link.hidden = query ? !any : false;
    });
    document.querySelectorAll(".q-link").forEach(function (link) {
      const id = link.getAttribute("href").slice(1);
      const card = document.getElementById(id);
      link.hidden = !card || card.hidden;
    });
    if (meta) {
      meta.textContent = query && pageId !== "hub" ? shown + " here" : "";
    }
    if (!hits) return;
    if (!query) {
      hits.classList.remove("is-on");
      hits.innerHTML = "";
      return;
    }
    const others = index.filter(function (item) {
      return item.page !== pageId && matches(item._text, tokens);
    }).slice(0, 10);
    if (!others.length) {
      hits.classList.remove("is-on");
      hits.innerHTML = "";
      return;
    }
    hits.innerHTML = others.map(function (item) {
      return '<a class="hit" href="' + escapeHtml(item.href) + '"><small>' + escapeHtml(item.category) + '</small><strong>' + escapeHtml(item.title) + '</strong></a>';
    }).join("");
    hits.classList.add("is-on");
  }

  if (input) {
    input.addEventListener("input", function () { filter(input.value); });
    document.addEventListener("keydown", function (event) {
      if (event.key === "/" && document.activeElement !== input) {
        event.preventDefault();
        input.focus();
      }
      if (event.key === "Escape") {
        if (topbar && topbar.classList.contains("is-nav-open")) {
          setNavOpen(false);
          navToggle && navToggle.focus();
          return;
        }
        input.value = "";
        filter("");
        input.blur();
      }
    });
  }

  document.querySelectorAll("[data-expand]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      const open = btn.getAttribute("data-expand") === "open";
      cards.forEach(function (card) {
        if (!card.hidden) card.open = open;
      });
    });
  });

  const sideLinks = Array.from(document.querySelectorAll(".side a"));
  const targets = sideLinks
    .map(function (link) { return document.getElementById(link.getAttribute("href").slice(1)); })
    .filter(Boolean);
  function spy() {
    const marker = topbarHeight() + 24;
    let current = targets[0] ? targets[0].id : "";
    targets.forEach(function (el) {
      if (el.getBoundingClientRect().top <= marker) current = el.id;
    });
    let activeLink = null;
    sideLinks.forEach(function (link) {
      const on = link.getAttribute("href") === "#" + current;
      link.classList.toggle("is-active", on);
      if (on) activeLink = link;
    });
    const box = document.querySelector(".side");
    if (activeLink && box && box.scrollHeight > box.clientHeight && !navQuery.matches) {
      const top = activeLink.getBoundingClientRect().top - box.getBoundingClientRect().top + box.scrollTop;
      if (top < box.scrollTop + 40 || top > box.scrollTop + box.clientHeight - 60) {
        box.scrollTop = Math.max(0, top - box.clientHeight / 3);
      }
    }
  }
  if (targets.length) {
    window.addEventListener("scroll", spy, { passive: true });
    spy();
  }

  // Mobile "On this page" toggle.
  const side = document.querySelector("[data-side]");
  const sideToggle = document.querySelector("[data-side-toggle]");
  if (side && sideToggle) {
    sideToggle.addEventListener("click", function () {
      const open = !side.classList.contains("is-open");
      side.classList.toggle("is-open", open);
      sideToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    side.addEventListener("click", function (event) {
      if (event.target.closest(".side-list a") && navQuery.matches) {
        side.classList.remove("is-open");
        sideToggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Known cards, practice mode, and progress. Stored in this browser only.
  const KNOWN_KEY = "cheat-known";
  let known = {};
  try { known = JSON.parse(localStorage.getItem(KNOWN_KEY) || "{}") || {}; } catch (e) { known = {}; }
  const progress = document.querySelector("[data-progress]");
  function renderProgress() {
    if (!progress || !cards.length) return;
    const done = cards.filter(function (card) { return known[card.id]; }).length;
    progress.textContent = done + " / " + cards.length + " ready";
  }
  cards.forEach(function (card) {
    const box = card.querySelector("[data-known]");
    const isKnown = !!known[card.id];
    card.classList.toggle("is-known", isKnown);
    if (box) {
      box.checked = isKnown;
      box.addEventListener("change", function () {
        if (box.checked) known[card.id] = 1; else delete known[card.id];
        localStorage.setItem(KNOWN_KEY, JSON.stringify(known));
        card.classList.toggle("is-known", box.checked);
        renderProgress();
      });
    }
    const reveal = card.querySelector("[data-reveal]");
    if (reveal) {
      reveal.addEventListener("click", function () { card.classList.add("is-revealed"); });
    }
    card.addEventListener("toggle", function () {
      if (!card.open) card.classList.remove("is-revealed");
    });
  });
  renderProgress();

  function bindToggle(selector, bodyClass, storeKey) {
    const btn = document.querySelector(selector);
    if (!btn) return;
    function set(on) {
      document.body.classList.toggle(bodyClass, on);
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      localStorage.setItem(storeKey, on ? "1" : "");
    }
    set(localStorage.getItem(storeKey) === "1");
    btn.addEventListener("click", function () { set(!document.body.classList.contains(bodyClass)); });
  }
  bindToggle("[data-practice]", "is-practice", "cheat-practice");
  bindToggle("[data-hide-known]", "is-hide-known", "cheat-hide-known");

  setOpenFromHash();
  window.addEventListener("hashchange", setOpenFromHash);
})();
