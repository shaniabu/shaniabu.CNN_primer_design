# CNN Primer Design
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
1. Run [createCrossVal.ipynb](./GPU_run/code/createCrossVal.ipynb) and move the index files obtained to 
