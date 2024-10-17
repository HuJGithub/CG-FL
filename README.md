# CG-FL: A Data Augmentation Approach using Context-aware Genetic Algorithm for Fault Localization
## Introduction
This repository provides source code of CG-FL.
CG-FL is  a data augmentation approach using context-aware genetic algorithm.

## Environment
OS: Linux  
Python package:  
pandas==0.25.1  
chardet==3.0.4  
numpy==1.16.5  
torch==1.9.0  

## Structure
The structure of the repository is as follows:  
calculate_suspiciousness  
|____CalculateSuspiciousness.py	:calculate suspiciousness of each statement and give the MFR rank or MAR rank according to the real fault line.  
data_process  
|____data_systhesis: data synthesis approaches  
|    |____Genetic_algorithm.py  
|____dimensional_reduction: fault-irrelevant statements reduction  
|	 |____Slice.py		  
metrics : SFL and DLFL metrics  
|____calc_corr.py  
|____dl_metrics.py  
|____metrics.py  
pipeline  
|____Pipeline.py : load different type of data, process data and calculate suspiciousness task  
read_data : load data according to args  
|____DataLoader.py  
|____Defects4JDataLoader.py  
|____ManyBugsDataLoader.py  
|____SIRDataLoader.py  
results : store the results in txt format  
utils : some utils during pipeline  
|____args_util.py  
|____file_util.py  
|____read_util.py  
|____write_util.py  
run.py : program entry  
## Usage
**required arguments: **

name	meaning	value  
-d	dataset	"d4j", "manybugs","SIR"  
-p	program	"Chart", "Closure", "Time", "Lang", ...  
-i	bug_id	"1", "2", ...  
-m	method	"dstar", "ochiai", "barinel", "MLP-FL", ...  
-e	experiment	"origin", "slice", "slice_ga", ...  

## command for running
run.py -d d4j -p Chart -i 1 -m GP02 -e slice_ga
