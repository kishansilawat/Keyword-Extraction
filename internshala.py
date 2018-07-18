import PyPDF2

pdfObj=open('JavaBasics-notes.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfObj)
numPages=pdfReader.numPages
Text=''
for i in range(numPages):
	PageObj=pdfReader.getPage(i)
	Text=Text+PageObj.extractText()

from nltk.corpus import stopwords

stop_words=stopwords.words('english')

import re

words=re.findall("[a-z]+", Text.lower())
temp=re.findall("[a-z]", Text.lower())
for t in temp:
	if t not in stop_words:
		stop_words.append(t)

keywords=[]
for word in words:
	if word not in stop_words:
		if word not in keywords:
			keywords.append(word)
counter={}
for keyword in keywords:
	count=Text.count(keyword)
	counter[keyword]=count

for keyword in keywords:
	if counter[keyword]==0:
		del counter[keyword]

	
import pandas as pd

keyword_count=pd.DataFrame(counter,index=[0])