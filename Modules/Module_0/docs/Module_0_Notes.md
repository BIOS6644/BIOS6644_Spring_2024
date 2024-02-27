# Module 0 (≈2 weeks)  

## Computing Environment Setup 
### Necessary
 * [git](https://git-scm.com/): A free and open source tool for distributed version control
 * [github.com](www.github.com) A site to which your git will save your work so it can be easily shared
 * [Anaconda](https://www.anaconda.com/download) A convenient bundle of python, jupyter, and virtually every library you'll ever need for data wrangling (and lots of other things).

### My typical setup (Nothing here required--I just find it handy):
 * Computer: Redhat Linux (at work), MacAir (other places)
 * Editor: [VSCode](https://code.visualstudio.com/), [vim](https://www.vim.org/), or [neovim](https://neovim.io/)
 * Shell:  [Oh My Zsh](https://ohmyz.sh/)
 * Note taking: [Obsidian](https://obsidian.md)
---


1) Python is the industry standard language for wrangling data of all types.   If you don't know Python, it is strongly recommended that you learn it over this semester.  If you are likely to EVER wrangle data again, it's worth the time invested.

2) Jupyter Notebooks are a hand, interactive mechanism for running Python code, documenting your process, and making visualizations.  For this course, Jupyter Notebooks are the primary way of communicating results.

3) Git is the industry standard tool for distributed version control.  It's kind of painful to use, but that's because it enforces rigor for updates and changes.   We'll use git for submitting work.  The workflow you learn doing this will be a good basis for future collaboration.

---

- [ ] <--That kind of checkbox indicates a task you should accomplish

## Setup Github
- [ ] If you don't already have a [gituhub](www.github.com) account, make one.   
- [ ] Send your github username to the instructor via canvas message 
- [ ] If you're not familiar with Github, watch one of the tutorials such as [this one](https://www.youtube.com/watch?v=tRZGeaHPoaw).  If you're a git power user, watch [this one](https://www.youtube.com/watch?v=Uszj_k0DGsg).  It's pretty great.
- [ ] Clone the class git repo on to the computer you'll use for this course.
```bash
>  git clone git@github.com:pulsetracker/BIOS6644_Spring_2024.git

I the one above fails (Windows users?), try instead:
>  git clone https://github.com/BIOS6644/BIOS6644_Spring_2024.git 
```
```bash
> # This "clone" will make a new folder called BIOS6644_Spring_2024
> cd BIOS6644_Spring_2024   # "change directory" (cd) into it.
```

- [ ] Make a branch with your username, and check it out (activate it)
```bash
> git branch James_King
> git checkout James_King 
```
For the duration of this course, you should always work within this branch (You won't have a reason to alter *main*)

- [ ] Set the branch with your name as the github default for you
```bash
> git branch --set-upstream origin James_King
```

This makes it so that anytime you add anything, it goes into the branch with your name.  That prevents us from stepping on each other's files.

- [ ] Make a folder inside the Students directory.  This will be where you'll submit work.
```bash
> cd students
> mkdir JamesKing
```

## Saving & Sending Your Work

Assignments will often be submitted via github.    For practice, write a brief biography about yourself similar to mine (found in BIOS6644_Spring_2024/students/James_King/Module_0/James_bio.txt)
* Note: this file will be visible to everyone on the interwebs.  Don't include anything sensitive.  

- [ ] In your folder under students, make a folder called Module_0
```bash
> mkdir Module_0
```
- [ ] In put your biography in the Module_0 folder
```bash
> mv /path/to/Yourname_bio.txt BIOS6644_Spring_2024/students/James_King/Module_0
```
- [ ] Commit the change
```bash
> git add .
> git commit -m"Added a biography"
```
- [ ] Push the commit to github
```bash
> git push
```
## Pulling Updates
Course files might be distributed within github.  To get the latest of everything, run a git pull, then merge the main branch into yours.
```bash
> git pull origin main:main # pulls current main and merges main into your branch
> git push # Push your branch's updates (the stuff grabbed from main) into GitHub
```
- [ ] Do the pull above
