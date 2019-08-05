import sys
import pandas as pd
import numpy as numpy
import json
import time

from PIL import Image
import requests
from io import BytesIO

output = "./downloads/"

thumb_size = 200,200

urls = {}
slug = {}

offset = 1

def parse_url(row):
    if row['model'] == "animals.animal":
        url = row['fields']['image_url']
        urls[row['pk']] = url
        slug[row['pk']] = row['fields']['slug']
        return row['fields']

    else:
        return row['fields']


def download_pics():
    global offset

    try:

        for i in range(offset, len(urls)):
            offset = offset+1
            if urls[i] == 'https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png':
                continue
            print("Downloading: ", i , "  -- URL: ", urls[i] )
            response = requests.get(urls[i])
            img = Image.open(BytesIO(response.content))
            rgb_im = img.convert('RGB')

            rgb_im.save(output + "/" + slug[i] + ".jpg", format="JPEG", quality=100)

            inpath = output + "/" + slug[i] + ".jpg"

            img = Image.open(inpath)
            width, height = img.size

            if width > height:
                diff = (width - height) / 2
                img = img.crop((diff, 0, width - diff, height))
            elif height > width:
                diff = (height - width) / 2
                img = img.crop((0, diff, width, height-diff))

            img = img.resize(thumb_size, Image.ANTIALIAS)

            # path = outdir + "/" + filename
            img.save(output + "/" + slug[i] + ".jpg", format="JPEG",quality=40)


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
