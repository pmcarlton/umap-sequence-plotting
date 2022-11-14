# first, import the required modules:
import h5py
import umap
import plotly.express as px
import pandas as pd

# load the worm protein embeddings:
hfworm=h5py.File("elegans-protein.h5",'r')
wormkeys=list(hfworm.keys())
wormprot=[hfworm[x][()] for x in wormkeys]
hfworm.close()

# load the human protein embeddings:
hfhuman=h5py.File('human-protein.h5','r')
humankeys=list(hfhuman.keys())
humanprot=[hfhuman[x][()] for x in humankeys]
hfhuman.close()

# create a UMAP-reducer object
reducer=umap.UMAP()

# create the fit of worm protein embeddings into 2D space:
wormfit=reducer.fit(wormprot)

# use the fit to transform both worm and human proteins:
wormxy=wormfit.transform(wormprot)
humanxy=wormfit.transform(humanprot)

# create a Pandas data frame for plotting:
proteins=pd.concat((pd.DataFrame(wormxy,index=wormkeys,columns=['X','Y'],copy=True).assign(species='worm'),pd.DataFrame(humanxy,index=humankeys,columns=['X','Y'],copy=True).assign(species='human')),axis=0)

# create the plot as an HTML file
fig=px.scatter(proteins,x='X',y='Y',color='species',hover_name=proteins.index)
fig.update_traces(marker=dict(opacity=0.3))
fig.write_html('figure.html')

# now double-click the HTML file to see the plot
