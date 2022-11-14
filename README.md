# umap-sequence-plotting
Visualization and comparison of protein and DNA sequence embeddings

<img width="879" alt="Worm_Human_UMAP" src="https://user-images.githubusercontent.com/1320820/201573317-377e2be9-8fb8-4bc3-a28a-cc5a7e7952c9.png">


Instructions should work on Mac OSX of recent versions (v12 and higher)

The steps needed are:

1. Obtain protein embedding files from Uniprot

2. Prepare the python environment

3. Modify (if necessary) and run the provided script


# Obtaining the embedding files:

See the explanation here:
https://www.uniprot.org/help/embeddings

Download from here:
https://www.uniprot.org/help/downloads

The two files needed for this example are:
- https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/embeddings/UP000001940_6239/per-protein.h5
- https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/embeddings/UP000005640_9606/per-protein.h5

### Note that these files have the same base filename, so you'll need to rename them (e.g. "elegans-protein.h5")

Download these files one at a time, renaming as necessary, and place them in a new directory.

# Preparing the python environment

1. Install "pip" (a package manager for python) from the Terminal if necessary: 

`python3 -m ensurepip`
 
2. Install the needed modules (Dash, UMAP, Pandas, and iPython for ease of use):

### One way to do it is:
`pip install dash`
`pip install pandas`
`pip install umap-learn`
`pip install ipython`

### Another way is to use `conda` to create a virtual environment and install the same thing (TODO explain more about this)

3. Start iPython and run the "worm_human_plot.py" script:

`ipython`

(you can then paste in the commands from the script line-by-line)

Alternatively you can just run the script using `python3 worm_human_plot.py` from the Terminal, non-interactively.



