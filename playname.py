'''PROGRAM TO RENAME THE UNORDERED DOWNLOADED YOUTUBE PLAYLIST FILES ACCORDING TO THE SEQUENCE OF THE PLAYLIST'''
import HTMLParser
import os
import urllib2
from bs4 import BeautifulSoup
url = raw_input("Enter the youtube playlist Url: ")
#url = 'https://www.youtube.com/playlist?list=PLx5CT0AzDJCnxcudBsfZlB5joMjEBSOKi'
def Print(l):
	if len(l) == 0:
		print "EMPTY"
		return 0
	for _ in l:
		print _,str(len(_))
try:
	soup = BeautifulSoup(urllib2.urlopen(url))
except :
	print "Oops Network Error!!\nKindly check your internet connection and re-run"
	exit()

ols = list()
uls = list()
s = set()


oo=''
for link in soup.find_all('tr'):
    oo = link.get('data-title')
    ols.append(oo+'.mp4')



p = './folder'
uls= os.listdir('./folder')

faulty_words = list()
index = -22
for a in uls:
	new = str(HTMLParser.HTMLParser().unescape(a))
	try:
		#new = new.replace('-',':',1)
		#print new,len(new)
		index = ols.index(new)
		#new = new.replace(':','-',1)
		new_word = str(index+1) + ' ' + new
		os.rename(os.path.join(p,a),os.path.join(p,new_word))
	except Exception, e:
		faulty_words.append(a)
		print str(e)
		pass

if len(faulty_words):
	print "Following are the list of the words that could not be renamed:"
	Print(faulty_words)
print str(len(ols)-len(faulty_words)-1),'File(s) renamed'
print "Done"

