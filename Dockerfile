# Use an official Python runtime as a parent image
# docker build --rm -t eris/crawler-modis .
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /crawler

# Copy the current directory contents into the container at /app
ADD crawler.py /crawler
ADD config.py /crawler
ADD url.json /crawler

# requiriments for the crawler
ADD requirements.txt /crawler

# Configure crontab
ADD crontab /etc/cron.d/crawler-cron
RUN chmod 0644 /etc/cron.d/crawler-cron
RUN touch /var/log/cron.log

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
