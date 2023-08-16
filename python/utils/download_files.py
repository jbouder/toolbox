import requests
import csv

filename = '/Users/jbouder/repos/toolbox/python/utils/data.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        file_name = row[38]
        file_url = row[39]

url = 'https://s3.amazonaws.com/NARAprodstorage/opastorage/live/24/6096/2609624/content/arcmedia/9-11/MFR/t-0148-911MFR-00038.pdf'
r = requests.get(url, allow_redirects=False)

# open('facebook.ico', 'wb').write(r.content)