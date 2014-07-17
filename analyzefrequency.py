from prettytable import PrettyTable
import csv
import sys

#
#  Program calculates most frequently appearing word in saved CSV dump of group for sale ads
#  Data from: https://www.facebook.com/groups/369460706502532/
#  All posts between 2013-04-04T04:46:32+0000 and 2014-07-10T02:04:20+0000
#  Author: Bryce Danz
#

try:
    stopwords = sys.argv[1];
    input_file = sys.argv[2];
    output_file = sys.argv[3];

except IndexError:
    print ("Usage: analyzefrequency.py stopwords input_file output_file")
    sys.exit(1)

#load stopwords file
stopwords = set(open('stopwords.txt').read().split())

#create empty dictionary to hold frequency counts
words = {}

#add words in a row to the dictionary
def process_row(row):
    sentence = (row.split())
    for word in sentence:
        word = word.lower()
        if not word in stopwords and len(word) < 20:
            words[word] = words.get(word, 0) + 1

#read in the data
with open(input_file, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter='\t', quotechar='"')
    for row in data:
        process_row(row[0])

#sort the dictionary by frequency for display
result = sorted([value, key] for (key, value) in words.items())

#print highest counts first
result.reverse()

#close CSV
csvfile.close()

#write frequency results to CSV
ofile = open(output_file, "w")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
for row in result:
    writer.writerow(row)
ofile.close()





