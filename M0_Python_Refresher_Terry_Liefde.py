#!/usr/bin/env python
# coding: utf-8

# In[2]:


##########################################################################################
#                                                                                        #
#  888888b.  8888888 .d88888b.   .d8888b.     .d8888b.   .d8888b.      d8888      d8888  #
#  888  "88b   888  d88P" "Y88b d88P  Y88b   d88P  Y88b d88P  Y88b    d8P888     d8P888  #
#  888  .88P   888  888     888 Y88b.        888        888          d8P 888    d8P 888  #
#  8888888K.   888  888     888  "Y888b.     888d888b.  888d888b.   d8P  888   d8P  888  #
#  888  "Y88b  888  888     888     "Y88b.   888P "Y88b 888P "Y88b d88   888  d88   888  #
#  888    888  888  888     888       "888   888    888 888    888 8888888888 8888888888 #
#  888   d88P  888  Y88b. .d88P Y88b  d88P   Y88b  d88P Y88b  d88P       888        888  #
#  8888888P" 8888888 "Y88888P"   "Y8888P"     "Y8888P"   "Y8888P"        888        888  #
#                                                                                        # 
##########################################################################################
#
# Python Refresher
#
##########################################################################################


# In[3]:


##################################################################################################################
#
# YouDo:
#    1) Make a copy of this notebook with your name as a suffix:  
#           M0_Python_Refresher_FirstLast
#    2) Put it in your folder undr students
#    3) Ensure you are in your branch in git 
#    2) Do all work in this new notebook.
#
##################################################################################################################


# In[6]:


# Python Refresher
# Basic Data Structures
# The most basic "thing" in python is called an "object". Basically anything you imagine as "data" would be represented by some number of Python objects. Python provides several "built-in object types", like integers and strings, which are useful for storing and manipulating various data.

# The following table lists the fundamental Python object types.

Type Abbreviation	Type Full Name	Notes
str	string	Text
int	integer	Decimal-free numbers
float	Floating point Number	A decimal number
bool	Boolean	Can be either True or False
list	List	An indexed, ordered, collection of other types
dict	Dictionary	A 1-to-1 lookup table
set	Set	As in set-theory. A collection of unique objects
The following cells show how to create objects of different types.


# In[9]:


Strings
[2]
# Strings are surrounded by quotes

s1 = 'This is a string'
s2 = "Double-quotes and single-quotes are equivalent"
s3 = '''This kind can span 
        many lines'''

print(s1)
print(s2) 
print(s3)


# This is a string
# Double-quotes and single-quotes are equivalent
# This kind can span many lines

[3]
# Adding strings contatenates them together

L1 = 'Luke. '
L2 = 'I am your father.'
print(L1+L2)

LAdd = L1 + L2

print(LAdd)
Luke. I am your father.
Luke. I am your father.

[18]
B0 = '99'
B1 = '98'
B2 = ' bottles of beer'
B3 = ' on the wall'
B4 = 'you take one down, pass it around'

print(B0+B2+B3)
print('\t'+B0+B2)           # '\t' is a tab character
print(B4+'\n'+'\t'+B0+B2+B3)# '\n' is a newline character
99 bottles of beer on the wall
	99 bottles of beer you take one down, pass it around
	99 bottles of beer on the wall

##################################################################################################################
# YouDo
# In a similar pattern to the cell above, make a set of print statements 
# which makes the next verse of that song.
# 
# In case you didn't grow up in North America:
#   https://en.wikipedia.org/wiki/99_Bottles_of_Beer
#
##################################################################################################################
#######################################  BEGIN STUDENT CODE  #####################################################



#######################################   END STUDENT CODE   #####################################################



# In[10]:


B0 = '99'
B1 = '98'
B2 = ' bottles of beer'
B3 = ' on the wall'
B4 = 'you take one down, pass it around'
print(B1+B2+B3)
print('\t'+B1+B2) 
print(B4+'\n'+'\t'+B1+B2+B3)


# In[12]:


Integers
[22]
A = 3        # type is inferred by lack of decimal point
B = int(3)   # explicitly typed
C = int('3') # Casting a numeral/string 3, to the integer value of 3

print(A, B, C)
3 3 3

