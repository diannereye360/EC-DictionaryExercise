
'''
Word Index - Analyze the text of the book of John from the Bible and display how many times
 each of these words show up in the text - 'Father', 'God', 'Christ', 'Spirit', 'life', 'man' (case sensitive).
 The text file is available here (note: all punctuation marks, chapter and verse references have been removed to allow to 
 analyze each word) - book of John text.txt Download book of John text.txt 

'''

search_list=['Father','God','Christ','Spirit','life','man']


infile = open("book of John text.txt","r")

content = infile.read()

text = content.split(" ")

dict = {}

for k in search_list:
    dict[k]=0
    for word in text:
        if k == word:
            dict[k] = dict[k] + 1

for key in list(dict.keys()):
    print(key,":", dict[key])