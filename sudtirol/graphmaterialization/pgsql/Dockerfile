FROM postgis/postgis:latest

# Install the PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

# Copy the CSV file into the container
COPY FinalInput.csv /docker-entrypoint-initdb.d/

# Copy the SQL script to create the table and load the CSV
COPY sql/init.sql /docker-entrypoint-initdb.d/

# Make sure the script is executable
RUN chmod +x /docker-entrypoint-initdb.d/init.sql