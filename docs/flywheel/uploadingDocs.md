---
layout: default
title: Custom Info Uploader
parent: Flywheel
nav_order: 6
has_toc: false
---
# Uploading To Flywheel
There are several ways to get your data onto flywheel. Which one you should use will depend on the type and quantity of data you are uploading.

1. The Graphical User Interface (GUI), a.k.a. the website: This is best to use only when you are uploading small files, such as attachments and logs, to individual projects, subejcts, sessions, or acquisitions.
2. The Command Line Interface: This is the most flexible way to upload your data. There are several commands that you can use and tailor to your particular use case. You can find the documentation here: https://docs.flywheel.io/hc/en-us
3. Using the Custom Info Uploader Script: This is how cool kids upload their subject-level custom information. If you have a csv of data you need to upload to individual subjects, this tool will allow you to do it in one command.
4. Using the Self-Report Score and Upload Gear:

## Way 1: Using the GUI
A. Uploading a file at the project level: Go to any subject in the project of interest, and navigate to the project tab.
![alt text](https://github.com/PennBBL/pennbbl.github.io/assets/images/project_tab.png "Project Tab")

Scroll down until you see the Attachments, and click on "Upload Attachment".
![alt text](https://github.com/PennBBL/pennbbl.github.io/assets/images/attachments.png "Attachments")

Then, you should see this window prompting you to drag the file to upload.
![alt text](https://github.com/PennBBL/pennbbl.github.io/assets/images/upload_file.png "Upload File")

Do so, and the file should upload automatically. Click close when you're done.
This same procedure can be done at the subject and session levels by clicking on the appropriate tab.

To upload a file at the acquisition level, navigate to the Acquisitions tab. Then scroll down to the acquisiton you'd like to upload to, and click on the rightmost three vertical buttons as seen below.
![alt text](https://github.com/PennBBL/pennbbl.github.io/assets/images/acquisition_threebuttons.png "Upload File")

select "Upload Data To Acquisition", and drag the file to the box prompting you to upload.
![alt text](https://github.com/PennBBL/pennbbl.github.io/assets/images/acq_dragdrop.png "Upload File Box")
click on "Upload" when you're done.



## Way 2: Using the CLI
For instruction for installing the CLI, the different commands to upload, and when best to use them, see Flywheel's CLI documentation here: https://docs.flywheel.io/hc/en-us

## Way 3: Using the Custom Info Uploader Script

This script takes as input a CSV file with the following characteristics:
 1. No Protected Health Information (PHI) in the file
 2. All columns are named
 3. The subject ID column is named "bblid"

It then organizes the data into dictionaries and uploads it to each subject's Custom Info field on flywheel. The script can be called in the terminal by doing:
```
python customInfoUploader.py -d path/to/CSV -p name_of_project -n dict_name
```
For example, to upload data in a csv called "flavortown.csv" to my "GUY_FIERI" project on flywheel as a custom field called "recipes" I would do:
```
python customInfoUploader.py -d flavortown.csv -p GUY_FIERI -n recipes
```

*NOTE: Prior to uploading, please sign into a flywheel session in your environment. See here for instructions: https://flywheel-io.github.io/core/branches/master/python/getting_started.html*

See below for the script. You can also find it here: https://github.com/diegodav/general_customInfoUploader/blob/master/customInfoUploader.py

```
#####################################################################################
####                           Custom Info Uploader                              ####
####                           By: Diego G. Dávila                               ####
####                            Satterthwaite Lab                                ####
####               University of Pennsylvania School of Medicine                 ####
#####################################################################################
#
# This script takes as input a CSV file with the following characteristics:
# 1. No Protected Health Information (PHI) in the file
# 2. All columns are named
# 3. The subject ID column is named "bblid"
#
# It then organizes the data into dictionaries, and uploads it to each subject's Custom Info field on flywheel.
#
# The script can be called in the terminal by doing: python customInfoUploader.py -d path/to/CSV -p name_of_project -n dict_name
#
# *NOTE: Prior to uploading, please sign into a flywheel session in your environment. See here for instructions: https://flywheel-io.github.io/core/branches/master/python/getting_started.html


import sys
import csv
import numpy as np
import pandas as pd
import os
import argparse
import math


# Set up argument parsing for the required inputs
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--data', required = True) # the csv containing data
parser.add_argument('-p', '--project', required = True) # the name of the project you're uploading to
parser.add_argument('-n', '--name', required = True) # the desired name for the dictionary
inputs = parser.parse_args()

# Feed in the user inputs
path2data = inputs.data
project = inputs.project
name = inputs.name

# Read in the data
customData = pd.read_csv(path2data)

#turn the bblid field into string
customData.bblid = customData.bblid.astype('str')

# make the bblid column the index
customData.set_index('bblid', inplace=True)

# Turn the scored data.frame into a dictionary
fullDict = customData.to_dict(orient = 'index')

# Loop thorugh the newly created dictionary, and nest all the fields in their own dictionary for each subject
for x in fullDict:
    fullDict[x] = {'{}'.format(name): fullDict[x]}

# Replace NAs - uploading NAs to flywheel interferes with the GUI and makes objects not visible. This function replaces them with None, which flywheel should be able to handle.
def iter_replace_dict_nans(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, dict):
            iter_replace_dict_nans(value)
        elif pd.isna(value):
            input_dict[key] = None
iter_replace_dict_nans(fullDict)


## Attach To Each Subject On Flywheel ##
# Create an instance of flywheel and containers for sessions and subjects
import flywheel
projname = '{}'.format(project)
fw = flywheel.Client()
projectContainer = fw.projects.find("label={}".format(projname))
projectContainer = projectContainer[0]
sessions = projectContainer.sessions()
subjects = projectContainer.subjects()


#Attach the dictionaries to the appropriate session objects
for i in range(len(subjects)):
    bblid = subjects[i].label.lstrip("0") # removes any leading zeros there may be
    if bblid in fullDict:
        try:
            subjects[i].update_info(fullDict[bblid])
        except AssertionError as y:
             logger.setLevel(logging.DEBUG)
             logger.error("Subject not found.")
             logger.error(y)
        print ("Uploading {}'s Info".format(bblid))
    else:
        print('{} was not uploaded because it was not found in the input csv'.format(bblid))
```

## Way 4: Using the Self-Report Score and Upload Gear
