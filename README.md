# **Assignment 1: Exploring, Ingesting & Analyzing Missing Files in a Dataset**

## **Objective**
In this assignment, you will assume the role of an urban data analyst. Your task is to analyze data from NYC's CitiBike Bikeshare network. You have received a large amount of data from the city, including a number of `.csv`, `.txt` and `.pdf` files, among others, and you will need to transform it to create a report for each station to analyze ridership. 

To make things more complicated, you are not the first person to work on this project. You are taking over the task from a coworker, who recently left the office due to accepting a buyout from a tech billionaire. Before they leave, they send you their data and the progress they have made analyzing a few stations. They also include a module they have inherited from another previous coworker, which they were using to transform the data - it is now up to you to clean it up and finish the project.

Thus, like with any real-world situation, your data is far from perfect. You will need to first figure out what data you have, and what format it is in. And then decide how to proceed.

## **Note on Allowed Packages**
For many of these tasks, there are additional packages available that can help with these tasks (in particular, `pandas` and `numpy`). For this project we ask that you **do not** use them, or any additional packages besides `os` and the module provided. If you solve it using a disallowed library, you will not receive points for that section.

## **Dataset Description**
A directory named **`January Files/`** contains a number of documents:
- **`stations.txt`**: this file contains a list of `station_ids` separated by `|`. They are NOT necessarily distinct.
- **a number of `.csv` files**: These are in the format these contain one line for each ride that *began* at that station.
- **a number of `.png` files**: these contain visualizations of *some* of the data files received. Your collegue has made these by hand before you joined the project.
- **a number of `.pdf` files**: these contain reports which your colleague has completed. You might want to recreate them for consistency.

---

## **Tasks**
### **Part A. Data Investigation [15/15 Total Points]** 
In this section, we'll take stock of all the data we've received and make a report of what we have and what is missing. This is an important first step to **any project** to ensure you are not missing any data, and that all of it is in the correct format.

#### **A.1. Load and Explore the Dataset** [2 points]
- Read in the `stations.txt` file, and split it by `|`s. 
- Calculate the number of distinct stations. **HINT**: Remember, your coworker was not necessarily careful about avoiding duplicates.

#### **A.2. Count the number of each file type provided** [3 points]
- Calculate the number of `.csv`, `.png` and `.pdf` files respectively.

#### **A.3. Create a report of your findings** [10 points]
- Create a new file named `file_report_counts.csv`
- Write your findings to it, creating a table with:
    - **2 columns**: [`type`, `number`]
    - **4 rows**: one for the number of stations, and one for each file type above.

- This file should be formatted as a valid `.csv` file with correctly named **column-headers**.

### **Part B. Data Cleaning [22/20 Total Points]**
The next, essential part of any data analysis task is cleaning the data. Your output of this step will be a script called `data_cleaning.py`, containing functions:
    - `identify_missing`
    - `generate_missing`
    - `get_num_ride`
You will need to hang on to the script to use as a module import into later parts.

#### **B.1. Identify Missing `.csv` Files [2 points]**
- Each `station_id` should also have a corresponding `trips_[station_id]_202501.csv` file.
- Write a function `identify_missing`, that counts and `returns` the number of `.csv` files that are missing.

#### **B.2. Calculate the share of each type that is missing [3 points]**
- Figure out the "*coverage*" (share of total) for each file.
- Add this as a column to your data from part **A.3**, with the column-name `share` and create a new csv called `file_report_share.csv`.
- `share` should be the proportion of total stations, that have data. e.g. `[number of csvs missing]/[number of stations]` (for 'stations' it should be `1`).

#### **B.3. Generate the Missing `.csv` Files [5 points]**
- Write a function `get_num_ride` that 
- For each of the csv files that is missing, create an **empty** csv file, with the correct naming convention.(`trips_[station_id]_202501.csv`)
- For each file, you'll need to not just create the file, but also **add a header with the column-names** that the other files use.
    - This will allow later functions to read in the file as if it is a similar table but just with no rows.

