import os
import sys
import re
import argparse
import errno
import requests
import urllib2
import datetime
from bs4 import BeautifulSoup


def parse_url(url):
    	
	links = []
  	try:
		get_html = requests.get(url)
		soup = BeautifulSoup(get_html.text, 'html.parser')
		for link in soup.findAll('a'):
			try:
				if not os.path.isdir(link['href']):
		    			os.makedirs(link['href'])
		    			print "%s created!" % link['href']
	    		except OSError as e:
				if e.errno == errno.EEXIST and os.path.isdir(link['href']):
		    			pass
	       			else:
		    			print "Error: {}".format(e)
		    			sys.exit(1)
			links.append(url+link['href'])
    	except requests.exceptions.RequestException as e:
        	print "Error detected: {}".format(e)
        	sys.exit(1)

    	return links

def get_mp3(urls):
    
    	''' Actually download .mp3 file'''
	count_qari=-1
	for url2 in urls:
		count_qari=count_qari+1
	
	
	file=open("log.txt","w")
	file.write(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
	file.write(" Total Qari: {0} \n".format(count_qari))
	count_rec=0
    	for url1 in urls:
		mp3=[]
		get_html = requests.get(url1)
		soup = BeautifulSoup(get_html.text, 'html.parser')
		count_rec=count_rec+1
		qari_name=url1.split('/')[-2]
		print url1
		print "qari name: {0} ".format(qari_name)
			
		file.write(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
		file.write(" Start processing {0} out of {1} \n".format(count_rec,count_qari))
		file.write(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
		file.write(" Start processing {0}\n".format(qari_name))
		for link in soup.findAll('a'):
			print link['href']
			if link['href'] != '../':
				mp3.append(url1+link['href'])
	
		
		for url in mp3[-2:]:
			dir_name=url.split('/')[-2]
			print dir_name
			count=0
			try:
				os.chdir(dir_name)
				count=count+1

			except OSError as e:
				print "directory not found" 
			os.system("pwd")
			if count!=0:
				usock=urllib2.urlopen(url)
				file_name=url.split('/')[-1]
				if(file_name!=''):
					
					file.write(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
					file.write(" {0} {1} Start\n".format(dir_name,file_name))
					
					f=open(file_name,'wb')
					file_size=int(usock.info().getheaders("Content-Length")[0])
					print "Downloading %s Bytes:%s" %(file_name,file_size)
					downloaded=0
					block_size=8192
					while True:				
						buff=usock.read(block_size)
						
						if not buff:
							break

						downloaded=downloaded + len(buff)
						
						f.write(buff)
						downloaded_status= r"%3.2f%%" % (downloaded*100.00/file_size)
						downloaded_status=downloaded_status+((downloaded)+1)*chr(8)
						print downloaded_status,"done"
					f.close()
					file.write(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
					file.write(" {0} {1} END\n".format(dir_name,file_name))
	
			if count!=0:
				var1="???.mp3"
				var2="second_half.mp3"
				cmd="cat {0}>{1}".format(var1,var2)
				os.system(cmd)
				os.chdir("..")
		file.write(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))
		file.write(" Merging files of {0} \n".format(qari_name))
	file.close()
		
		
		
	
			

if __name__=='__main__':
	url='https://download.quranicaudio.com/quran/'
	urls=[]
	urls=parse_url(url)
	for link in urls:
		print link
	get_mp3(urls)
