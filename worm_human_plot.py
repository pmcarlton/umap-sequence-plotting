import h5py
import umap
import plotly.express as px
import pandas as pd

with open('human-pdesc') as fh:
    hdesc=[x.strip() for x in list(fh)]

with open('worm-pdesc') as fh:
    wdesc=[x.strip() for x in list(fh)]

hfworm=h5py.File("elegans-protein.h5",'r')
wormkeys=list(hfworm.keys())
wormprot=[hfworm[x][()] for x in wormkeys]
hfworm.close()

hfhuman=h5py.File('human-protein.h5','r')
humankeys=list(hfhuman.keys())
humanprot=[hfhuman[x][()] for x in humankeys]
hfhuman.close()

reducer=umap.UMAP()

wormfit=reducer.fit(wormprot)

wormxy=wormfit.transform(wormprot)
humanxy=wormfit.transform(humanprot)

proteins=pd.concat((pd.DataFrame(wormxy,index=wormkeys,columns=['X','Y'],copy=True).assign(species='worm'),pd.DataFrame(humanxy,index=humankeys,columns=['X','Y'],copy=True).assign(species='human')),axis=0)

wdhd=[x[0]+x[1] for x in (zip(wormkeys,wdesc))]+[x[0]+x[1] for x in (zip(humankeys,hdesc))]

fig=px.scatter(proteins,x='X',y='Y',color='species',hover_name=wdhd)
fig.update_traces(marker=dict(opacity=0.3))
fig.write_html('figure.html')