[8]
##################################################################################################################
#
# YouDo:
#    1) In the code below, fix the 3rd term so it computes and prints the integer 12 as the answer
#
##################################################################################################################
#######################################  BEGIN STUDENT CODE  #####################################################

two = 2
three = 3

answer = two * three + '2' * three
print(answer)


#######################################   END STUDENT CODE   #####################################################

12


# In[14]:


A = 3        # type is inferred by lack of decimal point
B = int(3)   # explicitly typed
C = int('3') # Casting a numeral/string 3, to the integer value of 3
two = 2
three = 3

answer = (two * three ) * int(two)
print(answer)


# In[15]:


Floats
[41]
# The type() function will tell you what type a data object is

F0 = 3           # Not a float!
print('F0: ', F0, type(F0))

F1 = float(3)    # Cast to a float!
print('F1: ', F1, type(F1))

F2 = 3 + 0.0     # Added to a float
print('F2: ', F2, type(F2))

F3 = 3.         # A dot on the end makes it a float
print('F3: ', F3, type(F3))

F4 = 3.000      # So does adding decimapl places
print('F4: ', F4, type(F4))

F5 = 1e6-999997 # Scientific notation is a float as well
print('F5: ', F5, type(F5))

F6 = float('inf') # infinity is a float
print('F6: ', F6, type(F6))
#print(F6 + 1)

F7 = float('NaN') # not a number (nan) is a float, too
print('F7: ', F7, type(F7))
F0:  3 <class 'int'>
F1:  3.0 <class 'float'>
F2:  3.0 <class 'float'>
F3:  3.0 <class 'float'>
F4:  3.0 <class 'float'>
F5:  3.0 <class 'float'>
F6:  inf <class 'float'>
F7:  nan <class 'float'>

[11]
##################################################################################################################
#
# YouDo:
#    1) Fix the code below so it computes and prints 9.0 (a float) as the answer
#       Hint:  I can do it by adding a single character
#
##################################################################################################################
#######################################  BEGIN STUDENT CODE  #####################################################

two = 2
three = 3

answer = two * three + float(three)
print('My answer is: ', answer, ' of type ', type(answer))




#######################################   END STUDENT CODE   #####################################################

My answer is:  9  of type  <class 'int'>


# In[17]:



two = 2
three = 3
answer = two * three + 3.0
print('My answer is: ', answer, ' of type ', type(answer))


# In[ ]:


Lists
[20]
darf = [True,2,3,4,'five'] # Lists hold stuff

print(darf[2])  # brackets read a value out (counting starts at zero)

# Use .append(newthing) to add a newthing to the list
darf.append("I am new thing")

print(darf)

3
[True, 2, 3, 4, 'five', 'I am new thing']

[21]
# You can get a "slice" (subset) of list items with a colon:

print(darf[3:5]) # Get objects 3 and 4 (doens't include the last one)

[4, 'five']

[32]
##################################################################################################################
#
# YouDo:
#    1) print the slice of worklist which contains all the items which begin with 3 and no other itemts
#       [30, 32, ..., 38]
#
##################################################################################################################

worklist = list(range(0,50,2))
print(f'Original worklist: {worklist}')

#######################################  BEGIN STUDENT CODE  #####################################################

myslice = worklist[0:4]

print(f'Thirties Subset: {myslice}')



#######################################   END STUDENT CODE   #####################################################

Original worklist: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
Thirties Subset: [0, 2, 4, 6]


# In[19]:


nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
30slice = nums[20:25]
print(30slice)


# In[ ]:


Dictionaries
[37]
# Dictionaries are a key-based map of objects.   

dex = dict()
dex['AllMonths']=['January', 'February', 'March']
dex['Jan']='January'
dex['jan']='January'
dex['JAN']='January'
dex['jan.']='January'
dex['Feb']='February'
dex['Mar']='March'
dex
{'AllMonths': ['January', 'February', 'March'],
 'Jan': 'January',
 'jan': 'January',
 'JAN': 'January',
 'jan.': 'January',
 'Feb': 'February',
 'Mar': 'March'}
[44]
# You can use them to make a lookup table

print(f'I was not born in Jan')
print(f"I was not born in {dex['Jan']}")
print(f"I was not born in {dex['AllMonths']}")
I was not born in Jan
I was not born in January
I was not born in ['January', 'February', 'March']

