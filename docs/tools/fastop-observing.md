---
parent: tools/fastop.md
---

# Observing with FASTOP

<script src="../../auto-toc.js"></script>


## How to conduct a FASTOP observation?

In our research, we used FASTOP in two kinds of observations:

- **Student-level observations** (live, in the classroom).
  The observer follows a sample of 8–12 specific students, plus the instructor.
  Every minute, the observer records the *action* codes for each student and for the instructor.
  Focus codes are not recorded.
- **Class-level observations** (from a video recording of the entire class).
  The observer codes the students as a group and the instructor.
  Every minute, the observer records both the *focus* and *action* codes for students and for the instructor.

In both kinds of observations:

- Record every code that applies during each one-minute interval.
  For example, a student might *Work* and *Discuss* in the same minute.
- Write a brief note whenever the class switches to a different activity
  (e.g., from lecture to teamwork), so the session can be split into segments later.
- Note anything unusual, such as technical problems or interruptions.

For student-level observations, we used the following IRB-approved procedure to protect student privacy:

1. Near the start of the term, students watched a short video describing the study
   and were invited to complete an informed consent form.
2. A colleague (not the instructor) collected the forms, so the instructor did not know which students consented.
3. The colleague used the list of consenting students and the instructor's team assignments
   to select the students to observe, and gave the observer photos of those students.

New observers should practice coding with classroom videos before observing a live class,
and compare their codes with an experienced observer.


## What are some tips for coding?

Some codes can be difficult to tell apart.
Here are some guidelines for common situations:

- **Ask, Answer, or Discuss?**
  If one person asks a question and another person answers, code *Ask* and *Answer*.
  If the conversation goes back and forth (more than one question and answer), code *Discuss*.
- **Speak or Ask?**
  If the teacher presents without interaction, code *Speak*.
  If the teacher poses a question and waits for students to respond, code *Ask*.
- **Work or Watch/Listen?**
  Students who listen to a lecture are *Watch/Listen* with focus *Class*.
  Students who take notes or work on their own are *Work* with focus *Solo*.
  If students do both during the same minute, code both.
- **Teacher walking around the room?**
  If the teacher monitors the class without talking to anyone, code *Watch/Listen* with focus *Class*.
  If the teacher stops to talk with a team, code *Discuss* (or *Ask* or *Answer*) with focus *Team*.
  If the teacher talks with two or more teams at the same time, use focus *Teams*.
- **Not sure?**
  Record the codes that seem closest, and write a note explaining what happened.

In data files, codes are prefixed with **S-** (student) or **I-** (instructor),
and *Watch/Listen* is abbreviated as *Watch* (e.g., `S-Watch`, `I-Speak`).


## What FASTOP codes are typical for various classroom activities?

This table shows the expected FASTOP codes for various classroom activities.
When a cell has multiple lines, each focus code is paired with the action code(s) on the same line.
For example, during a traditional lecture, some students watch/listen as a whole class,
some discuss in pairs, and some work alone or are distracted.

POGIL classes alternate between two modes:
teams work on an activity while the teacher monitors the class and interacts with teams,
and the teacher has teams "report out" their answers to the whole class.
Peer Instruction repeats a cycle of steps:
(a) the teacher poses a question, (b) students answer individually,
(c) the teacher presents the distribution of answers, (d) students discuss in pairs,
(e) students answer individually again, and (f) the teacher again presents the answers.

<div class="compact" markdown> <!-- affects mkdocs but not VSCodium preview -->

|                         Activity |        Teacher Focus | Teacher Action                 |           Student Focus | Student Action                                |
| -------------------------------: | -------------------: | ------------------------------ | ----------------------: | --------------------------------------------- |
|              Traditional Lecture |                Class | Speak                          | Class<br/>Pair<br/>Solo | Watch/Listen<br/>Discuss<br/>Work, Distracted |
|              Computer Laboratory | Class<br/>Solo, Pair | Watch/Listen<br/>Discuss, Work |           Solo<br/>Pair | Work<br/>Work, Discuss                        |
|                   POGIL Teamwork |       Class<br/>Team | Watch/Listen<br/>Discuss       |                    Team | Discuss, Work                                 |
|                 POGIL Report Out |                Class | Ask, Discuss                   |                   Class | Answer                                        |
|    Peer Instruction (a) question |                Class | Speak, Ask                     |                   Class | Watch/Listen                                  |
|      Peer Instruction (b) answer |                Class | Watch/Listen                   |                    Solo | Answer                                        |
|     Peer Instruction (c) results |                Class | Speak, Ask                     |                   Class | Watch/Listen                                  |
|     Peer Instruction (d) discuss |                Class | Watch/Listen                   |                    Pair | Discuss                                       |
|      Peer Instruction (e) answer |                Class | Ask                            |                    Solo | Answer                                        |
|     Peer Instruction (f) results |                Class | Speak                          |                   Class | Watch/Listen                                  |

</div>

See [FASTOP for Researchers](fastop-research.md) for a table and plots of FASTOP codes from real classrooms.
