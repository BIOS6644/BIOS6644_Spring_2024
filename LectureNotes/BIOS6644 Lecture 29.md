#BIOS6644
#LectureNotes

1 May  2024

# Presentations begin Next Week!
![[Pasted image 20240429171617.png]]

# Projects Due in Finals Week
- May 6, 8, 13 & 15 will be you presenting a brief synopsis of your project
- Deliverables (notebooks) are due to Canvas at the end of 17 May (end of semester)
- [Assignment and Rubric](https://ucdenver.instructure.com/courses/533986/assignments/1717710)
- [Peer Review Assignment](https://ucdenver.instructure.com/courses/533986/assignments/1718103)
	- You've each been assigned 3 peer reviews. (Details in Assignment on Canvas)
## Presentation Time switches
If you need to change presentation time, please arrange a swap with one of your classmates and send me an email (via canvas) with details.
- Switch:  Lola will be presenting on May 6th, second slot and Irena will be presenting on May 15th, first slot. 
- **Please give feedback to the same *person*, despite the change.** 

# MedRecs Grades
- If you don't have a grade in the MedRecs assignment, please submit your notebook via canvas--I've reopened it. 
- This means you:
	- Joanna G. (Again)
	- Alina S.      (Again)
	- Asma T.     (Again)
	- Sean V.      (Again)


# Project Proposals are graded
-  **Can you all please put what you've sent me into the Assignments section of the canvas page?**   
- About ~~5~~ 2 of you have grades but have not resubmitted via Canvas--please do.
	- This means you:
		- Jonathan M.  (New entry to list--missed it last time)
		- Alina S.  (Again)


#  Assignments
## EEG
- Extended until Monday, 6 May.  If you submitted but think you want to do more, feel free to submit another and I'll grade that one.
- [EEG wrangling](https://ucdenver.instructure.com/courses/533986/assignments/1715961)  ~~Due 30 April (This Wednesday)
- If you're struggling with getting the data unzipped correctly, use the [data file which I added to the github archive](https://github.com/BIOS6644/BIOS6644_Spring_2024/blob/main/Modules/Module_2/Data/co2a0000364.rd.000)
## Regex
- [Canvas Assignment](https://ucdenver.instructure.com/courses/533986/assignments/1718544)
- Complete **YouDo** in [regex notebook](https://github.com/BIOS6644/BIOS6644_Spring_2024/blob/main/Modules/Module_2/JamesKing_BIOS6644_RegEx_Transcription_Search.ipynb)
- Due 15 May (Flex around your presentation schedule)

# For the rest of class
1. Detailed review of presentation & project expectations
	- [Assignment and Rubric](https://ucdenver.instructure.com/courses/533986/assignments/1717710)
	- [Peer Review Assignment](https://ucdenver.instructure.com/courses/533986/assignments/1718103)

2. EEG plotting re-visit
```python

# dfs:  A list of dataframes.   Each dataframe contains all channel
#       recordings for a single trial (i.e. a single patient)
# dfs[3]:  the third trial
# dfs[24]:  The 24th trial
# ...
#
# Within a df, the columns are recordings from a single channel
#
# dfs[3].C1 is the recording of channel C1 from trial #3
# dfs[73].X is the recording of channel X from trial #73

all_channel_names = dfs[0].columns

#outer loop:  All channel names
for thischannel in all_channel_names:
	plt.figure(). # make a new figure for each channel

	#inner loop: All trials
	for cc in list(dfs.values()):
		Pxx, f =plt.psd(cc[thischannel], Fs=256, NFFT=2**10, alpha=.2)
		plt.title(f'All trials, Channel {thischannel}')

```
