/* app.js — Lightweight VLOOK replacement
 * Features: chapter nav, TOC sidebar, sidebar toggle, auto-numbering
 */

(function () {
  "use strict";

  // ── Chapter navigation ───────────────────────────────────────
  // Builds the chapter list and inlines the current chapter's TOC
  // as a collapsible sub-list right after its entry.

  function buildDocNav() {
    var list = document.getElementById("doc-nav-list");
    if (!list || !window.docLib || !window.docLib.length) return;

    var currentFile = location.pathname.split("/").pop() || "index.html";

    window.docLib.forEach(function (item) {
      var li = document.createElement("li");
      li.className = "nav-chapter";
      var a = document.createElement("a");

      a.href = item.url;
      a.textContent = item.title;
      a.title = item.title;

      var itemFile = item.url.split("?")[0].split("/").pop();
      var isCurrent = (itemFile === currentFile);

      if (isCurrent) {
        a.className = "current";
        li.classList.add("nav-chapter-current");

        // Move the page TOC into this list item as an inline sub-list
        var tocNav = document.getElementById("toc-nav");
        if (tocNav) {
          var tocUl = tocNav.querySelector("ul");
          if (tocUl) {
            tocUl.className = "chapter-toc";
            li.appendChild(tocUl);
          }
          // Hide the now-empty toc-nav panel
          tocNav.style.display = "none";
          // Also hide the divider above it
          var divider = document.querySelector(".nav-divider");
          if (divider) divider.style.display = "none";
        }

        // Toggle chapter TOC on click (already on this page — no navigation needed)
        a.addEventListener("click", function (e) {
          e.preventDefault();
          li.classList.toggle("open");
        });

        // Scroll into view after render
        setTimeout(function () {
          a.scrollIntoView({ block: "nearest" });
        }, 0);
      }

      li.insertBefore(a, li.firstChild);
      list.appendChild(li);
    });
  }

  // ── Auto chapter numbering ───────────────────────────────────

  function applyAutonum() {
    if (!window.chpAutonum || window.chpAutonum === "") return;

    if (window.chpAutonum.indexOf("off") !== -1 &&
        window.chpAutonum.indexOf("h1") !== -1) {
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

  window.toggleSidebar = toggleSidebar;
  window.closeSidebar  = closeSidebar;

  // ── TOC active section highlighting ─────────────────────────
  // After buildDocNav() runs, the TOC links are inside #doc-nav-list.
  // Select only anchor links (href="#...") to avoid matching chapter links.

  function initTocHighlight() {
    var tocLinks = document.querySelectorAll("#doc-nav-list a[href^='#']");
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

  // ── TOC accordion ────────────────────────────────────────────
  // Adds expand/collapse behaviour to section and subsection entries.

  function initTocAccordion() {
    var chapterToc = document.querySelector("ul.chapter-toc");
    if (!chapterToc) return;

    chapterToc.querySelectorAll("li").forEach(function (li) {
      // Find direct child <ul>
      var childUl = null;
      for (var i = 0; i < li.children.length; i++) {
        if (li.children[i].tagName === "UL") { childUl = li.children[i]; break; }
      }
      if (!childUl) return;

      li.classList.add("has-children");

      // Find direct child <a>
      var link = null;
      for (var i = 0; i < li.children.length; i++) {
        if (li.children[i].tagName === "A") { link = li.children[i]; break; }
      }
      if (!link) return;

      link.addEventListener("click", function (e) {
        e.preventDefault();           // toggle only; navigate via active highlight
        li.classList.toggle("open");
      });
    });
  }

  // ── Video panel ──────────────────────────────────────────────

  var VIDEO_KEY = "video-panel-open";

  function initVideo() {
    var url = (window.videoUrl || "").trim();
    if (!url) return;

    var panel     = document.getElementById("video-panel");
    var frame     = document.getElementById("video-frame");
    var closeBtn  = document.getElementById("video-close-btn");
    var mainEl    = document.getElementById("main");
    if (!panel || !frame) return;

    frame.src = url;
    panel.style.display = "none";

    var activeOwner = null;

    function openAfter(owner) {
      owner.insertAdjacentElement("afterend", panel);
      panel.style.display = "block";
      frame.style.height = Math.round(panel.offsetWidth * 9 / 16) + "px";
      activeOwner = owner;
      var top = panel.getBoundingClientRect().top + mainEl.scrollTop - 56;
      mainEl.scrollTo({ top: top, behavior: "smooth" });
    }

    function closePanel() {
      panel.style.display = "none";
      activeOwner = null;
    }

    if (closeBtn) closeBtn.onclick = closePanel;

    var closeBottom = document.getElementById("video-close-bottom");
    if (closeBottom) closeBottom.onclick = closePanel;

    // Insert a ▶ button after every .callout-tip
    document.querySelectorAll(".callout.callout-tip").forEach(function (tip) {
      var trigger = document.createElement("button");
      trigger.className = "video-inline-btn";
      trigger.innerHTML = "&#9654; 观看视频";
      trigger.onclick = function () {
        if (activeOwner === trigger) {
          closePanel(); // same button → hide
        } else {
          openAfter(trigger); // different/new → show here
        }
      };
      tip.insertAdjacentElement("afterend", trigger);
    });
  }

  // ── Init ─────────────────────────────────────────────────────

  function init() {
    buildDocNav();
    applyAutonum();
    initTocAccordion();
    initTocHighlight();
    buildFigureCaptions();
    initVideo();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
