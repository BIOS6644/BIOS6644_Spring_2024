# Setting up authenticated GitHub Access over HTTPS protocol

- [ ] Open the following page and select your operating system:
[link](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git)
    - This will have you install a github-specific command line tool called gh
- [ ] From your normal terminal, do
```bash
gh auth login
```
  This will start an interactive script.  I found that the options were sometimes not visible,
  and so had to up/down arrow a few times to see them.  Select the following options:
```
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code:...
```
Copy the code and and paste it into the webpage that pops up and follow the rest of the prompts.

## Re-initialize your local repository.
This is not required, but recommended to make sure we're all on the same setup.
```bash
mkdir BIOS6644_GitHub
cd BIOS6644_GitHub
git clone https://github.com/BIOS6644/BIOS6644_Spring_2024.git
```
This will download all the stuff that's there.  Now setup your branch:

```bash
cd BIOS_6644_Spring_2024
git branch Your_Name
git checkout Your_Name
git push git push --set-upstream origin Your_Name # not an typo!  use git push!
```
Now you'll be on your branch locally and github will be aware of your branch.  Now make
a folder for yourself under students.
```bash
cd students
mkdir YourName
cd YourName
mkdir Module_0
touch empty.txt # make an empty file to force git to build the directory tree
```
Now you have a folder structure for submitting your work.

Now we can push this (empty) structure to GitHub
```bash
git add .
git commit -m"Initial Commit"

git pull origin main:main  # just in case something has changed

git push

```
Locally, you'll have the folder: 

BIOS6644_GitHub/BIOS6644_Spring_2024/students/Your_Name/Module_0

This is the folder to put Module_0 submissions.
  1. The biography, YourName_Bio.txt
  2. Your work-through of the Python Refresher.  Make sure your name is in the filename: M0_Python_Refresher_Your_name.ipynb

There are really 2 ways to submit the files.   
  1) put the files on your repo (in the folder mentioned above), then push to github
```bash
cp /path/to/your/bio/YourName_Bio.txt BIOS6644_GitHub/BIOS6644_Spring_2024/students/Your_Name/Module_0
cp /path/to/your/notebook/M0_Python_Refresher_Your_name.ipynb BIOS6644_GitHub/BIOS6644_Spring_2024/students/Your_Name/Module_0
git add .
git commit -m"Module 0 submissions"
git push
```
  3) Upload the files via github's web page
    - Dropdown menu--select your branch
    - Navigate to the drop folder
    - Click Add File --> Upload Files
     - Drag & Drop your submissions there
     - Click the commit button.
    Now your files will be on github, but not your local repo.  You can git pull to get them locally.
```bash
git pull
```
    
    
