import sys
import os

import pandas as pd
import numpy as numpy
import json

urls = {}

def parse_data(row):
    if row['model'] == "animals.animal":
        url = row['fields']['image_url']
        urls[row['pk']] = row['fields']['slug']
        return row['fields']
    else:
        return row['fields']


def main(imagedir, datapath):
    data = pd.read_json(datapath)
    data.apply(parse_data, axis=1)


    files = os.listdir(imagedir)
    files.sort()
    for filename in files:
        if filename.endswith(".jpg"):
            i = filename.find(".");
            pk = int(filename[:i])
            os.rename(imagedir + "/" + filename, imagedir + "/" + urls[pk] + ".jpg")




if __name__=="__main__":
    main(sys.argv[1], sys.argv[2])
