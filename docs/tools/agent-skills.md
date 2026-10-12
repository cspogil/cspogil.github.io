# Agent Skills for LLMs

An [agent skill](https://agentskills.io/) is a folder of instructions, scripts, and other resources that an AI large language model (LLM) loads when it is relevant to the task at hand.
Skills use an open format that Claude, ChatGPT, and Gemini can all import.
A skill can encode expertise that a general-purpose assistant lacks, such as how to write an activity that follows POGIL pedagogy.

## pogil-activity-writer

[**pogil-activity-writer**](https://github.com/ChrisMayfield/claude-skills/tree/main/pogil-activity-writer) helps authors draft guided inquiry activities through an interactive **backward-design** workflow.
Instead of generating an activity in one shot, the skill turns authoring into a conversation:

1. Starting from the topic, course, and class length, the LLM proposes learning objectives, process skill goals, application questions, and concept invention questions.
2. Only then does it design the models and exploration questions, one model at a time.
3. At each step, you (the content expert) correct and extend each proposal before moving on.

Core pedagogical principles are built in as guardrails.
For example, terms are not introduced before the key question, models contain contrasting cases that distinguish the concept, and process skills are developed by the structure of the questions.

The result is two Word documents, ready to print or to upload to Google Docs:

* A **teacher version** with sample answers and facilitation notes.
* A **student version** with answer boxes sized to the expected answers.

Both are built from a single Markdown source, so you can revise the activity in the future and rebuild the word docs.

To preview exactly what the LLM is told, read the skill's instructions in [SKILL.md][S].
When you are ready to try it, [README.md][R] explains how to install the skill on each platform and how to start a conversation.
If you have questions or feedback, please contact Chris Mayfield.

[R]: https://github.com/ChrisMayfield/claude-skills/blob/main/pogil-activity-writer/README.md
[S]: https://github.com/ChrisMayfield/claude-skills/blob/main/pogil-activity-writer/SKILL.md

!!! note
    Drafts produced by this skill are not POGIL activities.
    POGIL® is a registered trademark of The POGIL Project, reserved for materials that have been [reviewed and endorsed](https://pogil.org/authoring-materials/endorsement-publication).
    The drafts are starting points that authors can test in class, revise, and submit for review.
