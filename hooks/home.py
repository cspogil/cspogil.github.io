"""Make the site_name link to the home page."""

import os


def patch(output, config):
    """Find and modify each site_name."""
    # logo = config["theme"]["logo"]
    logo = 'aria-label="CS-POGIL"'
    name = config["site_name"]
    link = f'<a href="/">{name}</a>'
    beg = 0
    while (beg := output.find(logo, beg)) > -1:
        # Find site_name after the logo
        beg = output.index(name, beg + len(logo))
        end = beg + len(name)
        output = output[:beg] + link + output[end:]
    return output.replace('title="CS-POGIL"', 'title="Home Page"')


def on_post_page(output, page, config):
    """Called after the template is rendered."""
    return patch(output, config)


def on_post_build(config):
    """Use this event to call post-build scripts."""
    path = config["site_dir"] + os.sep + "404.html"
    with open(path, "r") as file:
        output = file.read()
    output = patch(output, config)
    with open(path, "w") as file:
        file.write(output)
