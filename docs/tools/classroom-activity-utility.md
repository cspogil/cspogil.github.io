# Classroom Activity Utility

![Raven Icon](img/raven_icon_128x128.png){ align=right }

The **Classroom Activity Utility (CAU)** is a Google Docs add-on to help teachers to create and revise classroom activities. CAU can use an author’s version of an activity to generate versions for students and teachers. Specifically, CAU will:

* Remove sample answers and teacher notes **within** the activity (anything in a selected heading style).
* Remove teacher information at the **start and end** of the activity (anything before and after selected tags).

For details, contact Clif Kussmaul [clif@kussmaul.org](mailto:clif@kussmaul.org).

To use CAU:

1. Install from:
https://workspace.google.com/u/0/marketplace/app/classroom_activity_utility/782628538794
1. Create a document with a classroom activity, or import from other formats (e.g. Microsoft Word).
2. Use a specific text style (**Heading 4**, by default) for answers, teacher notes, and other text that should be in the teacher version but not the student version. Note that in Google Doc you can change the formatting for a text style, and it often makes sense for this text style to be the same size & font as normal text, but with a different color or format (italics, underline, etc).
3. Optionally, add tags to identify text at the start and end of the document that should also be removed (see **Document Structure** below).
4. From the Add-ons menu, select “Make student version”, “Make teacher version”, etc.
5. The new versions should appear in the same folder as the author’s master version.
   * Note: If several people are editing the same document, you may need to delete the generated documents so that CAU can create new versions.
6. From the Add-ons menu, select “Settings” to adjust settings and enable some advanced features.

See **Advanced Features** below for other features in development.

## Document Structure

If there is a `{{TEACHER START}}` tag, any text **before** it will be **removed** from the teacher version. If there is a `{{TEACHER STOP}}` tag, any text **after** it will be **removed** from the teacher version. These tags can be used to exclude information for the author(s), such as a list of changes to be made, a revision history, or draft content that is not yet part of the main activity.

If there is a `{{STUDENT START}}` tag, any text **before** it will be **removed** from the student version. If there is a `{{STUDENT STOP}}` tag, and text **after** it will be **removed** from the student version. These tags can be used to exclude information for teachers, such as prerequisites, learning outcomes, notes on how to adapt the activity, sample homework, test questions, and handouts.

Similarly, `{{SAMPLE START}}` and` {{SAMPLE STOP}}` can be used to create a sample version.

Thus, a typical document with all 4 teacher and student tags would look like this:

| initial text<br/>for author | `{{TEACHER START}}` | initial text<br/>for teachers | `{{STUDENT START}}` | main body<br/>of activity | `{{STUDENT STOP}}` | final text<br/>for teachers | `{{TEACHER STOP}}` | final text<br/>for author |
|-------------------------|---------------------|---------------------------|---------------------|-----------------------|--------------------|-------------------------|--------------------|-----------------------|
<br/>

If `{{TEACHER START}}` does not appear, all initial text will be in the teacher version. If `{{TEACHER STOP}}` does not appear, all final text will be in the teacher version. Thus, if the document starts with the body of the activity, both START tags can be left out. Similarly, one or both of the `STUDENT` or `SAMPLE` tags can be omitted.

The following table shows the author version (far left), and the resulting versions for teachers (middle left) and students (middle right).

| Author Version                                                                                                                                       | Teacher Version                                                                                                                                      | Student Version                                       | Notes                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------------------------|
| **Things To Do**                                                                                                                                     |                                                                                                                                                      |                                                       | *content for author only*                                              |
| `{{TEACHER_START}}`                                                                                                                                  |                                                                                                                                                      |                                                       | *if this tag is not used, teacher version starts at start of document* |
| **Overview**<br/> This activity ...<br/> **Prerequisites**<br/> Students should be able to ...<br/> **Objectives**<br/> Students will be able to ... | **Overview**<br/> This activity ...<br/> **Prerequisites**<br/> Students should be able to ...<br/> **Objectives**<br/> Students will be able to ... |                                                       | *content for teachers (before `STUDENT START`)*                         |
| `{{STUDENT START}}`                                                                                                                                  |                                                                                                                                                      |                                                       | *if this tag is not used, student version starts at start of document* |
| **Introduction**<br/> What color was the white horse?                                                                                                | **Introduction**<br/> What color was the white horse?                                                                                                | **Introduction**<br/> What color was the white horse? | *body of activity*                                                     |
| *ANSWER: White*                                                                                                                                      | *ANSWER: White*                                                                                                                                      |                                                       | *answers removed*                                                      |
| `{{STUDENT STOP}}`                                                                                                                                   |                                                                                                                                                      |                                                       | *if this tag is not used, student version ends at end of document*     |
| **References**<br/><br/> **Sample Test Questions**                                                                                                   | **References**<br/><br/> **Sample Test Questions**                                                                                                   |                                                       | *content for teachers (after `STUDENT STOP`, before `TEACHER STOP`)*   |
| `{{TEACHER STOP}}`                                                                                                                                   |                                                                                                                                                      |                                                       | *if this tag is not used, teacher version ends at end of document*     |
| **Revision History**                                                                                                                                 |                                                                                                                                                      |                                                       | *content for author only (after `TEACHER STOP`)*                       |

<br/>

## Advanced Features

CAU has other features in development. If you are eager to use them or have comments or suggestions, please contact Clif Kussmaul [clif@kussmaul.org](mailto:clif@kussmaul.org).

* CAU can insert headers and footers if they are not set in the document.
* CAU can replace tags with values, e.g. `{{DATE}}` for current date, `{{TITLE}}` for title,
`{{CC-BY}}` for a Creative Commons Attribution License.
* CAU can compute readability scores and flag text that may be difficult to read.
* CAU can check for some problems with colors, fonts, image size, etc.