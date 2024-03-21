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

#### Encoder 2 - Fasttext
Fasttext is used to encode the textual data. The official website is https://fasttext.cc/docs/en/crawl-vectors.html.

Pre-trained models are quite large >2GB. We need to apply this for both German and Italian.

Training name_en might not work in this case since we do not have enough data.

TODO: Check whether the default name is more likely to be in German or Italian. This might pose a challenge for a bilingual region
such as South Tyrol.