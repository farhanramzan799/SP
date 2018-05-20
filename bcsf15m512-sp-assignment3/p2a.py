#!usr/bin/python

import requests
from bs4 import BeautifulSoup

def getCategories(URL):
	if(URL !=""):
		try:
			
			wor=raw_input("Enter the word you want to search : ")			
			status=requests.get(URL)

			if(status.status_code == 200):
				parser_object = BeautifulSoup	(status.content,"html.parser")
			div_tag_list = parser_object.find_all('div',{'class':'mobile-nav'})
			for div in div_tag_list:
				li_tag = div.find_all('li',{'id':'menu-item-174055'})
				for li in li_tag:
					a_tag = li.find_all('a')
					for a in a_tag:
						
						URL=(a['href'])
						#print URL						
						print("________________")
						
						for c in range(5):
							print "page : ",c+1
							status=requests.get(URL)	
							if(status.status_code == 200):
								parser_object = BeautifulSoup(status.content,"html.parser")	
							
								p_tag_list = parser_object.find_all("p")
								stringList_from_p_tags = []
								p_content = ""
								for p in p_tag_list:
								
									p_content = p_content + str(p.text.encode('utf-8').strip())
								
									a_tag = p.find_all('a')
									for a in a_tag:
										if wor in p_content:
											print(a['href'])
										else:
											print " "

								div_tag_list = parser_object.find_all('div',{'id':'primary'})
								for div in div_tag_list:
									li_tag = div.find_all('li',{"class":"page-item"})
									for li in li_tag:
										a_tag = li.find_all('a',{'class':'page-link'})
										for a in a_tag:
											URL=(a['href'])
											

		
		except requests.ConnectionError:
			print ("Error.")


#__________________________#
def main():
	URL = "https://propakistani.pk/"

	getCategories(URL)

#___________________________#

if __name__ == "__main__":
	main()


