# Unique-Exams

Unique-Exams is a simple program to create randomized exams so each student receives a unique set of questions.

## Why?

When students have a good idea of what will be included in an upcoming exam, they will study towards the particular type of questions that will feature. This has significant value for educators due to the backwash effect - you can focus students' study time without the need of homework by this method of flagging the kind of questions you will be asking them.

However, to ensure students aren't simply memorizing answers prepared by other students, we still need a degree of exam security and randomness. This program provide that by randomizing the selection of questions for each student's exam, while keeping the overall question pool and topics consistent.

An educator prepares a template paper (or multiple template papers for situations where an examiner and student each receive their own copy - like an oral spoken assessment) following a particular format.

This program takes those templates, analyses the content, and generates however many unique exam papers are required by the educator.

Due to the randomness involved, templates can be reused in subsequent semesters without risk of students memorizing answers from past exams. In fact, students acquiring past exams from former students is encouraged as it helps motivate students to study a wider range of topics.

Please read TEMPLATE_DESIGN.md for details on the process of designing template exams.

## Getting started

### Installation

Run `poetry install`

### Usage

Have a look at the sample template files provided in the `input` folder to see the expected format. 

You can Follow the TEMPLATE_DESIGN.md guide to design your own templates. Remove the sample files and add your own template files to the `input` folder.

Modify config.py to reflect the text you want to use for placeholders for the Alternate questions.

Run `python unique_exams/main.py`

Generated exams will be placed in the `output` folder

## Running the tests

Currently there are no tests written.

# Contributing

Please read CONTRIBUTING.md for details on the process for submitting pull requests to us. We look forward to receiving your contributions!

# License

[MIT](https://choosealicense.com/licenses/mit/)

# Contributors
- Andrew de Jonge (https://github.com/talkingtoaj)