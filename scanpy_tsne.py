#!/usr/bin/env python

from itertools import combinations
import random

import scanpy.api as sc
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

from granatum_sdk import Granatum

# import pandas as pd
# import seaborn as sns


def main():
  gn = Granatum()

  df = gn.pandas_from_assay(gn.get_import('assay')).T
  random_seed = gn.get_arg('random_seed')
  perplexity = gn.get_arg('perplexity')
  early_exaggeration = gn.get_arg('early_exaggeration')
  metric = gn.get_arg('metric')

  #sc.tl.tsne(adata, random_state=random_seed)

  #X_tsne = adata.obsm['X_tsne']
  X_tsne = TSNE(perplexity=perplexity, early_exaggeration=early_exaggeration, metric=metric, random_state=random_seed).fit_transform(df)

  plt.figure()
  plt.scatter(X_tsne[:, 0], X_tsne[:, 1], 5000 / df.shape[0])
  plt.xlabel('t-SNE dim. 1')
  plt.ylabel('t-SNE dim. 2')
  plt.tight_layout()
  gn.add_current_figure_to_results('t-SNE plot: each dot represents a cell', dpi=75)

  pca_export = {
    'dimNames': ['t-SNE dim. 1', 't-SNE dim. 2'],
    'coords': {sample_id: X_tsne[i, :].tolist() for i, sample_id in enumerate(df.index)},
  }
  #gn.export_statically(pca_export, 't-SNE coordinates')
  gn.export(pca_export, "{}".format(gn.get_arg("coord_name")), kind='sampleCoords', meta=None)

  gn.commit()


if __name__ == '__main__':
  main()
