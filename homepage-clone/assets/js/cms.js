(function () {
  var SUPABASE_URL = "https://ppyffkabfavifyrwohhp.supabase.co";
  var SUPABASE_ANON_KEY =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBweWZma2FiZmF2aWZ5cndvaGhwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQyMzc3MDQsImV4cCI6MjA5OTgxMzcwNH0.LP8zcKY2Rv9KfPX0QesyjH5bu56oiZmKB2_vHQUwoiM";

  var slug = document.body.getAttribute("data-page-slug") || "home";

  function applyRow(row) {
    var els = document.querySelectorAll(
      '[data-cms-id="' + row.cms_key + '"]'
    );
    if (!els.length) return;
    els.forEach(function (el) {
      switch (row.field_type) {
        case "image":
        case "video":
          if (
            el.tagName === "IMG" ||
            el.tagName === "SOURCE" ||
            el.tagName === "IFRAME" ||
            el.tagName === "VIDEO"
          ) {
            el.setAttribute("src", row.value);
          }
          break;
        case "email":
          el.textContent = row.value;
          el.setAttribute("href", "mailto:" + row.value);
          break;
        case "text":
        default:
          el.textContent = row.value;
      }
    });
  }

  var url =
    SUPABASE_URL +
    "/rest/v1/site_content?select=cms_key,field_type,value&or=(page_slug.eq." +
    encodeURIComponent(slug) +
    ",page_slug.eq.global)";

  fetch(url, {
    headers: {
      apikey: SUPABASE_ANON_KEY,
      Authorization: "Bearer " + SUPABASE_ANON_KEY,
    },
  })
    .then(function (r) {
      if (!r.ok) throw new Error("Supabase error " + r.status);
      return r.json();
    })
    .then(function (rows) {
      rows.forEach(applyRow);
      document.dispatchEvent(new CustomEvent("cms:applied", { detail: rows }));
    })
    .catch(function (err) {
      console.error("[CMS] failed to load content", err);
    });
})();
