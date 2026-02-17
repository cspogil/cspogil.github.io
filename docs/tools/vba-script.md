# VBA Script for MS Word

The VBA script below can be used to create student versions from an instructor version of an activity in MS Word, as follows:

1. Create and save a MS Word file with the learning activity.
1. In the “Developer” tab, click on “Macros” and “Create”, and copy the VBA code below.
1. Define a new style named “Answer”. It should use the same font size and spacing as normal, but be visually different, e.g. in color and/or italics.
1. Apply the “Answer” style to all sample answers, instructor notes, etc.
1. Run the `removeAnswers()` function, which will copy the file with “-student” appended to the name, and then remove all text in the “Answer” style.
1. Review the student version and correct any problems.

[:material-download: Download VBA Script](vba-script.vb)

```vbnet
--8<-- "docs/tools/vba-script.vb"
```
