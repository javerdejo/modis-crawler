# Simple MODIS Web Crawler
###### version 0.18.20.8-beta

## Introduction

MODIS Web Crawler is a simple crawler that allows you to automatically download files from the [OceanColor website](https://oceancolor.gsfc.nasa.gov/) for products of the Aqua satellite mission. The crawler ONLY downloads those files that are not in our local repository.

## Configuration

The crawler uses two configuration files which are:

```
- config.py
- url.json
```

### config.py

```python
log_file_name = '/crawler/log/crawler.log'
download_path = '/crawler/files'
urls = '/crawler/url.json'
```
- **log_file_name** sets the path where the log file containing all the operations that the cvrawler has made will be saved.
- **download_path** sets the path where the downloaded files will be stored (local repository).
- **download_path** urls is a file in JSON format where the products to be downloaded are established.

### url.json
```json
{
  "base": "https://oceandata.sci.gsfc.nasa.gov",
  "platform": "MODIS-Aqua",
  "level": "Mapped",
  "period": "Monthly",
  "pixel": "4km",
  "products": [
    {"name": "chlor_a"},
    {"name": "sst"}
  ]
}
```

- **base** URL for the Ocean Data web site
- **platform** It refers to the platform and can be MODIS-Aqua or MODIS-Terra
- **level** Level of data processing, at the moment only the "Mapped" level is supported
- **period** Annual or Monthly
- **pixel** 4km or 9km

### products
- **name** Name of MODIS product like chlor_a, sst, etc. To see a complete list of products see [OceanColor website](https://oceancolor.gsfc.nasa.gov/)

## Build, start and stop docker container

- **build** Run ./build command to generate the docker image
- **start** Run ./start command to run docker container
- **stop** Run ./stop command to stop an delete docker process
