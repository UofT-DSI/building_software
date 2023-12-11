# Building Research Software

## Contents:
1. [Description](https://github.com/rachaellam/dsi-workshop#description)
2. [Learning Outcomes](https://github.com/rachaellam/dsi-workshop#learning-outcomes)
3. [Logistics](https://github.com/rachaellam/dsi-workshop#logistics)
4. [Marking Scheme](https://github.com/rachaellam/dsi-workshop#marking-scheme)
5. [Policies](https://github.com/rachaellam/dsi-workshop#policies)
6. [Folder Structure](https://github.com/rachaellam/dsi-workshop#folder-structure)
7. [Acknowledgements and Contributions](https://github.com/rachaellam/dsi-workshop#acknowledgements-and-contributions)

## Description:
Much research these days is done using software. Researchers need to develop a comfort with building, maintaining and improving high-quality software. This course focuses on equipping students with the skills to build robust software that can be used to answer research questions. It focuses on how to effectively write short programs, as part of a small team, in a reproducible way. Research software that is built correctly can be used by other teams, not just the researcher who originally wrote it.

## Learning Outcomes
Students will know how to:
1. Learn how to work as a team within a Git/GitHub setting. Specifically, branching, merging, conflicts, and pull requests.
2. Know how to create bug reports and prioritize requests.
3. Develop a comfort with using makefiles and configuring programs.
4. Proficiently test software, handle errors, and track provenance
5. Know how to create Python packages.
6. Acquire a comfort with calling APIs. 
7. Develop comfort with Docker


## Logistics

### Course Contacts
* Instructor: [**Name**] [Pronouns] [degree]. hyperlinked email
  * Email etiquette
  * Other comments 
* TA: [**Name**] [pronouns] [degree]. hyperlinkedEmail

### Delivery instructions
The workshop will be held over three weeks, three days a week. Two of the three days will be 2-hours long and the last day will be 3-hours. Being mindful of online fatigue, there will be one break during each class where students are encouraged to stretch, grab a drink and snacks, or ask any additional questions.

### Technology Requirements
1. Camera is optional although highly encouraged. We understand that not everyone may have the space at home to have the camera on.


### Lesson Schedule
| Lesson | Topic                                                                                        | Assignments      | Resources  |
|--------|----------------------------------------------------------------------------------------------|------------------|------------|
| 1      | Unix Shell I <br>(introducing the Shell, introductory commands, files and directories)       | [Assignment 1]() | [Slides]() |
| 2      | Unix Shell II<br>(input/output and pipes/filters)                                            | [Assignment 1]() | [Slides]() |
| 3      | Unix Shell III<br>(shell scripts, shell functions, parameters, flow control)                 | [Assignment 1]() | [Slides]() |
| 4      | Version Control and GitHub I<br>(introducing version control and GitHub, basic Git commands) | [Assignment 2]() | [Slides]() |
| 5      | Version Control and GitHub II<br>(remote repositories; branching)                            | [Assignment 2]() | [Slides]() |
| 6      | Version Control and GitHub III <br>(collaborating, dealing with conflicts)                   | [Assignment 2]() | [Slides]() |
| 7      | Problem solve, reproducibility, ethics, inequity                                             | [Assignment 1]() <br> [Assignment 2]() | [Slides]() |
| 8      | Professional Skills - Industry Case Study                                                    | [Assignment 2]() | [Slides]() |
| 9      | Data Science Foundations - Review and Practice                                               |                  | [Slides]() |

## Marking Scheme
| Assessment       | Weight | Description | Due Date |
|------------------|--------|-------------|----------|
| [Assignment 1]() |        |             |          |
| [Assignment 2]() |        |             |          |
|                  |        |             |          |

## Policies
The course is a live-coding class. Students are expected to follow along with the coding, creating files and folders to navigate and manipulate. Students should be active participants while coding and are encouraged to ask questions throughout. Although slides will be available for students to reference, they should be referenced before or after class, as during class will be dedicated to coding with the instructor.

**How to submit assignments, late policy, academic integrity.**

## Folder Structure
Below are the folders contained in this repo with a description of what they contain and information on how to use them.

### 1 *assignments*:
This folder contains the assignments for the workshop. Students are expected to complete them one week after the content has been delivered.

### 2. *homework*:
This folder contains homework for students to practice Unix and Git/GitHub workshops. Please complete the Unix Shell homework in the first week, and the Git/GitHub homework in the second.

There are pdf copies of the homework and markdown files, which can be edited. The homework can change based on the amount of content that was completed each day.

Homework is just a suggestion but will help students throughout the workshop, as content is cumulative and will only get more difficult. Unfortunately, there is not enough time to review previous content each class so while this homework is **not** graded, it is highly recommended.

### 3. *lessons*:
This folder contains the pdf and html version of the slides. Either the pdf slides or the html slides can be used when teaching. If slides are edited to contain any gifs, the instructor will need to use the html slides so that the gifs are active.

pdf slides should be referenced before class to prepare or after class to review. During class will be live-coding, therefore, there is no need to follow them during class. They contain all information that was discussed in class and are a great resource in the future if students need to reassess their knowledge.

### 4. *post-course*:
This folder contains the exit surveys for students to complete. It holds both the md and docx versions of the survey.

### 5. *slides-resources*:
This folder contains all editable slides. To edit, download the entire folder, including the *pics* folder as this folder contains the pictures which are relationally referenced in the markdown files.

To change a photo, edit the markdown where photos are referenced.

Example: 

Change `![w:1150 center](pics/github.png)` to `![bg](pics/github.png)`

To add a photo, add photo to the *pics* folder and reference it within the markdown file.

Example:

Added photo labelled "git_commit.png" will be referenced in markdown file as `![w:1000 left](pics/git_commit.png)`

## Acknowledgements and Contributions
## Achnowledgements
* Who helped make theses slides
* We wish to acknowledge this land on which the University of Toronto operates. For thousands of years it has been the traditional land of the Huron-Wendat, the Seneca, and most recently, the Mississaugas of the Credit River. Today, this meeting place is still the home to many Indigenous people from across Turtle Island and we are grateful to have the opportunity to work on this land.
### Contributions 
* `bash-git-github` welcomes issues, enhancement requests, and other contributions. To submit an issue, use the [GitHub
issues](https://github.com/anjalisilva/bash-git-github/issues).

## Additional Resources

"You are never taught how to build quality software" via Hacker News https://news.ycombinator.com/item?id=38570261 
