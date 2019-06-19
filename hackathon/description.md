# Hackathon 2019 - Information and Projects Description

This document contains the basic details on each of the available projects for this year's hackathon. The description should suffice when making a descision regarding the project you wish to undertake. Once you have a couple of favorite projects head over [here](http://polljunkie.com/poll/rrdkon/hackathon-2019-projects) and rank them from most to least preferable. All students should rank their preferences, even those who informed me that they can't attend.

## General Information

The hackathon will take place during June 19-20th. We start at 9 AM on Wednesday in the Naftali Building (floor number 5, the exact rooms will be updated here soon enough). Food and beverages, including lunch and dinner, will be served there. At about 19:00 we'll have a special lecture with an external guest from IBM who'll talk to us about Python in their company. Work on your projects may continue until 21:00, when the building closes.

The next day you arrive at your own pace, but shortly after noon time you're expected to start preparing your presentations. The grade for the hackathon is determined mostly by this presentation, so make sure it displays the work you've done in the past two days in a comprehensive manner. A presentation template can be found in this folder. Presentations start at 15:00, and we expect the event to end by 16:30.

## Grading

40% - Code quality - usage of objects\methdos\functions, proper libraries, tests, git, PyPI.
40% - Collaboration and Presentation
20% - Is the application usable?

## Project 1: Real-time Readout and Analysis of Analog Data
### Mentor: Dr. Jason Friedman

For this project, students will create an application that runs a game used to study coordination in humans. During this game, the subject presses on a pressure sensitive detector, which in turn controls the behavior of a figure on a screen, in a very similar fashion to [flappy bird](https://flappybird.io/). The two main parts of the project consist of (1) connecting and reading the pressure data from a digital-to-analog device, and (2) interpreting this data and sending it online to a process which is responsible to move a figure on screen based on the value that was recorded by the sensor.

Relevant Libraries:
1. `pygame`
2. `zeromq`

# Project 2: Sub-movements Detection From Motion-capture Data
### Mentor: Dr. Jason Friedman

These experiments aim to find the components that compose typical hand movements made by humans, and how they change when presented with new information. A motion-capture sensor is placed on the finger of the subject, and the data recorded from it represents the position of the finger during each trial. When the subject points at some stimulus we expect to be able to "decompose" the entirety of the gesture into smaller, shorter movements. In this project you'll write a pipeline-like application which reads the data from disk, reduces the inherit noise in it, detects and marks the sub-movements in it and finally displays the results.

Relevant libraries:
1. `pandas`
2. `scipy`
3. Plotting library (like `matplotlib`, but not a must)

# Project 3: MRI Magnetic Field Reconstruction
### Mentor: Dekel Vered (Prof. Uri Nevo)

MRI machines are extremely expensive in part due to the perfect homogenic magnetic field that has to be generated inside them. But what if you could generate a non-perfect field, and correct the recorded data by analyzing the imperfections in the generated field? In this project students will create a pipeline that simulates such non-perfect MRI data by "spoiling" perfect data in a known manner, only to the try to reconstruct the true, "perfect" field using existing methods in the literature.

Relevant libraries:
1. `PySimpleGUI`
2. `multiprocessing`
3. `matplotlib`
4. `xarray`

# Project 4: Eye Tracker Analysis
### Mentor: Libi Kliger (Prof. Galit Yovel)

Prof. Galit Yovel's Person Recognition lab experiments with human subjects on topics related to the way we recognize other humans. To answer these questions they use an eye-tracking device, which records the coordinates of the screen pixel that the subject's eye was gazing upon every moment. In a recent experiment, they showed three types of images to subjects and asked them to fixate on a specific point on the screen. However, they can't be sure that subjects _did_ look on that point during all times, and whether specific events occurring on-screen motivated these shifts. The goal of the project is to create a tool that given the raw data and the general experimental design, outputs figures showing a "heatmap" of the gaze of each subject, as well as more quantitave data regarding the correlation of the fixation times to the other things happening on-screen.

Relevant libraries:
1. `PySimpleGUI`
2. `pandas`
3. `matplotlib`

# Project 5: Exploratory Genetic Analysis
### Mentor: Guy Taichman (Prof. Oded Rechavi)

The project is based on a large dataset containing the relative expression of thousands of genes in worms under many different conditions. Many of these genes are associated with expected phenotypes that should be evident under certain conditions. The goal is to find where the given external conditions dramatically changed the expression of certain genes, and to correlate these changes with the known function of the genes. The data on both the expression levels and the gene's function has already been collected and formatted properly, leaving the students undertaking the project to find interesting, machine-learning based methods to analyze the data.

Relevant libraries:
1. `scikit-learn`
2. `pandas`

# Project 6: Graphical User Interface for fMRI Data Exploration
### Mentor: Shachar Gal (Dr. Ido Tavor)

fMRI and DTI data is complex: It's multidimensional, it supports many types of analysis and therefore is sometimes hard to visualize. The goal of this project is to create a modular GUI that supports different types of visualizations for each individual scan. Once pointed to a scan, the GUI will prompt the user to choose a parcellation atlas, which will then allow it to show a connectivity matrix of the scan, measure certain graph properties between different brain areas and more.

Relevant libraries:
1. `nipy`
2. `bokeh`
