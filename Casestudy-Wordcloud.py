import re
import numpy as np
from wordcloud import WordCloud,STOPWORDS
import pandas as pd
from PIL import Image
text=open("SteveJobsSpeech.txt","r",encoding="utf8").read()
text=text.replace("’","")
text=re.sub(r"[^A-Z a-z]"," ",text)
a=re.split(r" |\n",text)
wordlist=[]
for x in a:
    if x!='':
        wordlist.append(x)
wordlist=np.array(wordlist)
wordlist=list(map(lambda x:x.capitalize(),wordlist))
uniwords,frequency=np.unique(wordlist,return_counts=True)
Table={}
for i in range(len(uniwords)):
    Table[uniwords[i]]=frequency[i]
sortedkeys=sorted(Table,key=Table.get,reverse=True)
sortedTable={}
for i in sortedkeys:
    if i.lower() in STOPWORDS:
        pass
    else:
        sortedTable[i]=Table[i]
Table=sortedTable
pd.set_option("display.max_columns",None)
print(pd.DataFrame(Table,index=[0]))
print("Number of words = ",len(Table.keys()))
k=int(input("Enter number of words to be in the wordcloud : "))
print("shape of wordcloud:\n\t1 for dolphin\n\t2 for dragon\n\t3 for apple")
n=int(input("Enter option : "))
if n==1:
    mask=np.array(Image.open("Dolphin.png"))
elif n==2:
    mask=np.array(Image.open("Dragon.png"))
elif n==3:
    mask=np.array(Image.open("Apple.png"))
else:mask=None
#mask=np.array(Image.open("Dragon.png"))
wc=WordCloud(
    background_color="white",
    mask=mask,
    max_words=k,
    normalize_plurals=False,).generate_from_frequencies(Table)
wc.to_file("output_wordcloud.png")
img=Image.open('output_wordcloud.png')
img.show()


