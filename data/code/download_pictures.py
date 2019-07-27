import sys
import pandas as pd
import numpy as numpy
import json
import time

from PIL import Image
import requests
from io import BytesIO

output = "./downloads/"

urls = {}

offset = 1080

def parse_url(row):
    if row['model'] == "animals.animal":
        url = row['fields']['image_url']
        urls[row['pk']] = url
        return row['fields']

    else:
        return row['fields']


def download_pics():
    global offset

    try:

        # Needs to be updated to not download github pics
        for i in range(offset, len(urls)):
            offset = offset+1

            print("Downloading: ", i , "  -- URL: ", urls[i] )
            response = requests.get(urls[i])
            img = Image.open(BytesIO(response.content))
            rgb_im = img.convert('RGB')

            rgb_im.save(output + str(i) + ".jpg", format="JPEG", quality=100)


    except:
        if "http" not in urls[offset-1]:
            download_pics()
        else:
            print("ERRROR: gunna sleep")
            time.sleep(2.5)
            offset-=1
            download_pics()


def main(infile):
    data = pd.read_json(infile)
    data.apply(parse_url, axis=1)


    download_pics()


if __name__=="__main__":
    main(sys.argv[1])
