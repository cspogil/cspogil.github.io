# Classroom Activity Utility for Google Docs

![Raven Icon](img/raven_icon_128x128.png){ align=right }

The **Classroom Activity Utility (CAU)** is a Google Docs add-on to help teachers to create and revise classroom activities. CAU can use an author’s version of an activity to generate versions for students and teachers. Specifically, CAU will:

* Remove sample answers and teacher notes **within** the activity (anything in a selected paragraph style).
* Remove teacher information at the **start and end** of the activity (anything before and after selected tags).

For details, contact Clif Kussmaul (clif@kussmaul.org).

## To use CAU

1. Install from:
https://workspace.google.com/u/0/marketplace/app/classroom_activity_utility/782628538794
    * Google warns that CAU is not verified. Click “Advanced”, then “Go to Classroom Activity Utility (unsafe)”.
    * Check all three permissions (see **Permissions** below). If any are unchecked, CAU asks again when you use it.
2. Create a document with a classroom activity, or import from other formats (e.g. Microsoft Word).
3. Use a specific paragraph style (**Heading 4**, by default) for answers, teacher notes, and other text that should be in the teacher version but not the student version. In Google Docs you can change the formatting for a paragraph style, and it often makes sense for this style to be the same size & font as normal text, but with a different color or format (italics, underline, etc).
4. Optionally, add tags to identify text at the start and end of the document that should also be removed (see **Document Structure** below).
5. From Extensions > Classroom Activity Utility, select “Make student version”, “Make teacher version”, etc.
6. The new versions should appear in the same folder as the author’s master version.
    * Note: If “Remove old versions” is checked in Settings (the default), CAU replaces earlier versions with the same name.
7. From Extensions > Classroom Activity Utility, select “Settings” to adjust settings and enable some advanced features.
8. If the document has tabs, CAU uses the current tab (and any parent tabs), and removes other tabs from the new versions.
    * To use several tabs, open Settings and check “Process all tabs (not just current) with author suffix”. CAU then keeps every tab whose title ends with the author suffix (“(Author)” by default).
    * In each kept tab title, CAU replaces the author suffix (e.g. “Activity (Author)” becomes “Activity (Student)”).
    * If no tab title ends with the suffix, CAU shows an error and makes no files. If the setting is off but other tab titles end with the suffix, CAU asks before continuing.
    * Tags such as `{{TITLE}}` are replaced separately in each tab, including its headers and footers.

See **Advanced Features** below for other features in development.


### Permissions

CAU needs three permissions. Google lets you uncheck each one, but CAU needs all three and asks again if any are missing.

* “See, edit, create, and delete all your Google Docs documents”: CAU edits the new versions it creates. It never changes the author’s document.
* “See, edit, create, and delete all of your Google Drive files”: CAU copies the author’s document, saves new versions and PDFs in the same folder, and removes old versions. A narrower Drive permission would not let CAU see the document you have open.
* “Display and run third-party web content in prompts and sidebars inside Google applications”: Google’s wording for showing CAU’s own Settings dialog, sidebars, and messages. CAU does not load content from other websites.

Google shows the “unverified” warning because CAU uses full Drive access, and Google requires a security review before verifying apps with that access. CAU is a small, free tool and has not gone through that review.


## Document Structure

If there is a `{{TEACHER START}}` tag, any text **before** it will be **removed** from the teacher version. If there is a `{{TEACHER STOP}}` tag, any text **after** it will be **removed** from the teacher version. These tags can be used to exclude information for the author(s), such as a list of changes to be made, a revision history, or draft content that is not yet part of the main activity.

If there is a `{{STUDENT START}}` tag, any text **before** it will be **removed** from the student version. If there is a `{{STUDENT STOP}}` tag, any text **after** it will be **removed** from the student version. These tags can be used to exclude information for teachers, such as prerequisites, learning outcomes, notes on how to adapt the activity, sample homework, test questions, and handouts.

Similarly, `{{SAMPLE START}}` and `{{SAMPLE STOP}}` can be used to create a sample version.

Thus, a typical document with all 4 teacher and student tags would look like this:

| initial text<br/>for author | `{{TEACHER START}}` | initial text<br/>for teachers | `{{STUDENT START}}` | main body<br/>of activity | `{{STUDENT STOP}}` | final text<br/>for teachers | `{{TEACHER STOP}}` | final text<br/>for author |
| --------------------------- | ------------------- | ----------------------------- | ------------------- | ------------------------- | ------------------ | --------------------------- | ------------------ | ------------------------- |

If `{{TEACHER START}}` does not appear, all initial text will be in the teacher version. If `{{TEACHER STOP}}` does not appear, all final text will be in the teacher version. Thus, if the document starts with the body of the activity, both START tags can be left out. Similarly, one or both of the `STUDENT` or `SAMPLE` tags can be omitted.

The following table shows the author version (far left), and the resulting versions for teachers (middle left) and students (middle right).

| Author Version                                                                                                                                       | Teacher Version                                                                                                                                      | Student Version                                       | Notes                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- |
| **Things To Do**                                                                                                                                     |                                                                                                                                                      |                                                       | *content for author only*                                              |
| `{{TEACHER START}}`                                                                                                                                  |                                                                                                                                                      |                                                       | *if this tag is not used, teacher version starts at start of document* |
| **Overview**<br/> This activity ...<br/> **Prerequisites**<br/> Students should be able to ...<br/> **Objectives**<br/> Students will be able to ... | **Overview**<br/> This activity ...<br/> **Prerequisites**<br/> Students should be able to ...<br/> **Objectives**<br/> Students will be able to ... |                                                       | *content for teachers (before `STUDENT START`)*                        |
| `{{STUDENT START}}`                                                                                                                                  |                                                                                                                                                      |                                                       | *if this tag is not used, student version starts at start of document* |
| **Introduction**<br/> What color was the white horse?                                                                                                | **Introduction**<br/> What color was the white horse?                                                                                                | **Introduction**<br/> What color was the white horse? | *body of activity*                                                     |
| *ANSWER: White*                                                                                                                                      | *ANSWER: White*                                                                                                                                      |                                                       | *answers removed*                                                      |
| `{{STUDENT STOP}}`                                                                                                                                   |                                                                                                                                                      |                                                       | *if this tag is not used, student version ends at end of document*     |
| **References**<br/><br/> **Sample Test Questions**                                                                                                   | **References**<br/><br/> **Sample Test Questions**                                                                                                   |                                                       | *content for teachers (after `STUDENT STOP`, before `TEACHER STOP`)*   |
| `{{TEACHER STOP}}`                                                                                                                                   |                                                                                                                                                      |                                                       | *if this tag is not used, teacher version ends at end of document*     |
| **Revision History**                                                                                                                                 |                                                                                                                                                      |                                                       | *content for author only (after `TEACHER STOP`)*                       |


## Advanced Features

CAU has other features in development. If you are eager to use them or have comments or suggestions, please contact Clif Kussmaul (clif@kussmaul.org).

* CAU can replace tags with values, in the body, headers, and footers:
    `{{DATE}}` (current date), `{{YEAR}}`, `{{NAME}}` (file name), `{{TITLE}}` (first Title paragraph), `{{NEWLINE}}`,
    `{{CC-BY}}`, `{{CC-BY-NC}}`, `{{CC-BY-NC-SA}}` (Creative Commons licenses with image and link),
    `{{CS-POGIL}}`, `{{POGIL}}` (project names with links).
* CAU can compute readability scores and flag text that may be difficult to read.
* CAU can check for some problems with colors, fonts, image size, etc.
