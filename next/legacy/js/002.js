
/* ===== ผลงาน — Shorts-style feed. Self-contained; runs only if .tk exists. ===== */
(function () {
  'use strict';
  var root = document.querySelector('.tk');
  if (!root || root.dataset.tkReady) return;
  root.dataset.tkReady = '1';

  var feed = root.querySelector('.tk-feed');
  var items = Array.prototype.slice.call(root.querySelectorAll('.tk-item'));
  var bars = Array.prototype.slice.call(root.querySelectorAll('.tk-bars i'));
  var idxBtns = Array.prototype.slice.call(root.querySelectorAll('.tk-index-btn'));
  var idxList = root.querySelector('.tk-index-list');
  var allBtn = root.querySelector('.tk-all');
  var prevBtn = root.querySelector('.tk-prev');
  var nextBtn = root.querySelector('.tk-next');
  var countEl = root.querySelector('.tk-count-n');
  var toastEl = root.querySelector('.tk-toast');
  var firstWork = root.querySelector('.tk-work');
  var mm = function (q) { return window.matchMedia ? window.matchMedia(q) : { matches: false }; };
  var reduce = mm('(prefers-reduced-motion: reduce)');
  var coarse = mm('(pointer: coarse)');
  var soundOn = false;      // shared across clips, like TikTok
  var liked = {};           // per-session, memory only
  var current = 0;

  function $(el, sel) { return el.querySelector(sel); }
  function vidOf(item) { return $(item, '.tk-vid'); }

  /* ---------- active item + HUD + list + arrows ---------- */
  function setActive(idx) {
    if (idx < 0 || idx >= items.length) return;
    current = idx;
    items.forEach(function (it, i) { it.classList.toggle('is-active', i === idx); });
    var kind = items[idx].dataset.kind;
    var wi = kind === 'work' ? +items[idx].dataset.i : (kind === 'outro' ? bars.length : -1);
    bars.forEach(function (b, i) {
      b.classList.toggle('is-on', i === wi);
      b.classList.toggle('is-done', i < wi);
    });
    if (countEl) countEl.textContent = wi < 0 ? 0 : Math.min(wi + 1, bars.length);
    root.classList.toggle('is-intro', kind === 'intro');
    if (firstWork && items.indexOf(firstWork) < idx) root.classList.add('is-scrolled');
    if (prevBtn) prevBtn.disabled = idx === 0;
    if (nextBtn) nextBtn.disabled = idx === items.length - 1;
    idxBtns.forEach(function (b) {
      var on = +b.dataset.tkGo === idx;
      if (on) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current');
      if (on && idxList) {   // keep the highlighted row in view without moving the page
        var top = b.offsetTop - idxList.offsetTop, bottom = top + b.offsetHeight;
        if (top < idxList.scrollTop) idxList.scrollTop = top - 8;
        else if (bottom > idxList.scrollTop + idxList.clientHeight) idxList.scrollTop = bottom - idxList.clientHeight + 8;
      }
    });
  }

  /* ---------- video: lazy src, play only when >=60% visible ---------- */
  function playItem(item) {
    var v = vidOf(item);
    if (!v) return;
    if (!v.getAttribute('src') && v.dataset.src) { v.src = v.dataset.src; }
    v.muted = !soundOn;
    if (reduce.matches && !item.dataset.userPlay) { item.classList.add('is-paused'); return; }
    var p = v.play();
    if (p && p.catch) {
      p.catch(function () {
        if (!v.muted) { v.muted = true; syncMuteButtons(false); v.play().catch(function () { item.classList.add('is-paused'); }); }
        else item.classList.add('is-paused');
      });
    }
  }
  function pauseItem(item) {
    var v = vidOf(item);
    if (v && !v.paused) v.pause();
  }

  items.forEach(function (item) {
    var v = vidOf(item);
    if (!v) return;
    v.addEventListener('playing', function () { v.classList.add('is-ready'); item.classList.remove('is-paused'); });
    v.addEventListener('pause', function () { if (item.classList.contains('is-visible')) item.classList.add('is-paused'); });
    v.addEventListener('error', function () { v.classList.remove('is-ready'); item.classList.remove('is-paused'); item.classList.add('is-novideo'); });
    var btn = $(item, '.tk-play');
    if (btn) btn.addEventListener('click', function () { item.dataset.userPlay = '1'; playItem(item); });
  });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var item = en.target;
        var on = en.isIntersecting && en.intersectionRatio >= 0.6;
        item.classList.toggle('is-visible', on);
        if (on) { setActive(items.indexOf(item)); playItem(item); }
        else { pauseItem(item); item.classList.remove('is-paused'); }
      });
    }, { root: feed, threshold: [0, 0.6, 1] });
    items.forEach(function (it) { io.observe(it); });
  }
  setActive(0);

  /* ---------- navigation ---------- */
  function nearest() {
    var st = feed.scrollTop, best = 0, d = Infinity;
    items.forEach(function (it, i) { var x = Math.abs(it.offsetTop - st); if (x < d) { d = x; best = i; } });
    return best;
  }
  function go(idx) {
    idx = Math.max(0, Math.min(items.length - 1, idx));
    feed.scrollTo({ top: items[idx].offsetTop, behavior: reduce.matches ? 'auto' : 'smooth' });
  }

  feed.addEventListener('keydown', function (e) {
    var k = e.key, d = 0;
    if (k === 'ArrowDown' || k === 'PageDown' || (k === ' ' && !e.shiftKey)) d = 1;
    else if (k === 'ArrowUp' || k === 'PageUp' || (k === ' ' && e.shiftKey)) d = -1;
    else if (k === 'Home') { e.preventDefault(); go(0); return; }
    else if (k === 'End') { e.preventDefault(); go(items.length - 1); return; }
    if (!d) return;
    if (e.target !== feed && /^(A|BUTTON)$/.test(e.target.tagName) && k === ' ') return;
    e.preventDefault();
    go(nearest() + d);
  });

  // Wheel / trackpad: one item per gesture, ignore the inertia tail.
  // At the first/last item the event is left alone so the page keeps scrolling.
  var wheelLock = false, wheelAcc = 0, lockedAt = 0, unlockTimer = 0;
  feed.addEventListener('wheel', function (e) {
    if (e.ctrlKey || Math.abs(e.deltaY) < Math.abs(e.deltaX)) return;
    var dir = e.deltaY > 0 ? 1 : -1;
    var at = nearest();
    if (!wheelLock && ((dir < 0 && at === 0 && feed.scrollTop <= 1) ||
        (dir > 0 && at === items.length - 1))) return;
    e.preventDefault();
    var now = Date.now();
    clearTimeout(unlockTimer);
    unlockTimer = setTimeout(function tryUnlock() {
      if (Date.now() - lockedAt > 450) { wheelLock = false; wheelAcc = 0; }
      else unlockTimer = setTimeout(tryUnlock, 80);
    }, 160);
    if (wheelLock) return;
    wheelAcc += e.deltaMode === 1 ? e.deltaY * 16 : e.deltaY;
    if (Math.abs(wheelAcc) < 24) return;
    wheelLock = true; lockedAt = now; wheelAcc = 0;
    go(at + dir);
  }, { passive: false });

  /* ---------- list of all works (sidebar on wide screens, bottom sheet otherwise) ---------- */
  function openSheet() {
    root.classList.add('is-sheet');
    if (allBtn) allBtn.setAttribute('aria-expanded', 'true');
    var cur = $(root, '.tk-index-btn[aria-current="true"]') || idxBtns[0];
    setTimeout(function () { if (cur) cur.focus({ preventScroll: true }); }, 50);
  }
  function closeSheet(returnFocus) {
    if (!root.classList.contains('is-sheet')) return;
    root.classList.remove('is-sheet');
    if (allBtn) { allBtn.setAttribute('aria-expanded', 'false'); if (returnFocus) allBtn.focus({ preventScroll: true }); }
  }
  root.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeSheet(true); });

  root.addEventListener('click', function (e) {
    var t = e.target;
    var el;
    if ((el = t.closest('[data-tk-go]'))) { closeSheet(false); go(+el.dataset.tkGo); }
    else if ((el = t.closest('[data-tk-step]'))) { go(current + (+el.dataset.tkStep)); }
    else if (t.closest('[data-tk-next]')) go(current + 1);
    else if (t.closest('[data-tk-top]')) go(1);
    else if (t.closest('.tk-all')) { if (root.classList.contains('is-sheet')) closeSheet(true); else openSheet(); }
    else if (t.closest('.tk-index-x') || t.closest('.tk-scrim')) closeSheet(true);
  });

  /* ---------- sound toggle ---------- */
  function syncMuteButtons(on) {
    soundOn = on;
    root.querySelectorAll('.tk-mute').forEach(function (b) {
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.setAttribute('aria-label', on ? 'ปิดเสียง' : 'เปิดเสียง');
      $(b, 'small').textContent = on ? 'ปิดเสียง' : 'เปิดเสียง';
    });
  }
  root.querySelectorAll('.tk-mute').forEach(function (b) {
    b.addEventListener('click', function () {
      syncMuteButtons(!soundOn);
      var item = b.closest('.tk-item');
      var v = vidOf(item);
      if (v) {
        v.muted = !soundOn;
        if (v.paused) { item.dataset.userPlay = '1'; playItem(item); }
      }
    });
  });

  /* ---------- toast + share (always ends in a visible toast) ---------- */
  var toastT = 0;
  function toast(msg, url) {
    toastEl.textContent = msg;
    toastEl.classList.toggle('is-url', !!url);
    if (url) {
      var c = document.createElement('code');
      c.textContent = url;
      toastEl.appendChild(c);
    }
    toastEl.classList.add('is-on');
    clearTimeout(toastT);
    toastT = setTimeout(function () { toastEl.classList.remove('is-on', 'is-url'); }, url ? 8000 : 1800);
  }
  function execCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text; ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;top:0;left:0;width:1px;height:1px;opacity:0;';
    root.appendChild(ta);
    var ok = false;
    try { ta.focus({ preventScroll: true }); ta.select(); ta.setSelectionRange(0, text.length); ok = document.execCommand('copy'); }
    catch (err) { ok = false; }
    root.removeChild(ta);
    return ok;
  }
  function copyLink(url) {
    var done = function () { toast('คัดลอกลิงก์แล้ว'); };
    var manual = function () {
      if (execCopy(url)) done();
      else toast('คัดลอกอัตโนมัติไม่ได้ กดค้างที่ลิงก์นี้เพื่อคัดลอก', url);
    };
    try {
      if (navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) {
        navigator.clipboard.writeText(url).then(done, manual);
        return;
      }
    } catch (err) { /* fall through */ }
    manual();
  }
  root.querySelectorAll('.tk-share').forEach(function (b) {
    b.addEventListener('click', function () {
      var item = b.closest('.tk-item');
      var url = item.dataset.link;
      var title = ($(item, '.tk-title') || {}).textContent || 'ผลงาน Hamster Hub';
      // Native share sheet on phones/tablets; desktops get a plain copy.
      if (navigator.share && coarse.matches) {
        var data = { title: title, text: title + ' — ผลงานของน้องๆ Hamster Hub', url: url };
        var can = true;
        try { if (navigator.canShare) can = navigator.canShare(data); } catch (err) { can = false; }
        if (can) {
          navigator.share(data).then(function () { toast('แชร์ลิงก์แล้ว'); }, function (err) {
            if (err && err.name === 'AbortError') toast('ยกเลิกการแชร์');
            else copyLink(url);
          });
          return;
        }
      }
      copyLink(url);
    });
  });

  /* ---------- heart ---------- */
  function burst(host, x, y) {
    var b = document.createElement('span');
    b.className = 'tk-burst';
    b.setAttribute('aria-hidden', 'true');
    if (x != null) { b.style.left = x + 'px'; b.style.top = y + 'px'; }
    var heart = $(root, '.tk-like .tk-ic svg');
    var h = document.createElement('span');
    h.className = 'tk-bh';
    if (heart) h.appendChild(heart.cloneNode(true));
    b.appendChild(h);
    for (var i = 0; i < 8; i++) {
      var s = document.createElement('i'), a = (i / 8) * Math.PI * 2, r = 46 + (i % 2) * 18;
      s.style.setProperty('--dx', Math.round(Math.cos(a) * r) + 'px');
      s.style.setProperty('--dy', Math.round(Math.sin(a) * r) + 'px');
      b.appendChild(s);
    }
    host.appendChild(b);
    setTimeout(function () { b.remove(); }, 900);
  }
  function setLiked(item, on) {
    liked[item.dataset.i] = on;
    var btn = $(item, '.tk-like');
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.setAttribute('aria-label', on ? 'เลิกชอบผลงานนี้' : 'ชอบผลงานนี้');
    if (on) {
      btn.classList.remove('is-pop'); void btn.offsetWidth; btn.classList.add('is-pop');
      burst(btn, null, null);
    }
  }
  root.querySelectorAll('.tk-like').forEach(function (b) {
    b.addEventListener('click', function () {
      var item = b.closest('.tk-item');
      setLiked(item, !liked[item.dataset.i]);
    });
  });

  // Double-click / double-tap on the media only (never on links or buttons) = like + burst.
  function mediaLike(item, cx, cy) {
    var r = item.getBoundingClientRect();
    burst(item, cx - r.left, cy - r.top);
    if (!liked[item.dataset.i]) setLiked(item, true);
  }
  root.querySelectorAll('.tk-work').forEach(function (item) {
    var stage = $(item, '.tk-stage');
    var lastTap = 0, lx = 0, ly = 0, touchLikeAt = 0;
    stage.addEventListener('dblclick', function (e) {
      if (e.target.closest('a,button') || Date.now() - touchLikeAt < 600) return;
      mediaLike(item, e.clientX, e.clientY);
    });
    stage.addEventListener('pointerup', function (e) {
      if (e.pointerType !== 'touch' || e.target.closest('a,button')) return;
      var now = Date.now();
      if (now - lastTap < 320 && Math.abs(e.clientX - lx) < 40 && Math.abs(e.clientY - ly) < 40) {
        mediaLike(item, e.clientX, e.clientY);
        lastTap = 0; touchLikeAt = now;
      } else { lastTap = now; lx = e.clientX; ly = e.clientY; }
    });
  });

  document.addEventListener('visibilitychange', function () {
    if (document.hidden) items.forEach(pauseItem);
    else if (items[current] && items[current].classList.contains('is-visible')) playItem(items[current]);
  });
})();


