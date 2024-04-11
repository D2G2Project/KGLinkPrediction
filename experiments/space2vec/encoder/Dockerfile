FROM python:3.10-bullseye

# Add the 'space2vec' and 'fasttextutils' directories to the Python path
ENV PYTHONPATH="${PYTHONPATH}:/space2vec:/fasttextutils"

WORKDIR /code
# Folder where to store the output
RUN mkdir output

RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin libgdal-dev

# Alternative installation of pytorch, from requirements.txt could not get the latest version correctly
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

ADD requirements.txt .
RUN pip install -r requirements.txt

# Add the Python files and the space2vec folder
ADD space2vec.py .
ADD geometry_to_ndarray.py .
ADD space2vec /code/space2vec

# Add the fasttext.py file and the fasttextutils folder
ADD fasttext.py .
ADD fasttextutils /code/fasttextutils
ADD output /code/output

CMD ["python", "space2vec.py", "fasttext.py"]