##################################################################################################################
#
# YouDo:
#    1) print the slice of worklist which contains all the items which begin with 3 and no other itemts
#       [30, 32, ..., 38]
#
##################################################################################################################

worklist = list(range(0,50,2))
print(f'Original worklist: {worklist}')

#######################################  BEGIN STUDENT CODE  #####################################################

myslice = worklist[0:4]

print('\nThirties Subset: {myslice}')



#######################################   END STUDENT CODE   #####################################################

## Very Useful Libraries

# Numerical Python (numpy)
# Matplotlib (good for making visualizations)
# plotly (another good plotting library) 
# Regular Expressions (re)
# Scientific Python (scipy)

#### Statsmodels
#### Statistics
#### Signals (for some kinds of time-series processing)
### Sci-Kit Learn (sklearn)


# In[ ]:


Installing useful libraries
Python has a very rich ecosystem of libraries for more or less anything you can imagine. The following libraries are the "core" for data science type work.

Very Useful Libraries
Numerical Python (numpy)
Matplotlib (good for making visualizations)
plotly (another good plotting library)
Regular Expressions (re)
Scientific Python (scipy)
Statsmodels
Statistics
Sci-Kit Learn (sklearn)
Depending on how you are running python or notebooks, there are various ways to install the libraries.

For Anaconda users
These generally come packaged with Anaconda To be sure, use the Anaconda package manager and/or do the following from your anaconda command line:
conda install

If you're not using Ananconda, pip is then generally used method:

pip3 install

It is possible to run command line comands from within a notebook. Just prefix a "!" to the command, as in the next line


# In[ ]:



