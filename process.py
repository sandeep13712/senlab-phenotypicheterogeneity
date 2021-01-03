import pandas as pd
from GSVA import gsva, gmt_to_dataframe
# Some extras to look at the high dimensional data
# from plotnine import *
# from sklearn.manifold import TSNE

genesets_df = gmt_to_dataframe('gmtFiles/BiophyicalGeneset.gmt')
print(genesets_df.head())

expression_df = pd.read_csv('filtered2_collapsed.csv',index_col=0)
print(expression_df.columns)
# expression_df = expression_df.drop(labels = ['gene_name'], axis=1)
print(expression_df.iloc[0:5,0:5])
print(expression_df.shape)


pathways_df = gsva(expression_df,genesets_df,method='ssgsea',verbose=True, tempdir='./data')

print(pathways_df.shape)

# XV = TSNE(n_components=2).\
#     fit_transform(expression_df.T)
# df = pd.DataFrame(XV).rename(columns={0:'x',1:'y'})
# (ggplot(df,aes(x='x',y='y'))
#  + geom_point(alpha=0.2)
# )
