#!/usr/bin/env python
"""MODIS Web Crawler."""
from bs4 import BeautifulSoup
from config import download_path, urls, log_file_name
import datetime
import glob
import json
import os
import requests
import re


def download(fname, url, files, save_in):
    """Download file."""
    if fname not in files:
        printLog("downloading %s" % (fname))
        req = requests.get(url).content
        with open(save_in + '/' + fname, 'wb+') as f:
            f.write(req)
            printLog("%s downloaded" % (fname))


def startCrawler(cfg):
    """Define main function."""
    for product in cfg['products']:
        link = cfg['url'] + '/' + product['name']
        save_in = "%s/%s/%s/%s/%s/%s" % (download_path, cfg['platform'],
                                         cfg['level'], cfg['period'],
                                         cfg['pixel'], product['name'])
        files = glob.glob(save_in + '/*.nc')

        req = requests.get(link).content

        soup = BeautifulSoup(req, 'html.parser')
        # gets all links
        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            # extracts url
            url = link.get('href')
            # is a nc file?
            if url.find('km.nc') != -1:
                # gets only the name
                fname = url.rsplit('/', 1)[-1]
                download(fname, url, files, save_in)


def loadConfig(file_name):
    """Load configuration file."""
    with open(file_name) as f:
        data = json.load(f)

    base_url = "%s/%s/%s/%s/%s" % (data['base'], data['platform'],
                                   data['level'], data['period'],
                                   data['pixel'])
    data.update({'url': base_url})
    return data


def configBucket(cfg):
    """Configure the bucket to download the files."""
    for product in cfg['products']:
        data_path = "%s/%s/%s/%s/%s/%s" % (download_path,
                                           cfg['platform'],
                                           cfg['level'],
                                           cfg['period'],
                                           cfg['pixel'],
                                           product['name'])

        if not os.path.exists(data_path):
            os.makedirs(data_path)
            printLog("bucket %s created ..." % (data_path))


def printLog(arg):
    """Print log function."""
    strLog = "> %s: -> %s\n" % (str(datetime.datetime.now()), arg)
    log_file.write(strLog)
    log_file.flush()


def main():
    """Define main fuction."""
    global log_file

    cfg = loadConfig(urls)
    log_file = open(log_file_name, 'a+')
    printLog("looking for updates")
    configBucket(cfg)
    startCrawler(cfg)
    printLog("all is updated")
    log_file.close()


if __name__ == '__main__':
    main()
