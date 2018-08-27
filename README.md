# Simple MODIS Web Crawler
###### version 0.18.24.8-beta

Table of contents
=================

<!--ts-->
   * [Introduction](#introduction)
   * [Configuration](#configuration)
      * [config.py](#config-py)
      * [url.json](#url-json)
   * [Build, start and stop docker container](#build-start-stop)
   * [Crawler cron configuration](#cron)
   * [Adding new products for download](#adding-products)   
   * [Running commands into the docker container](#run)
<!--te-->

<a name="introduction"></a>
# Introduction

MODIS Web Crawler is a simple crawler that allows you to automatically download files from the [OceanColor website](https://oceancolor.gsfc.nasa.gov/) for products of the Aqua satellite mission. The crawler ONLY downloads those files that are not in our local repository.

<a name="configuration"></a>
# Configuration

The crawler uses two configuration files which are:

```
- config.py
- url.json
```

<a name="config-py"></a>
## config.py


```python
log_file_name = '/crawler/log/crawler.log'
download_path = '/crawler/files'
urls = '/crawler/url.json'
```
- **log_file_name** sets the path where the log file containing all the operations that the cvrawler has made will be saved.
- **download_path** sets the path where the downloaded files will be stored (local repository).
- **download_path** urls is a file in JSON format where the products to be downloaded are established.

<a name="url-json"></a>
## url.json


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
- **name** Name of MODIS product like chlor_a, sst, etc. To see a complete list of products see [OceanColor website](https://oceancolor.gsfc.nasa.gov/)


<a name="build-start-stop"></a>
# Build, start and stop docker container

- **./tools/build** generates the docker image
- **./tools/start** runs docker container
- **./tools/stop** deletes docker process

<a name="cron"></a>
# Crawler cron configuration

Before to build the docker container it is important to edit the [crontabfile](crontabfile) file to set the cron behavior i.e to program when the crawler will be wake up

Once cron is running, it is possible to modify the configuration, that is, the time and day in which the crawler service will be started by using  the following commands:

```text
$ ./tools/run bash
```

Once inside the docker container, you must modify the file **/crawler/crontab** and set in the file the new configuration for the cron. Finally notify the cron program of the new changes

```text
$ nano /crawler/crontab
$ crontab /crawler/crontab
```

You can verify the changes you have made by using the following command:

```text
$ crontab -l
```

Once you have finished making the changes, exit the docker container

```text
$ exit
```

**IMPORTANT:** All changes made will be valid while the docker container is running, once the container is stopped ALL changes made will be discarded.

<a name="adding-products"></a>
# Adding new products for download

It is possible to add more products for download, for this you must configure the file **/crawler/run/cfg/config.json**. In the following **config.json** file the **nflh** product has been added by inserting the next line after **products** section.

```json
{"name": "nflh"}
```

### config.json updated
 
```json
{
  "base": "https://oceandata.sci.gsfc.nasa.gov",
  "platform": "MODIS-Aqua",
  "level": "Mapped",
  "period": "Monthly",
  "pixel": "4km",
  "products": [
    {"name": "chlor_a"},
    {"name": "sst"},
    {"name": "nflh"}
  ]
}
```


<a name="run"></a>
# Running commands into the docker container

If you want to execute some command in the docker container, you can use the command:

```text
$ ./tools/run <command>
```

for example:

```text
$ ./tools/run bash
```
