# Use an official Python runtime as a parent image
# to create:
# docker build --rm -t crawler-modis:0.18.20.8-beta .
# to run:
# docker run --name crawler -v /Users/javerdejo/Desktop/ecosur/eris/modis-crawler/files:/crawler/files -v /Users/javerdejo/Desktop/ecosur/eris/modis-crawler/log:/crawler/log crawler-modis:0.18.20.8-beta
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /crawler

# Copy the current directory contents into the container at /app
ADD crawler.py config.py url.json requirements.txt log/ /crawler/

# Configure crontab
ADD crontab /etc/cron.d/crawler-cron
RUN chmod 0644 /etc/cron.d/crawler-cron
RUN touch /var/log/cron.log

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run the command on container startup
CMD ["python", "crawler.py"]
