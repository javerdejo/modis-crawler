# Use an official Python runtime as a parent image
# to create:
# docker build --rm -t crawler-modis:0.18.24-beta .
# to run:
# docker run --name crawler -v /Users/javerdejo/Desktop/ecosur/eris/modis-crawler/files:/crawler/files -v /Users/javerdejo/Desktop/ecosur/eris/modis-crawler/log:/crawler/log crawler-modis:0.18.20.8-beta
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /crawler

# Copy the current directory contents into the container at /app
ADD crawler.py config.py requirements.txt run/ /crawler/
ADD config.json /crawler/run/etc

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y \
        cron

ENV TZ=America/Mexico_City
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Run the command on container startup
ADD crontabfile /crawler/crontab
RUN crontab /crawler/crontab
CMD ["cron", "-f"]
