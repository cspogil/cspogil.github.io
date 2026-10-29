// Copy the table of contents to the top of the article
// (shown only when the right sidebar is not visible)

(function () {
  const toc = document.querySelector('.md-sidebar--secondary [data-md-component="toc"]');
  const h1 = document.querySelector('article h1');
  if (!toc || !h1) return;

  // Build a plain nested list from the sidebar links
  function copyList(navList) {
    const ul = document.createElement("ul");
    for (const navItem of navList.children) {
      const link = navItem.querySelector(':scope > a');
      if (!link) continue;
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = link.getAttribute("href");
      a.textContent = link.textContent.trim();
      li.appendChild(a);
      const subList = navItem.querySelector(':scope > nav > ul');
      if (subList) li.appendChild(copyList(subList));
      ul.appendChild(li);
    }
    return ul;
  }

  const section = document.createElement("section");
  section.className = "auto-toc";
  const title = document.createElement("strong");
  title.textContent = "Table of contents";
  section.appendChild(title);
  section.appendChild(copyList(toc));
  h1.after(section);

  // Hide the copy whenever the sidebar is visible
  const sidebar = toc.closest('.md-sidebar--secondary');
  function update() {
    if (!section.isConnected) {
      window.removeEventListener("resize", update);
      return;
    }
    section.hidden = sidebar.checkVisibility();
  }
  window.addEventListener("resize", update);
  update();
})();
