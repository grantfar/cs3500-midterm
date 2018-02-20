import re
fileC = open("spectrum.c","r")
stringC = fileC.read()
fileC.close()



stringC = re.sub("(.*)\n","<div class=\"codeLine\"> \\1 </div>\n",stringC)
stringC = re.sub("(?<!class=)(?!\">)(\".*\")","<span class=\"string\">\\1</span>",stringC)
stringC = re.sub("([\n\s\*\(\{])(int|double|char|FILE)([\n\s\)])","\\1<span class=\"declare\">\\2</span>\\3",stringC)
stringC = re.sub("([\n\s\*\(\{\)])(for|if|else|fprintf|printf)([\n\s\(])","\\1<span class=\"reserved\">\\2</span>\\3",stringC)
print(stringC)


fileHTML = open("spectrum.html","w");

fileHTML.write("<meta  charset=\"utf-8\"><link rel=\"stylesheet\" href=\"css/code.css\">\n<code>"+stringC+"</code>");
fileHTML.close();
