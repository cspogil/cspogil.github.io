"""Add links to People pages by searching for names."""

import io
import re
import sys
import yaml

# Get imported bib2md
bib2md = sys.modules["hooks/bib2md.py"]

# Primary name of each person
INDEX = []

# Map alternative names to urls
PEOPLE = {}


def is_author(names, item):
    """Are any of the names an author of the item?"""
    authors = item[1].fields_dict["author"].value
    authors = bib2md.reformat_authors(authors).split(", ")
    return any(name in authors for name in names)


def on_files(files, config):
    """Called after the files collection is populated from the docs_dir."""
    INDEX.clear()
    PEOPLE.clear()
    for file in files:
        if file.src_uri.startswith("people") and file.src_uri.endswith(".md"):

            # Get the front matter block
            block = ""
            with open("docs/" + file.src_uri) as f:
                line = f.readline()
                if not line.startswith("---"):
                    continue  # Next file
                while not (line := f.readline()).startswith("---"):
                    block += line

            # Add each name to the dict
            data = yaml.safe_load(block)
            INDEX.append(data["names"][0])
            for name in data["names"]:
                PEOPLE[name] = file.src_uri


def on_page_markdown(markdown, page, config, files):
    """Called after the page's markdown is loaded from the source file."""

    # Build the people index page
    if page.url == "people/":
        out = io.StringIO()
        for name in INDEX:
            out.write(f"\n* [{name}](../{PEOPLE[name]})")
        return markdown + out.getvalue()

    # Add acts and pubs on individual person pages
    page_names = page.meta.get("names", [])
    if page_names:

        # Get this person's activities and publications
        acts = [item for item in bib2md.ACTS if is_author(page_names, item)]
        pubs = [item for item in bib2md.PUBS if is_author(page_names, item)]

        # Generate markdown for each list of items
        template = bib2md.ENV.get_template("listitem.md")
        out = io.StringIO()
        if acts:
            out.write("\n## Activities { data-search-exclude }\n\n")
            for href, entry in acts:
                href = "../" + href
                rendered = template.render(href=href, **bib2md.get_fields(entry))
                out.write(rendered)
        if pubs:
            out.write("\n## Research { data-search-exclude }\n\n")
            for href, entry in pubs:
                href = "../" + href[:-3] + "md"
                rendered = template.render(href=href, **bib2md.get_fields(entry))
                out.write(rendered)
        markdown += out.getvalue()

    # Get the text after the heading
    pattern = r"^\s*# (.+)$"
    match = re.search(pattern, markdown, re.MULTILINE)
    neck = match.end() if match else 0
    head = markdown[:neck]
    body = markdown[neck:]

    # Determine the relative path
    count = page.url.count("/")
    if not page.is_index:
        count -= 1
    path = "../" * count

    # Link every name in the body text (except on their own page)
    for name, url in PEOPLE.items():
        if name in page_names:
            continue
        repl = f"[{name}]({path}{url})"
        body = re.sub(name, repl, body)
    return head + body
