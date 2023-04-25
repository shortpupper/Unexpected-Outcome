"""
NOT MY CODE
OG AUTHER
https://gist.github.com/hantoine/c4fc70b32c2d163f604a8dc2a050d5f6
"""

from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)