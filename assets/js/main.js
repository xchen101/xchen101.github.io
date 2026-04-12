/* main.js — no dependencies.
 * 1. Smooth-scroll for same-page anchor links.
 * 2. Active nav highlighting via IntersectionObserver.
 * 3. Progressive enhancement of repo cards with live GitHub stats.
 */

(function () {
  'use strict';

  // --- 1. Smooth scroll for anchor links on the landing page ------------------
  function initSmoothScroll() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href^="/#"], a[href^="#"]');
      if (!link) return;
      var href = link.getAttribute('href');
      var hash = href.indexOf('#') === -1 ? null : href.slice(href.indexOf('#') + 1);
      if (!hash) return;
      var target = document.getElementById(hash);
      if (!target) return; // let the browser navigate normally if not on this page
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      if (history.replaceState) history.replaceState(null, '', '#' + hash);
    });
  }

  // --- 2. Active nav highlighting (landing page only) ------------------------
  function initNavObserver() {
    var sections = document.querySelectorAll('.landing-section[id]');
    if (!sections.length) return;
    var navLinks = {};
    document.querySelectorAll('.nav-link[data-nav]').forEach(function (el) {
      navLinks[el.getAttribute('data-nav')] = el;
    });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = entry.target.id;
        Object.keys(navLinks).forEach(function (key) {
          navLinks[key].classList.toggle('active', key === id);
        });
      });
    }, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });

    sections.forEach(function (section) { observer.observe(section); });
  }

  // --- 3. GitHub stats enhancement -------------------------------------------
  function initRepoCards() {
    var cards = document.querySelectorAll('.repo-card[data-repo]');
    if (!cards.length) return;

    cards.forEach(function (card) {
      var repo = card.getAttribute('data-repo');
      var starsEl = card.querySelector('[data-stars]');
      var updatedEl = card.querySelector('[data-updated]');

      fetch('https://api.github.com/repos/' + repo)
        .then(function (r) { if (!r.ok) throw new Error('GitHub API ' + r.status); return r.json(); })
        .then(function (data) {
          if (starsEl) starsEl.textContent = '★ ' + formatCount(data.stargazers_count);
          if (updatedEl) updatedEl.textContent = 'Updated ' + formatRelativeTime(data.pushed_at);
        })
        .catch(function () {
          // Leave placeholder text if API fails or rate-limits.
          if (starsEl) starsEl.textContent = '★';
          if (updatedEl) updatedEl.textContent = '';
        });
    });
  }

  function formatCount(n) {
    if (n >= 1000) return (n / 1000).toFixed(1).replace(/\.0$/, '') + 'k';
    return String(n);
  }

  function formatRelativeTime(iso) {
    if (!iso) return '';
    var then = new Date(iso).getTime();
    var diffSec = Math.max(0, (Date.now() - then) / 1000);
    if (diffSec < 60) return 'just now';
    if (diffSec < 3600) return Math.floor(diffSec / 60) + 'm ago';
    if (diffSec < 86400) return Math.floor(diffSec / 3600) + 'h ago';
    if (diffSec < 2592000) return Math.floor(diffSec / 86400) + 'd ago';
    if (diffSec < 31536000) return Math.floor(diffSec / 2592000) + 'mo ago';
    return Math.floor(diffSec / 31536000) + 'y ago';
  }

  // --- Init ------------------------------------------------------------------
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initSmoothScroll();
      initNavObserver();
      initRepoCards();
    });
  } else {
    initSmoothScroll();
    initNavObserver();
    initRepoCards();
  }
})();