[26]
get_ipython().system('pip3 install scipy numpy pandas matplotlib scikit-learn Statsmodels Statistics plotly pooch')
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: scipy in /Users/james/Library/Python/3.9/lib/python/site-packages (1.12.0)
Requirement already satisfied: numpy in /Users/james/Library/Python/3.9/lib/python/site-packages (1.26.2)
Requirement already satisfied: pandas in /Users/james/Library/Python/3.9/lib/python/site-packages (2.1.4)
Requirement already satisfied: matplotlib in /Users/james/Library/Python/3.9/lib/python/site-packages (3.8.2)
Requirement already satisfied: scikit-learn in /Users/james/Library/Python/3.9/lib/python/site-packages (1.4.0)
Requirement already satisfied: Statsmodels in /Users/james/Library/Python/3.9/lib/python/site-packages (0.14.1)
Requirement already satisfied: Statistics in /Users/james/Library/Python/3.9/lib/python/site-packages (1.0.3.5)
Requirement already satisfied: plotly in /Users/james/Library/Python/3.9/lib/python/site-packages (5.18.0)
Collecting pooch
  Downloading pooch-1.8.0-py3-none-any.whl.metadata (9.9 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/james/Library/Python/3.9/lib/python/site-packages (from pandas) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /Users/james/Library/Python/3.9/lib/python/site-packages (from pandas) (2023.3.post1)
Requirement already satisfied: tzdata>=2022.1 in /Users/james/Library/Python/3.9/lib/python/site-packages (from pandas) (2023.4)
Requirement already satisfied: contourpy>=1.0.1 in /Users/james/Library/Python/3.9/lib/python/site-packages (from matplotlib) (1.2.0)
Requirement already satisfied: cycler>=0.10 in /Users/james/Library/Python/3.9/lib/python/site-packages (from matplotlib) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from matplotlib) (4.47.2)
Requirement already satisfied: kiwisolver>=1.3.1 in /Users/james/Library/Python/3.9/lib/python/site-packages (from matplotlib) (1.4.5)
Requirement already satisfied: packaging>=20.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from matplotlib) (23.2)
Requirement already satisfied: pillow>=8 in /Users/james/Library/Python/3.9/lib/python/site-packages (from matplotlib) (10.2.0)
Requirement already satisfied: pyparsing>=2.3.1 in /Users/james/Library/Python/3.9/lib/python/site-packages (from matplotlib) (3.1.1)
Requirement already satisfied: importlib-resources>=3.2.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from matplotlib) (6.1.1)
Requirement already satisfied: joblib>=1.2.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from scikit-learn) (1.3.2)
Requirement already satisfied: threadpoolctl>=2.0.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from scikit-learn) (3.2.0)
Requirement already satisfied: patsy>=0.5.4 in /Users/james/Library/Python/3.9/lib/python/site-packages (from Statsmodels) (0.5.6)
Requirement already satisfied: docutils>=0.3 in /Users/james/Library/Python/3.9/lib/python/site-packages (from Statistics) (0.20.1)
Requirement already satisfied: tenacity>=6.2.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from plotly) (8.2.3)
Requirement already satisfied: platformdirs>=2.5.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from pooch) (4.1.0)
Requirement already satisfied: requests>=2.19.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from pooch) (2.31.0)
Requirement already satisfied: zipp>=3.1.0 in /Users/james/Library/Python/3.9/lib/python/site-packages (from importlib-resources>=3.2.0->matplotlib) (3.17.0)
Requirement already satisfied: six in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from patsy>=0.5.4->Statsmodels) (1.15.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/james/Library/Python/3.9/lib/python/site-packages (from requests>=2.19.0->pooch) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in /Users/james/Library/Python/3.9/lib/python/site-packages (from requests>=2.19.0->pooch) (3.6)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/james/Library/Python/3.9/lib/python/site-packages (from requests>=2.19.0->pooch) (2.1.0)
Requirement already satisfied: certifi>=2017.4.17 in /Users/james/Library/Python/3.9/lib/python/site-packages (from requests>=2.19.0->pooch) (2023.11.17)
Downloading pooch-1.8.0-py3-none-any.whl (62 kB)
2K   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.7/62.7 kB 256.6 kB/s eta 0:00:00a 0:00:01
get_ipython().run_line_magic('pinfo', '25hInstalling')
Successfully installed pooch-1.8.0

[ ] Ensure that each of the "useful libraries" are installed via your preferred method
[ ] Verify this by doing import statements as below


# In[ ]:


import numpy as np
import scipy
import pandas as pd
import pylab as plt  # matplotlib import
import plotly
[20]
# Numpy is great for numerical stuff, matrix algebra, etc.

ar1 = np.array([1,2,3,4,5])
ar2 = np.array([9,9,9,9,9])

print("Some numpy arrays:")
print(ar1, ar2)

print(f'\nSome vector math: 3 * ar1 + ar2:')
print(3 * ar1 + ar2)
Some numpy arrays:
[1 2 3 4 5] [9 9 9 9 9]

Some vector math: 3 * ar1 + ar2:
[12 15 18 21 24]

[4]
# Scipy has lots of useful sublibraries
from scipy.datasets import face, electrocardiogram

face = face()
ecg = electrocardiogram()
Downloading file 'face.dat' from 'https://raw.githubusercontent.com/scipy/dataset-face/main/face.dat' to '/Users/james/Library/Caches/scipy-data'.

[5]
print(face)
[[[121 112 131]
  [138 129 148]
  [153 144 165]
  ...
  [119 126  74]
  [131 136  82]
  [139 144  90]]

 [[ 89  82 100]
  [110 103 121]
  [130 122 143]
  ...
  [118 125  71]
  [134 141  87]
  [146 153  99]]

 [[ 73  66  84]
  [ 94  87 105]
  [115 108 126]
  ...
  [117 126  71]
  [133 142  87]
  [144 153  98]]

 ...

 [[ 87 106  76]
  [ 94 110  81]
  [107 124  92]
  ...
  [120 158  97]
  [119 157  96]
  [119 158  95]]

 [[ 85 101  72]
  [ 95 111  82]
  [112 127  96]
  ...
  [121 157  96]
  [120 156  94]
  [120 156  94]]

 [[ 85 101  74]
  [ 97 113  84]
  [111 126  97]
  ...
  [120 156  95]
  [119 155  93]
  [118 154  92]]]


# In[ ]:


6]
print(ecg)
[-0.245 -0.215 -0.185 ... -0.405 -0.395 -0.385]

[7]
# Matplot lib is useful for looking at these:

import pylab as plt
plt.imshow(face)


# In[ ]:


<matplotlib.image.AxesImage at 0x11f6718b0>


# In[ ]:


plt.plot(ecg)


# In[ ]:


[<matplotlib.lines.Line2D at 0x11f7fbeb0>]


