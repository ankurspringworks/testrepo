import os
#from playname import Print
p = './folder'
def Print(l,beg=0,end=2):
	le = len(l)
	end = le
	if le == 0:
		print "EMPTY"
		return 0
	for _ in range(beg,end):
		print l[_],str(len(l[_]))
		
renamed_count = 0
l = os.listdir(p)
for a in l:
	a.lstrip()
	if a[0].isdigit():
		ls = a.split(' ')
		ls = ls[1:]
		ls = ' '.join(ls)
		try:
			os.rename(os.path.join(p,a),os.path.join(p,ls))
			renamed_count+=1
		except Exception, e:
			raise e
	else :
		#print a.split(' ')
		continue
print "Done"
print str(renamed_count),'File(s) renamed'
