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
      el.scrollIntoView({ block: "start" });
    }
  }

  function filter(raw) {
    const query = norm(raw.trim());
    let shown = 0;
    cards.forEach(function (card) {
      const blob = norm(card.getAttribute("data-blob") || "");
      const match = !query || blob.includes(query);
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
      meta.textContent = query ? shown + " on this page" : "";
    }
    if (!hits) return;
    if (!query) {
      hits.classList.remove("is-on");
      hits.innerHTML = "";
      return;
    }
    const others = index.filter(function (item) {
      return item.page !== pageId && norm(item.text).includes(query);
    }).slice(0, 8);
    if (!others.length) {
      hits.classList.remove("is-on");
      hits.innerHTML = "";
      return;
    }
    hits.innerHTML = others.map(function (item) {
      return '<a class="hit" href="' + item.href + '"><small>' + item.category + '</small><strong>' + item.title + '</strong></a>';
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
    const marker = 140;
    let current = targets[0] ? targets[0].id : "";
    targets.forEach(function (el) {
      if (el.getBoundingClientRect().top <= marker) current = el.id;
    });
    sideLinks.forEach(function (link) {
      link.classList.toggle("is-active", link.getAttribute("href") === "#" + current);
    });
  }
  if (targets.length) {
    window.addEventListener("scroll", spy, { passive: true });
    spy();
  }

  setOpenFromHash();
  window.addEventListener("hashchange", setOpenFromHash);
})();
