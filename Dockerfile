# pull official base image
FROM python:3.11.3-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat && apt-get install -y postgresql-client

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

# FROM postgres:10.2
# RUN apt-get update && apt-get install -y vim-tiny
# RUN mkdir /app
# WORKDIR /app
# ADD README.md /app/
# USER postgres
#RUN    /etc/init.d/postgresql start &&\
#    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
#    createdb -O docker docker
# Copy the SQL file and entrypoint script into the container
COPY model/database.sql /docker-entrypoint-initdb.d/
COPY entrypoint.sh /usr/local/bin/

# Make the entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh
# Expose the PostgreSQL port
EXPOSE 5432
EXPOSE 5001
# Add VOLUMEs to allow backup of config, logs and databases
# VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
#RUN psql -h olhapedidodb.internal -U flypgadmin -d olhapedido -f /model/database.sql

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
