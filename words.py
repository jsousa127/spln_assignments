import re
import unicodedata

f = open("file.txt","r")
e = open("elements.txt","r")
words = f.read().split()
elements = e.read().split()

def lookup(word):
    if not word:
        return 0   
    
    for e in elements:
        e = e.lower()
        if re.match(e, word) :
            if (len(word) == len(e)) | (lookup(word[len(e):]) == 1):
                return 1



def strip_accents(word):
   return ''.join(c for c in unicodedata.normalize('NFD', word)
                  if unicodedata.category(c) != 'Mn')


for w in words:
    w = strip_accents(w)
    w = re.sub('[^a-zA-Z]+', '', w).lower()
    if lookup(w):
        print(w)
    
    

               