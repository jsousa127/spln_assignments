import re
import unicodedata
import html
from sys import argv

def lookup(word):
    global array 
    if not word:
        return 0   
    
    for e in elements:
        el = e.lower()
        if re.match(el, word) :
            if (len(word) == len(el)) | (lookup(word[len(el):]) == 1):
                array.insert(0,e)
                return 1

    return 0

def strip_accents(word):
   return ''.join(c for c in unicodedata.normalize('NFD', word)
                  if unicodedata.category(c) != 'Mn')

elements = open("elements.txt","r").read().split()
f = open(argv[1],"r")

array = []
elems = ""
try:     
    words = f.read().split()
except:
    try:
        import codecs
        words = codecs.open(argv[1],"r","iso-8859-1").read().split()
    except:
        print("Não foi possivel abrir o ficheiro")    
out = html.initHtml("Words written as a sequence of chemical symbols")
for w in words:
    word = strip_accents(w)
    word = re.sub('[^a-zA-Z]+', '', w).lower()
    if lookup(word):
        for e in array:
            elems += e + " "
        html.addHtml("● %s ☛ %s"%(w.capitalize(),elems),out)  
    del array[:]
    elems = ""
html.endHtml(out)               


  

               
