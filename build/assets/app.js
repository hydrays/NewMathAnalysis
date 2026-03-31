/* app.js — Lightweight VLOOK replacement
 * Features: chapter nav, TOC sidebar, sidebar toggle, auto-numbering
 */

(function () {
  "use strict";

  // ── Chapter navigation ───────────────────────────────────────

  function buildDocNav() {
    var list = document.getElementById("doc-nav-list");
    if (!list || !window.docLib || !window.docLib.length) return;

    var currentFile = location.pathname.split("/").pop() || "index.html";

    window.docLib.forEach(function (item) {
      var li = document.createElement("li");
      var a = document.createElement("a");

      // item is {title, url}
      a.href = item.url;
      a.textContent = item.title;
      a.title = item.title;

      // Strip query string for comparison
      var itemFile = item.url.split("?")[0].split("/").pop();
      if (itemFile === currentFile) {
        a.className = "current";
        // Scroll this item into view in the sidebar after render
        setTimeout(function () {
          a.scrollIntoView({ block: "nearest" });
        }, 0);
      }

      li.appendChild(a);
      list.appendChild(li);
    });
  }

  // ── Auto chapter numbering ───────────────────────────────────

  function applyAutonum() {
    // chpAutonum is e.g. "h1=off" or empty/undefined
    if (!window.chpAutonum || window.chpAutonum === "") return;

    // Parse: we support "off" to disable entirely, or default = h2+ numbered
    if (window.chpAutonum.indexOf("off") !== -1 &&
        window.chpAutonum.indexOf("h1") !== -1) {
      // h1=off means don't number h1 but DO number h2+
      document.body.classList.add("chp-autonum");
    }
  }

  // ── Sidebar toggle ───────────────────────────────────────────

  function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var overlay = document.getElementById("overlay");
    sidebar.classList.toggle("open");
    overlay.classList.toggle("visible");
  }

  function closeSidebar() {
    var sidebar = document.getElementById("sidebar");
    var overlay = document.getElementById("overlay");
    sidebar.classList.remove("open");
    overlay.classList.remove("visible");
  }

  // Expose for inline onclick handlers in template
  window.toggleSidebar = toggleSidebar;
  window.closeSidebar  = closeSidebar;

  // ── TOC active section highlighting ─────────────────────────

  function initTocHighlight() {
    var tocLinks = document.querySelectorAll("#toc-nav a");
    if (!tocLinks.length) return;

    var headings = Array.from(
      document.querySelectorAll("#content h1, #content h2, #content h3, #content h4")
    );

    if (!headings.length) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var id = entry.target.id;
          if (!id) return;
          tocLinks.forEach(function (a) {
            a.classList.toggle(
              "toc-active",
              a.getAttribute("href") === "#" + id
            );
          });
        });
      },
      { rootMargin: "0px 0px -60% 0px", threshold: 0 }
    );

    headings.forEach(function (h) {
      if (h.id) observer.observe(h);
    });
  }

  // ── Image captions ───────────────────────────────────────────
  // Pandoc puts alt text as <img alt="...">. Wrap images in <figure>
  // and show alt text as <figcaption> when alt is non-empty and not a URL.

  function buildFigureCaptions() {
    var imgs = document.querySelectorAll("#content img");
    imgs.forEach(function (img) {
      var alt = img.getAttribute("alt");
      if (!alt || alt.match(/^https?:\/\//)) return;
      if (img.parentElement && img.parentElement.tagName === "FIGURE") return;

      var figure = document.createElement("figure");
      figure.className = "img-figure";
      img.parentNode.insertBefore(figure, img);
      figure.appendChild(img);

      var caption = document.createElement("figcaption");
      caption.textContent = alt;
      figure.appendChild(caption);
    });
  }

  // ── Init ─────────────────────────────────────────────────────

  function init() {
    buildDocNav();
    applyAutonum();
    initTocHighlight();
    buildFigureCaptions();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
