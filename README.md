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
	
