"""Web crawler."""
from bs4 import BeautifulSoup
from config import download_path
import glob
import requests
import re

files = []


def download(fname, url):
    """Download file."""
    if download_path + fname not in files:
        print fname
        req = requests.get(url).content
        with open(download_path + fname, 'wb+') as f:
            f.write(req)


def main(link):
    """Define main function."""
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
            download(fname, url)


if __name__ == '__main__':
    files = glob.glob(download_path + '*.nc')
    link = 'https://oceandata.sci.gsfc.nasa.gov/MODIS-Aqua/Mapped/Monthly/4km/chlor_a/'
    main(link)