# In[ ]:


# Sklearn has lots of machine learning and preprocessing stuff
# and some data sets
from sklearn import datasets
irr = datasets.load_iris()
irr


# In[ ]:


{'data': array([[5.1, 3.5, 1.4, 0.2],
        [4.9, 3. , 1.4, 0.2],
        [4.7, 3.2, 1.3, 0.2],
        [4.6, 3.1, 1.5, 0.2],
        [5. , 3.6, 1.4, 0.2],
        [5.4, 3.9, 1.7, 0.4],
        [4.6, 3.4, 1.4, 0.3],
        [5. , 3.4, 1.5, 0.2],
        [4.4, 2.9, 1.4, 0.2],
        [4.9, 3.1, 1.5, 0.1],
        [5.4, 3.7, 1.5, 0.2],
        [4.8, 3.4, 1.6, 0.2],
        [4.8, 3. , 1.4, 0.1],
        [4.3, 3. , 1.1, 0.1],
        [5.8, 4. , 1.2, 0.2],
        [5.7, 4.4, 1.5, 0.4],
        [5.4, 3.9, 1.3, 0.4],
        [5.1, 3.5, 1.4, 0.3],
        [5.7, 3.8, 1.7, 0.3],
        [5.1, 3.8, 1.5, 0.3],
        [5.4, 3.4, 1.7, 0.2],
        [5.1, 3.7, 1.5, 0.4],
        [4.6, 3.6, 1. , 0.2],
        [5.1, 3.3, 1.7, 0.5],
        [4.8, 3.4, 1.9, 0.2],
        [5. , 3. , 1.6, 0.2],
        [5. , 3.4, 1.6, 0.4],
        [5.2, 3.5, 1.5, 0.2],
        [5.2, 3.4, 1.4, 0.2],
        [4.7, 3.2, 1.6, 0.2],
        [4.8, 3.1, 1.6, 0.2],
        [5.4, 3.4, 1.5, 0.4],
        [5.2, 4.1, 1.5, 0.1],
        [5.5, 4.2, 1.4, 0.2],
        [4.9, 3.1, 1.5, 0.2],
        [5. , 3.2, 1.2, 0.2],
        [5.5, 3.5, 1.3, 0.2],
        [4.9, 3.6, 1.4, 0.1],
        [4.4, 3. , 1.3, 0.2],
        [5.1, 3.4, 1.5, 0.2],
        [5. , 3.5, 1.3, 0.3],
        [4.5, 2.3, 1.3, 0.3],
        [4.4, 3.2, 1.3, 0.2],
        [5. , 3.5, 1.6, 0.6],
        [5.1, 3.8, 1.9, 0.4],
        [4.8, 3. , 1.4, 0.3],
        [5.1, 3.8, 1.6, 0.2],
        [4.6, 3.2, 1.4, 0.2],
        [5.3, 3.7, 1.5, 0.2],
        [5. , 3.3, 1.4, 0.2],
        [7. , 3.2, 4.7, 1.4],
        [6.4, 3.2, 4.5, 1.5],
        [6.9, 3.1, 4.9, 1.5],
        [5.5, 2.3, 4. , 1.3],
        [6.5, 2.8, 4.6, 1.5],
        [5.7, 2.8, 4.5, 1.3],
        [6.3, 3.3, 4.7, 1.6],
        [4.9, 2.4, 3.3, 1. ],
        [6.6, 2.9, 4.6, 1.3],
        [5.2, 2.7, 3.9, 1.4],
        [5. , 2. , 3.5, 1. ],
        [5.9, 3. , 4.2, 1.5],
        [6. , 2.2, 4. , 1. ],
        [6.1, 2.9, 4.7, 1.4],
        [5.6, 2.9, 3.6, 1.3],
        [6.7, 3.1, 4.4, 1.4],
        [5.6, 3. , 4.5, 1.5],
        [5.8, 2.7, 4.1, 1. ],
        [6.2, 2.2, 4.5, 1.5],
        [5.6, 2.5, 3.9, 1.1],
        [5.9, 3.2, 4.8, 1.8],
        [6.1, 2.8, 4. , 1.3],
        [6.3, 2.5, 4.9, 1.5],
        [6.1, 2.8, 4.7, 1.2],
        [6.4, 2.9, 4.3, 1.3],
        [6.6, 3. , 4.4, 1.4],
        [6.8, 2.8, 4.8, 1.4],
        [6.7, 3. , 5. , 1.7],
        [6. , 2.9, 4.5, 1.5],
        [5.7, 2.6, 3.5, 1. ],
        [5.5, 2.4, 3.8, 1.1],
        [5.5, 2.4, 3.7, 1. ],
        [5.8, 2.7, 3.9, 1.2],
        [6. , 2.7, 5.1, 1.6],
        [5.4, 3. , 4.5, 1.5],
        [6. , 3.4, 4.5, 1.6],
        [6.7, 3.1, 4.7, 1.5],
        [6.3, 2.3, 4.4, 1.3],
        [5.6, 3. , 4.1, 1.3],
        [5.5, 2.5, 4. , 1.3],
        [5.5, 2.6, 4.4, 1.2],
        [6.1, 3. , 4.6, 1.4],
        [5.8, 2.6, 4. , 1.2],
        [5. , 2.3, 3.3, 1. ],
        [5.6, 2.7, 4.2, 1.3],
        [5.7, 3. , 4.2, 1.2],
        [5.7, 2.9, 4.2, 1.3],
        [6.2, 2.9, 4.3, 1.3],
        [5.1, 2.5, 3. , 1.1],
        [5.7, 2.8, 4.1, 1.3],
        [6.3, 3.3, 6. , 2.5],
        [5.8, 2.7, 5.1, 1.9],
        [7.1, 3. , 5.9, 2.1],
        [6.3, 2.9, 5.6, 1.8],
        [6.5, 3. , 5.8, 2.2],
        [7.6, 3. , 6.6, 2.1],
        [4.9, 2.5, 4.5, 1.7],
        [7.3, 2.9, 6.3, 1.8],
        [6.7, 2.5, 5.8, 1.8],
        [7.2, 3.6, 6.1, 2.5],
        [6.5, 3.2, 5.1, 2. ],
        [6.4, 2.7, 5.3, 1.9],
        [6.8, 3. , 5.5, 2.1],
        [5.7, 2.5, 5. , 2. ],
        [5.8, 2.8, 5.1, 2.4],
        [6.4, 3.2, 5.3, 2.3],
        [6.5, 3. , 5.5, 1.8],
        [7.7, 3.8, 6.7, 2.2],
        [7.7, 2.6, 6.9, 2.3],
        [6. , 2.2, 5. , 1.5],
        [6.9, 3.2, 5.7, 2.3],
        [5.6, 2.8, 4.9, 2. ],
        [7.7, 2.8, 6.7, 2. ],
        [6.3, 2.7, 4.9, 1.8],
        [6.7, 3.3, 5.7, 2.1],
        [7.2, 3.2, 6. , 1.8],
        [6.2, 2.8, 4.8, 1.8],
        [6.1, 3. , 4.9, 1.8],
        [6.4, 2.8, 5.6, 2.1],
        [7.2, 3. , 5.8, 1.6],
        [7.4, 2.8, 6.1, 1.9],
        [7.9, 3.8, 6.4, 2. ],
        [6.4, 2.8, 5.6, 2.2],
        [6.3, 2.8, 5.1, 1.5],
        [6.1, 2.6, 5.6, 1.4],
        [7.7, 3. , 6.1, 2.3],
        [6.3, 3.4, 5.6, 2.4],
        [6.4, 3.1, 5.5, 1.8],
        [6. , 3. , 4.8, 1.8],
        [6.9, 3.1, 5.4, 2.1],
        [6.7, 3.1, 5.6, 2.4],
        [6.9, 3.1, 5.1, 2.3],
        [5.8, 2.7, 5.1, 1.9],
        [6.8, 3.2, 5.9, 2.3],
        [6.7, 3.3, 5.7, 2.5],
        [6.7, 3. , 5.2, 2.3],
        [6.3, 2.5, 5. , 1.9],
        [6.5, 3. , 5.2, 2. ],
        [6.2, 3.4, 5.4, 2.3],
        [5.9, 3. , 5.1, 1.8]]),
 'target': array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
 'frame': None,
 'target_names': array(['setosa', 'versicolor', 'virginica'], dtype='<U10'),
 'DESCR': '.. _iris_dataset:\n\nIris plants dataset\n--------------------\n\n**Data Set Characteristics:**\n\n:Number of Instances: 150 (50 in each of three classes)\n:Number of Attributes: 4 numeric, predictive attributes and the class\n:Attribute Information:\n    - sepal length in cm\n    - sepal width in cm\n    - petal length in cm\n    - petal width in cm\n    - class:\n            - Iris-Setosa\n            - Iris-Versicolour\n            - Iris-Virginica\n\n:Summary Statistics:\n\n============== ==== ==== ======= ===== ====================\n                Min  Max   Mean    SD   Class Correlation\n============== ==== ==== ======= ===== ====================\nsepal length:   4.3  7.9   5.84   0.83    0.7826\nsepal width:    2.0  4.4   3.05   0.43   -0.4194\npetal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\npetal width:    0.1  2.5   1.20   0.76    0.9565  (high!)\n============== ==== ==== ======= ===== ====================\n\n:Missing Attribute Values: None\n:Class Distribution: 33.3% for each of 3 classes.\n:Creator: R.A. Fisher\n:Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\n:Date: July, 1988\n\nThe famous Iris database, first used by Sir R.A. Fisher. The dataset is taken\nfrom Fisher\'s paper. Note that it\'s the same as in R, but not as in the UCI\nMachine Learning Repository, which has two wrong data points.\n\nThis is perhaps the best known database to be found in the\npattern recognition literature.  Fisher\'s paper is a classic in the field and\nis referenced frequently to this day.  (See Duda & Hart, for example.)  The\ndata set contains 3 classes of 50 instances each, where each class refers to a\ntype of iris plant.  One class is linearly separable from the other 2; the\nlatter are NOT linearly separable from each other.\n\n|details-start|\n**References**\n|details-split|\n\n- Fisher, R.A. "The use of multiple measurements in taxonomic problems"\n  Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to\n  Mathematical Statistics" (John Wiley, NY, 1950).\n- Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.\n  (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.\n- Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System\n  Structure and Classification Rule for Recognition in Partially Exposed\n  Environments".  IEEE Transactions on Pattern Analysis and Machine\n  Intelligence, Vol. PAMI-2, No. 1, 67-71.\n- Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions\n  on Information Theory, May 1972, 431-433.\n- See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al"s AUTOCLASS II\n  conceptual clustering system finds 3 classes in the data.\n- Many, many more ...\n\n|details-end|\n',
 'feature_names': ['sepal length (cm)',
  'sepal width (cm)',
  'petal length (cm)',
  'petal width (cm)'],
 'filename': 'iris.csv',
 'data_module': 'sklearn.datasets.data'}


