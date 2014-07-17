import sys
import requests
import json
from pprint import pprint
import csv

#
# Retrieve data from a facebook group's feed for analysis
# Author: Bryce Danz
# Date: 07/16/14
#


#need an access token? Grab one at https://developers.facebook.com/tools/explorer/

#recursively call process_items until all paging has been handled
def process_items(data, writer):
    #dump json to the console to help with troubleshooting
    pprint (data)
    #get data for message, time, and name fields
    for item in data['data']:
        try:
            if item['message']:
                writer.writerow([item['message'], item['created_time'], item['from']['name']])
        except(TypeError, KeyError):
            #handle lines without one of the fields
            pass

    if data['paging']:
        try:
            url = data['paging']['next']
            data = requests.get(url).json()
            process_items(data, writer)
        except(KeyError):
            #handle end of input (no more paging)
            return writer

#read in command line args
try:
    file_name = sys.argv[1]
    ACCESS_TOKEN = sys.argv[2]

except IndexError:
    print ("Usage: getgroupdata.py filename.txt OAuth_Access_Token")
    sys.exit(1)

#write results to CSV
ofile = open(file_name, "w")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

#set up initial request for data
base_url = 'https://graph.facebook.com/v2.0/'
fields = '369460706502532/feed'

url = "{0}{1}?&access_token={2}".format(base_url, fields, ACCESS_TOKEN)

data = requests.get(url).json()

process_items(data, writer)
#close CSV when writing complete
ofile.close()
