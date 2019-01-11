def initHtml(title): 
    try:
        out = open("out.html", "c")
    except:
        try:
            out = open("out.html","w")
        except:
            print("Impossivel criar o ficheiro html")

    out.write("<html>\n<head><title>Words written as a sequence of chemical symbols</title></head>\n<body>\n<h1>Words written as a sequence of chemical symbols</h1>\n")
    return out


def addHtml(content, file):
    file.write("<p>%s</p>"%content) 


def endHtml(file): 
    file.write("<hr />\n</body>\n</html>")
    file.close()
