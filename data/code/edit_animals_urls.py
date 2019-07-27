import sys
import pandas as pd
import numpy as numpy
import json


output = []

urls = {}


def edit_url(row):
    if row['model'] == "animals.animal":
        url = row['fields']['image_url']
        index1 = url.find("commons/")

        url2 = url[0:index1+8] + "thumb/"

        
        index2 = url2.find("thumb/")

        url2 = url2 + url[index1+8:]

        index3 = url2.rfind("/")

        url3 = url2 + "/1200px-" + url2[index3+1:]

        urls[row['pk']] = url3

        return row['fields']
    else:
        return row['fields']

def add_to_JSON(row):
    obj = {}
    obj["fields"] = row.values.tolist()[0]
    obj["model"] = row.values.tolist()[1]
    obj["pk"] = row.values.tolist()[2]
    output.append(obj)
    return row

def main(infile):
    data = pd.read_json(infile)
    data['fields'] = data.apply(edit_url, axis=1)

    data.apply(edit_url, axis=1, raw=True)

    data.apply(add_to_JSON, axis=1)

    #print(json.JSONEncoder().encode(output))


    for obj in output:
        if obj['model'] == "animals.animal":
            obj['fields']['image_url'] = urls[obj['pk']]


    with open('data2.json', 'w') as f:
        json.dump(output,f)
    #print(data['fields'])
    #print(output)
    #data.to_json("data2.json", orient='values')

if __name__=="__main__":
    main(sys.argv[1])