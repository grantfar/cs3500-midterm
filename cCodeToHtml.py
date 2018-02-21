import re
fileC = open("color.c","r")
stringC = fileC.read()
fileC.close()

stringC = re.sub("&","&amp;",stringC);
stringC = re.sub("<","&lt;",stringC);
stringC = re.sub(">","&gt;",stringC);
stringC = re.sub("\n","<br>\n",stringC);
#stringC = re.sub("(.*)\n","<div class=\"codeLine\"> \\1 </div>\n",stringC)
stringC = re.sub("(?<!class=)(?!\">)(\".*\")","<span class=\"string\">\\1</span>",stringC)
stringC = re.sub("([\n\s\*\(\{])(int|double|char|FILE)([\n\s\)])","\\1<span class=\"declare\">\\2</span>\\3",stringC)
stringC = re.sub("([\n\s\*\(\{\)])(for|if|else|fprintf|printf|sizeof|(?:seabreeze_[a-zA-Z0-9_]*[a-zA-Z0-9]))([\n\s\(])","\\1<span class=\"reserved\">\\2</span>\\3",stringC)
print(stringC)


fileHTML = open("color.html","w");

fileHTML.write("<meta  charset=\"utf-8\"><link rel=\"stylesheet\" href=\"css/code.css\">\n<code>"+stringC+"</code>");
fileHTML.close();
