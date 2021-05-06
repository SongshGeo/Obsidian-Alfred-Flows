# An Alfred-WorkFlow for obsidian managing

## Introduction

I prefer to use Alfred to customise my own workflow than to install a bunch of plug-ins bundled with the software. This allows for light coupling between my tools and software, which creates more possibilities and reduces dependency on one tool or another. This workflow is made by [Alfred-workflow in python](https://github.com/deanishe/alfred-workflow). 

### **What is an Obsidian-Knowledge-Repository? **

[Obsidian is a powerful knowledge base that works on top of a local folder of plain text Markdown files.](https://obsidian.md/) If you are building an Obsidian-Knowledge-Repository (OKR) base based on local documents only, then it is a free software. It helps you to create links between electronic notes (if they are all stored in Markdown format) and shows them to you visually through beautiful visualisations. With this visual network you can easily keep track of the development of your body of knowledge.

If you have not had accessed to Obsidian before, I recommend that you use [my system](https://github.com/SongshGeo/My-Knowledge-Rep) for building your OKRs to better use this WorkFlow tool, here is a demo example: 

<img src="https://gitee.com/SongshGeo/PicGo_picbed/raw/master/img/20210506163138.png" alt="A demo OKR" style="zoom: 33%;" />



### **What is an Alfred WorkFlow?**

[Alfred](https://www.alfredapp.com/) is on the top of productivity tools in macOS. By using Alfred, you can access any amazing repeatable and trivial task with one hotkey easily. With Alfred's [WorkFlow](https://www.alfredapp.com/workflows/), you can extend Alfred and get things done in your own way. Replace repetitive tasks with workflows, and boost your productivity.

## Installation

- Download the newest released version `Manage Obsidian.alfredworkflow`.
- Drag it into your Alfred WorkFlow to install.
- Then, enjoy it!

## How to use

### Create topic tag one-hotkey

- Assign the path of your Obsidian-Knowledge-Repository  (OKR).
- Using keyword **Topic** + *Keyword* to get an overall statistic of in each folder of the OKR by the *Keyword*. 
- Press *Enter* to assign the *Keyword* directly as a "topic tag", if a tag-saving path specified. 

### Export your experts to Anki Flashcard

[Anki](https://apps.ankiweb.net/) is a program which makes remembering things easy. Because it's a lot more efficient than traditional study methods, you can either greatly decrease your time spent studying, or greatly increase the amount you learn.

```
# This is a demo, showing how an expert information organized.
# The two experts are all in a certain note, whose name is also the name of the book.

template = """
Experts (2021-05-05): 
> Text: Of course there is a difference between melodrama and mainstream, don't be afraid of mainstream language. This era has become so new that you are already in the mainstream when you are talking about what is appropriate for the margins. That includes alternative, which has now become mainstream.
> Source: *p77, Li*
> Notes: Some sink with the tide, others chase the tip, while the visionary predicts the direction the tide will go.

Experts (2021-05-05): 
> Text: Imagination is as important in film as it is in literature. But films often have to concretize the imagination, a restricted imagination. Literature, however hard you try to depict it, cannot restore the object of depiction to a physical object, right, so that the reader has a space for imagination, room for imagination.
> Source: *p167 Wanma*
> Notes: I love this book.
"""
```

- Assign the path of your Obsidian-Knowledge-Repository  (OKR), and an output path of auto-export anki file.
- Using keyword *mob* (managing obsidian) to activate existed managing functions. 
- After input *anki* as query following *mob*, it will send back all eligible experts in each note. 
- Press *Enter* to export all eligible experts into a formatted file which can be easily import to your anki. 

## Change Log:

2021-05-02, updated: An initial version: Get statistic by a keyword and transfer it as a topic tag now. 
2021-05-06, updated: Can extract experts to anki flashcard now.

## Future plans:

- Clean trash files in the OKR.
- Extract name, date, url information with one hotkey.
- Replace terms by keywords. 
- Connect to TickTick to-do API and generate tasks.