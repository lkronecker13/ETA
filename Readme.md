# ETA project

This project was developed as a Data science test for a potential employer. The data is not provided for privacy reasons.

## Project structure

### Notebooks

In the root folder of the project you will find two notebooks prepended with a number:

```
1. EDA
2. Modeling
```

This files are to be opened in order so that the flow in which the project was developed can be followed. 

### Data

The folder data contains the following paths:

```
1_original: Contains the original data as was received. The contents of this folder should never be modified so we always have a backup.
2_modeling: Contains the data that resulted from the preprocessing and EDA steps
3_results: Contains data that was saved since we considered useful for the future.
```

### Results

In the folder data/3_results there are two files called 'df eta trip results' and 'df eta all results' which contain new columns with the
different eta predictions from the Modeling step.

### Tools

The file tools.py contains some functions that are shared among the notebooks. I moved them here to free some space in the notebooks.
Please feel free to have a look.

## Project setup

In order to successfully run the project make sure that Anaconda (https://www.anaconda.com/downloads) is installed in your system since it is used as an 
environment/package manager. 

Once conda is installed in your system navigate to the project's root in your terminal (where the file transit_env.yml) and run the
following command:

```conda env create -f transit_env.yml```

This will create the environment that will be used to run the project. Once all the packages are installed run the command:

```jupyter notebook```

Once the web interface opens you will have access to the following notebooks:

```
1. EDA
2. Modeling
```

Open them in order so you can start looking at the project. Feel free to follow along by just reading or executing the code
in the notebook. Some of the code blocks will take a while to finish executing since the data files are kinda big.


With all this said I think you should be able to successfully run the project!



