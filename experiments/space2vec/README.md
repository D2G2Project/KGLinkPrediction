## Paper - WorldKG

This section tries to apply part of the WorldKG algorithm, in 
particular its encoder and framework. The target dataset and the type
of data analyzed e.g. CityGML changes. 

### Execute pipeline

Download the pretrained language models cc.de.300.bin and cc.it.300.bin from https://fasttext.cc/docs/en/crawl-vectors.html.
Place them in the fattextutils directory.

Keep port 7777 open for PostgreSQL.
```
docker-compose -f docker-compose.space2vec.yml up
```

The model will generate txt files with embedding for 1) space2vec and 2) fasttext German 3) fasttext Italian.

For simplicity, the model is run on a small subset of the data. In order to run more data please modify the following files:
- geometry_to_ndarray.py --> change the number of rows to be read from the SQL table. Currently LIMIT 100.
- fasttextutils.utils.py --> change the number of rows to be read from the SQL table. Currently LIMIT 10.

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

<font color="yellow">
Current open issues:

- Parameters used by space2vec for the model are not stated in the paper and the gitub repo is offline.
  - What is the dimension of the encoded vector?
- Space2Vec is a POINT encoder. Currently using the centroid of the polygons and linestrings.
  - Is this a good approximation?
- What will be the output? A vector for each osm_id? It will need to be merged back with the ttl file.

</font>

#### Encoder 2 - Fasttext
Fasttext is used to encode the textual data. The official website is https://fasttext.cc/docs/en/crawl-vectors.html.

Pre-trained models are quite large >2GB. We need to apply this for both German and Italian.

Training name_en might not work in this case since we do not have enough data.

<font color="yellow">Open issues</font>

For South Tyrol is the default name more likely to be in German or Italian? This might pose a challenge for a bilingual region
such as South Tyrol. Should a mixture be used?

For OSM data there is an issue of the presence of name, name_de, name_it or a combination thereof.

For example for osm_id, node=2442568856
- name=Kindergarten Arcobaleno - Scuola Materna Arcobaleno
- name_de=Kindergarten Arcobaleno
- name_it=Scuola Materna Arcobaleno

whereas for osm_id, node=5470887522
- name=Scuola materna “Biancaneve”
- name_de=Kindergarten Biancaneve
- name_it=""

Missing data in one language or the other can be random.