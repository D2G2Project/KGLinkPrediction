FROM python:3.10-bullseye
WORKDIR /code

# Install required packages
ADD requirements.txt .
RUN pip install -r requirements.txt

# Copy the input files and the python script
COPY bolzano.osm.pbf .
COPY constructgrid.py .

# Run python script and load data to SQL db
CMD ["python", "-u", "constructgrid.py"]