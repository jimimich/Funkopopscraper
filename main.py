from bs4 import BeautifulSoup

with open('home.html', 'r') as htmlFile:
    
    content = htmlFile.read()
    #print(content)
    
s = BeautifulSoup(content, 'lxml')

s.prettify()
#print(s.prettify())

                #Underscore after class to understand it's HTML tag
#tags = s.find_all('Title', class_ = 'sp_desktop_sponsored_label')
title = s.find_all('title')

if(str(title).__contains__('LeetCode')):
    print(title)
    

print(str(title))
#for tag in tags:
#    print(tag.h2.text)
