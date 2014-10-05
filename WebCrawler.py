'''
Created on Sep 5, 2014

@author: sukhdeepsaini
'''

from bs4 import BeautifulSoup
import urllib2
import re
import sys
import time


set_of_links = ()  #set of crawled links


def Crawler(seed,Keyphrase):
    url = "/wiki/" #pattern with which the link should start
    colon = ":"    #Link to Crawl should not have : in it
    mainPage = "/wiki/Main_Page" #We should not be following links to Main_Page
    urlPrefix = "http://en.wikipedia.org" #Prefix to add to the link to be crawled
    pat = re.compile(re.escape(url)) #String Pattern with which the link href should Start
    queue_links = [seed] #keep track of all the unique links to crawl
    visited  = set(seed)  #all the links that we have visited and we should not visit again
    depth = 0 #depth to measure for the breadth first search algorithm
    Inactive = [] #inactive list of links to keep track of neighbours of a link
    crawled = set() #links which are crawled having the Keyphrase
    allLinks = []
    pattern1 = re.compile(Keyphrase, re.IGNORECASE) #to perform case insensitive search
    
    while len(queue_links) > 0 and depth <= 2:
        try:
            '''
            get the url at the 0th position and start crawling
            '''
            time.sleep(1)
            htmltext = urllib2.urlopen(queue_links[0]).read() #Get the element at the front of the queue i.e. 0th place
        except:
            print("Not Able to Open the the following URL",queue_links[0])
        documentObject = BeautifulSoup(htmltext) #returns the document as an object
        canonicalLink = documentObject.find("link", rel = "canonical")
        canonicalHref = canonicalLink['href']  #canonical href of the link
        decodedPage = documentObject.get_text()
        
        if Keyphrase != "" and pattern1.search(decodedPage) is None:
            print("The URL {} is not having the keyphrase".format(queue_links[0]))
            queue_links.pop(0) # remove the element from the list if keyphrase is not present and continue to next one
            allLinks.append(canonicalHref)
            if len(queue_links) != 0: #if last link is not having the keyphrase it is stopping further len is zero of queue_links
                continue   #fix this problem of length zero for queue
            if len(queue_links) == 0:  #if depth is not reached and last link is opened and is not having the keyphrase
                queue_links, Inactive = Inactive ,queue_links
                depth += 1
                continue
        queue_links.pop(0) #remove the URL from the list after we have visited it
        crawled.add(canonicalHref)  #The links which we have opened to check for other links
        allLinks.append(canonicalHref)
        print("length is {} and popped is {}".format(len(queue_links),canonicalHref))
        links = documentObject.findAll('a',href= True) #get all the links from the current document
        for link in links:
            href = link['href']
            if pat.match(href) and colon not in href and mainPage not in href:
                newHref = urlPrefix + href;
                #newfile = open("AllLinks","a")
                if "#" in newHref:
                    newHref = newHref.split("#")[0]  #get the first part of the url before #
                if newHref not in visited:
                    visited.add(newHref)
                    Inactive.append(newHref)
                    #newfile.write("Link = {} \n".format(newHref))
        if len(queue_links) == 0: #swap the content of the active and non active queues when active is empty
            queue_links, Inactive = Inactive ,queue_links
            depth += 1
            print("Current Depth is {} and length of queue_links is {} and visited is {}".format(depth,len(queue_links),len(allLinks)))      #invariant to measure the depth of traversal
                   
    return set(crawled)  #Set of links having the keyphrase

    
#enumerating the set of links
if __name__ == "__main__":
    length = len(sys.argv)
    if length == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    else:
        arg1 = sys.argv[1]
        arg2 = ""
    set_of_links = Crawler(arg1,arg2)
    print("\n\n Please see below the links Which are crawled")
    f = open("result","a")
    for index,link in enumerate(set_of_links):
        print("Index = {} having link {} \n".format(index,link))
        f.write("Index = {} having link {} \n".format(index,link))
        

 
 

    
    




