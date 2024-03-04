import csv

# TODO Compute centralities
'''
with open('shake000023-richard-iii.network.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(row[0])
        print(row[0].split(',')[0])
'''

# Python program to read
# json file
 
import json
 
file = open('hamlet_scene1.json')
 
# deserializes into dict and returns dict.
data = json.load(file)

discourses = {}
# Iterating through the json list
for discourse in data[0]['lines']:
    speaker = discourse['speaker']
    receiver = discourse['receiver']
    text = discourse['text']

    if speaker not in discourses:
        discourses[speaker] = {}
    
    if receiver not in discourses[speaker]:
        discourses[speaker][receiver] = len(text.split(' '))
    else:
        discourses[speaker][receiver] = discourses[speaker][receiver] + len(text.split(' '))
 
print(discourses)
# Closing file
file.close()

# open the file in the write mode
file_writer = open('hamlet_scene1_v1.csv', 'w')

# create the csv writer
writer = csv.writer(file_writer)

writer.writerow(["Source","Target","Weight"])
for speaker,composite in discourses.items():
    for receiver, weigth in composite.items():
        writer.writerow([speaker,receiver,str(weigth)])

# close the file
file_writer.close()