"""Knowledge areas from the Computer Science Curricula 2023."""

import os

areas = {
    "AI": "Artificial Intelligence",
    "AL": "Algorithmic Foundations",
    "AR": "Architecture and Organization",
    "DM": "Data Management",
    "FPL": "Foundations of Programming Languages",
    "GIT": "Graphics and Interactive Techniques",
    "HCI": "Human-Computer Interaction",
    "MSF": "Mathematical and Statistical Foundations",
    "NC": "Networking and Communication",
    "OS": "Operating Systems",
    "PDC": "Parallel and Distributed Computing",
    "SDF": "Software Development Fundamentals",
    "SE": "Software Engineering",
    "SEC": "Security",
    "SEP": "Society, Ethics, and the Profession",
    "SF": "Systems Fundamentals",
    "SPD": "Specialized Platform Development",
}


def main():
    """Stub out directory and index pages."""
    for abbr, title in areas.items():
        # create directory
        path = f"../docs/activities/{abbr}/"
        if not os.path.exists(path):
            os.mkdir(path)
        # create index page
        path += "index.md"
        head = f"# {title}\n"
        print(path, head, end="", sep="  ")
        # replace first line of file
        if os.path.exists(path):
            fin = open(path)
            lines = fin.readlines()
            lines[0] = head
            fin.close()
        else:
            lines = [head]
        # update/create the file
        out = open(path, "w")
        out.writelines(lines)
        out.close()


if __name__ == "__main__":
    main()
