"""Parse all BibTeX files and generate Markdown for each entry."""

import glob
import os


def write_page(entry, out):
    """Generate a standalone page for the entry (publication)."""

    # Create a reference format string
    author, year, title, source = get_fields(entry)
    ref = f"{author}. ({year}). {title}."
    if source:
        if entry.entry_type.startswith("in"):
            ref += f" In *{source}*."
        else:
            ref += f" *{source}*."

    # Generate the top section of the page
    # out.write("---\nhide:\n  - toc\n---\n\n")
    out.write(WARN + "\n\n")
    out.write(f"# {title}\n\n")
    out.write(f"**Reference:** {ref}\n\n")
    out.write('<div class="grid" markdown="1">\n\n')
    out.write(f"**Entry Key:** `#!tex \\cite{{{entry.key}}}`\n\n")
    out.write(f"**Entry Type:** `@{entry.entry_type}`\n\n")
    out.write("</div>\n")

    # Generate the entry section of the page
    write_entry(entry, out)


def gen_md_file(path, entry):
    """Generate a Markdown file for the entry (publication)."""

    # Rename files to match the key
    name = os.path.basename(path)
    if name != entry.key + ".bib":
        new_name = entry.key + ".bib"
        new_path = path[:-len(name)] + new_name
        os.rename(path, new_path)
        md_path = path[:-3] + "md"
        if os.path.exists(md_path):
            os.rename(md_path, new_path[:-3] + "md")
        path = new_path
        name = new_name


def main():
    """Generate md files and index pages."""
    acts = {}
    pubs = {}

    # Find and parse every bib file
    for path in sorted(glob.glob("docs/**/*.bib", recursive=True)):
        print(path)
        entry = parse_entry(path)
        if path.startswith("docs/research"):
            gen_md_file(path, entry)

            # Relative path from index page
            href = path[14:-3] + "md"
            pubs[href] = entry
        else:
            href = path[16:-3] + "md"
            acts[href] = entry

    # Generate the index pages
    gen_table("activities", acts)
    gen_table("research", pubs)


if __name__ == "__main__":
    main()
