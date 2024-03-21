## Paper - WorldKG

This section tries to apply part of the WorldKG algorithm, in 
particular its encoder and framework. The target dataset and the type
of data analyzed e.g. CityGML changes. 


### Pipeline
1. Data Preprocessing
2. Encoder
3. Predictions

### Data Preprocessing
Standard D2G2 pipeline.
Due to encoder limitations all polygons are converted to points, using the centroids.
Modification performed in db-edit.sql.

### Encoders
#### Encoder 1 - Space2Vec
The Space2Vec encoder used is based on the respective paper:
```
@inproceedings{space2vec_iclr2020,
	title={Multi-Scale Representation Learning for Spatial Feature Distributions using Grid Cells},
	author={Mai, Gengchen and Janowicz, Krzysztof and Yan, Bo and Zhu, Rui and  Cai, Ling and Lao, Ni},
	booktitle={The Eighth International Conference on Learning Representations},
	year={2020},
	organization={openreview}
}
```
The official repository is ```https://github.com/gengchenmai/space2vec``` but,
The code used is taken from the respective repository with a sample demo: Gengchen Mai, space2vec_demo, (2020), GitHub repository,
```https://github.com/gengchenmai/space2vec_demo```.