# In[ ]:


# Pandas mimics R data frames 
import pandas as pd
print(irr.keys())
irrdf = pd.DataFrame(irr["data"], columns=irr["feature_names"])
irrdf


# In[ ]:


dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])


# In[ ]:



sepal length (cm)	sepal width (cm)	petal length (cm)	petal width (cm)
0	5.1	3.5	1.4	0.2
1	4.9	3.0	1.4	0.2
2	4.7	3.2	1.3	0.2
3	4.6	3.1	1.5	0.2
4	5.0	3.6	1.4	0.2
...	...	...	...	...
145	6.7	3.0	5.2	2.3
146	6.3	2.5	5.0	1.9
147	6.5	3.0	5.2	2.0
148	6.2	3.4	5.4	2.3
149	5.9	3.0	5.1	1.8
150 rows × 4 columns


# In[ ]:


# Here's a PCA on the iris data set
#
# Stolen from:  https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401

from sklearn.decomposition import PCA

fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(irr.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=irr.target,
    s=40,
)

ax.set_title("First three PCA dimensions")
ax.set_xlabel("1st Eigenvector")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("2nd Eigenvector")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("3rd Eigenvector")
ax.zaxis.set_ticklabels([])

plt.show()


# In[ ]:


Wrap up
[ ] Make a copy of this file next to your biography & rename it: M0_Python_Refresher_Your_Name.ipynb
[ ] Do all the "YouDo" stuff, above.
[ ] Commit to your branch and push to GitHub.
[ ] Verify that it arrived in your branch within GitHub (I'll pull them all on the due date)

