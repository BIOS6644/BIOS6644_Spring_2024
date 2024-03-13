#BIOS6644
#LectureNotes

4 March 2024

# Welcome Back
- Sugar Metabolomics Graded
	* What is an "output" of .8215?  How did you get this?
	* Be careful commenting out the assert statements.   If they're failing, you may be doing something wrong.
	* In "real life", is the random forest model actually "good"?
		* Accuracy
		* Precision/Recall/Sensitivty/Specificity/TPR/TNR/P(D)/P(FA)[...](https://en.wikipedia.org/wiki/Confusion_matrix)
		* [Mathew's Correlation](https://en.wikipedia.org/wiki/Phi_coefficient)
		* [Blog Post](https://medium.com/analytics-vidhya/evaluating-a-random-forest-model-9d165595ad56) on evaluating a random forest model
		* "describing the results as a markdown" --> set the Jupyter cell to be "Markdown"

# File Submission Convention
I have been inconsistent in what I ask for--apologies.   From here out, please put all submissions into 
```bash

BIOS6644_Spring_2024/students/YourName/Module_X
```
and please organize your files to match this structure:

```zsh
└── students
    └── JamesKing
        ├── Module_0
        │   ├── M0_BIOS6644_Read_CSV_Direct_James_King.ipynb
        │   ├── M0_Biography_James_King.txt
        │   └── M0_Python_Refresher-James_King.ipynb
        └── Module_1
            ├── M1_BIOS6644_CSV_ParseSlice_James_King.ipynb
            └── M1_BIOS6644_CSV_Sugar_Metabolomics_James_King.ipynb
```


# Updates
- Lots of updates!  Do a pull 
```bash
# Make sure you're in your branch
git checkout Your_Name
git add .
git commit -m"Stash current work before main:main pull"
git pull origin main:main
git push
```

---
# New Assignment
Complete [ MedRecs](https://github.com/BIOS6644/BIOS6644_Spring_2024/blob/main/Modules/Module_1/assignments/M1_BIOS6644_MedRecs_YourName.ipynb) .  My solution is under "[docs](https://github.com/BIOS6644/BIOS6644_Spring_2024/blob/main/Modules/Module_1/docs/M1_BIOS6644_MedRecs_JamesKing.ipynb))", but try to do it on your own.
Due: 11 March.

---
# Remainder of time
- My solution to Sugar Metabolomics.
- My MedRecs

---

# Reference:
-  [syllabus](https://ucdenver.instructure.com/courses/533986/assignments/syllabus)
- [Sugar Metabolomics](https://github.com/BIOS6644/BIOS6644_Spring_2024/blob/main/Modules/Module_1/notebooks/BIOS6644_CSV_Sugar_Metabolomics_YourName.ipynb) notebook
-
