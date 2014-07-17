import numpy as np
import matplotlib.pyplot as pyplot

#
# Create histogram from data for presentation
# Author: Bryce Danz
# Date: 07/16/14
#

N = 15
counts = (98, 83, 75, 61, 56, 44, 38, 36, 33, 32, 32, 32, 30, 29, 29)

#x locations
ind = np.arange(N)

#bar widths
width = .5

fig, ax = pyplot.subplots(figsize=(10,10))
rects1 = ax.bar(ind, counts, width, color='blue')

ax.set_xlim(-width * 2, len(ind) + width)

ax.set_ylabel('Counts', rotation='vertical')
ax.set_title('Counts by item for sale:')
ax.set_xticks(ind+ .5*width)

#top terms
ax.set_xticklabels(('book/s', 'ticket/s', 'i/phone', 'bed', 'table', 'mattress', 'tv', 'bike', 'coffee', 'shoes', 'frame', 'dress', 'xbox', 'desk', 'couch'), rotation='vertical')

#add labels
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.025*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)

pyplot.show()
