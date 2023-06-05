# CNN Primer Design
## Reference
The code of this project is based on the code shared on [primers-sars-cov-2](https://github.com/steppenwolf0/primers-sars-cov-2) by the paper [Classification and specific primer design for accurate detection of SARS-CoV-2 using deep learning](https://www.nature.com/articles/s41598-020-80363-5) published on Nature.

## Data Processing 
1. In the [data](./data) folder, create separate raw data csv files(with FASTA format) with different variants in the [raw_data](./data/raw_data) folder. 
2. Using [data_processing.py](./data/data_processing.py), read csv files by chaning the file names and adding mode="a" starting the second variant.

	```
	raw = pd.read_csv(dataFolder+"raw data/XBB.csv", names=["raw"])
	```
	```
	df.to_csv("sequences.csv", mode="a", index=False, header=False)
	```
3. Add a file labels.csv with numbers from 0 to n, with n=the number of variants in the dataset-1, the number of 0-n numbers corresponds to the order and number of sequences in sequences.csv. 

## Run CNN with GPU-powered Jupyter Notebooks
### Set up GPU-powered Jupyter Notebook
1. UCSD's [Data Science/Machine Learning Platform (DSMLP)](https://blink.ucsd.edu/faculty/instruction/tech-guide/dsmlp) provides undergraduate and graduate students with access to research-class CPU/GPU resources.
2. Submit the [DSMLP Independent Study & Student Research Access Request form](https://docs.google.com/forms/d/e/1FAIpQLSdEZvIfDhSJWz9-uxCCrhuCWOdCKPQwLksy-RdHfOQb3LQEkw/viewform) to get request access to GPU-powered Jupyter Notebook (with tensorflow, at least 4GB). 

### Upload files and setup folders
1. Create a folder "code" and upload the code files in [code](./GPU_run/code) to Jypterhub.
2. Create a folder "data" and two sub-folders "index" and "filters", and upload the code files in [filters](./GPU_run/data/filters) to Jypterhub.
3. Upload sequences.csv and labels.csv to the folder "data". 

### Create Filters
1. Run [createCrossVal.ipynb](./GPU_run/code/createCrossVal.ipynb) and move the index files obtained to the folder [index](./GPU_run/data/index) in folder data. 
2. Run [genCreateFilters.ipynb](./GPU_run/code/genCreateFilters.ipynb) to get sorted sequences by class and print filter and max pooling values. 
3. Move to codes in the folder "filters" in "data", run [posPool.ipynb](./GPU_run/data/filters/posPool.ipynb) to get most important position.
4. Run [createFeatVector.ipynb](./GPU_run/data/filters/createFeatVector.ipynb) to translate into 21-bps features.
5. Run [getFeatures.ipynb](./GPU_run/data/filters/getFeatures.ipynb) to reduce to non-repeated sequences.
6. Run [getFreqMatrix.ipynb](./GPU_run/data/filters/getFreqMatrix.ipynb) to create frequency matrix.

### Run CNN model
1. Create a folder "model" and a folder "results" in the folder "data". 
2. Run [genRunTrain.ipynb](./GPU_run/code/genRunTrain.ipynb) to get the accuracy and summary of results. 

## Run Feature Selection 
1. Move the files data_0.csv, features_0.csv, and labels.csv to the folder [data](./get_features/data). 
2. Run [aBioInf100.py](./get_features/src/aBioInf100.py) in the folder [src](./get_features/src).
3. Run [summaryMulti.py](./get_features/src/summaryMulti.py) to get the reduced list of most important features and get the accuracy. 