#### **B.4. Report number of rides [5 points]**
- Record the number of rows (rides) starting at each station and write the results to a csv.
- This csv should be named `station_ride_counts_202501.csv` and should have the structure:
    - 2 columns: `number of rides`
    - 1 row per station.
- HINT: you'll want to loop through each of the missing stations as well.

#### ***B.5 [BONUS]. Sort the list of stations by number of rides [2 points]**
- Create another csv, called `station_ride_counts_202501_sorted.csv`, identical to the one you created in **B.4** but sorted with the same rides


### **Part C. Visualize and Report [22/20 Total Points]**
In this part, we will use the data we've now ingested, investigated and cleaned to generate some insights and visualizations. We will have provided a visualization function as part of a separate module. Read the docstring in the 

#### **C.1. Import the visualization function [2 point]**
```
from report_functions import rides_histogram
```

You'll also want to import a function that will help you save your files.
```import matplotlib.pyplot as plt```

#### **C.2. Generate the Visualization `png`s for each station [8 points]**
- Create a new folder named `plots` [2 points]
- Create a visualization for each station using the `rides_histogram` function you just included. The file must be called `plt_[station_code]_202501.png` and all of the files should go in your new folder.

*HINT*: Example of how to use the provided visualization.
```
rides_histogram(input_path = 'path/to/your/file.csv', save_path = 'path/where/you/want/to/save.csv')
```

#### **C.3. Write a function to generate reports using the provided function** [10 points]
- Create a `pdf_reports` folder
- Write a function, `generate_reports`, which loops through each station and generates a pdf for each one.
- To generate a report for a given district, use the `generate_pdf_report` function (also included in the `report_functions.py` module). This function will take in the `file_path` from your generated pngs and additional data
- You'll need to loop through each file and save the files in your reports folder.

#### ***C.4. BONUS - Add a log to keep track of the function's progress [2 points]**
- As your function loops through all the stations, print out progress by 10s. e.g. if there were 333 districts, your script would print out to the terminal:
```
  0/333
 10/333
 20/333
 ...
330/333
DONE!
```
*HINT*: You may want to use the [Modulo](https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/) operator we talked about in class 3.2.

*NOTE*: Careful of the formatting of the numbers. Note that all of them are right-aligned.

### ***Part D [BONUS]. Bonus Exercises for December 6/0
Your old coworker also included files from December in their dataset. However, these are in an older file format. Look at the files and determine what the format is. Read through them and see if you can convert them to the same format as the January csvs. Then we'll do some additional tests on them

#### ***D.1 [BONUS) - Prep the data for December - Convert to CSVs [2 points]**
- Create a new `csvs_202412` folder in your directory.
- For each csv in the `December Data` folder, create a corresponding csv for each file.

Again, you **cannot** use external libraries except `os` and the `report_functions`.

#### ***D.2 [BONUS]. Return the number of distinct destination for each December station [5 points]**
- *NOTE*: This is hard without using a package like numpy or pandas. That is intentional.
- *HINT*: You'll probably want to write this as a function. Think about how you'd store and access data.
- Return this in a csv, named `station_ride_dests_202412.csv` with the format:
    - **3 columns**: `station_id`, `rides`, `destinations`
    - **1 row per station**
- Write these results to another csv called `station_ride

## **Deliverables** 
1. Python script: `analyze_files.py` which contains all of your code
2. Report csvs: 
    1. `station_ride_counts_202501.csv`
    2. `station_ride_counts_202501_sorted.csv` [BONUS]
    2. `station_ride_dests_202412.csv` [BONUS]
3. folders:
    1. `plots`
    2. `January Files`
    3. `pdf_reports`
    4. `csvs_202412` [BONUS]
---

## **Grading Criteria** 
| Criteria                     | Points |
|------------------------------|--------|
| All files created and exercises completed | 55 |
| Efficient and well-structured Python script | 10 |
| Code includes comments and relevant typing, docstrings | 10 | 
| Total | **75** |

---

Good luck!
