'''
Created on Oct 7, 2014
@author: Sukhdeep Saini
'''

import math
import sys
    
#Total number of pages present in the file
TotalPages = {}

#A Dictionary for the number of inlinks for a particular page key is page and value is list of inlinks
Inlinks = {}

#A Dictionary for the count of number of inlinks for a particular page key is page and value is list of count of the number of inlinks for that page
InlinkCount = {}

#A Dictionary to keep track of the outlink for a particular page key is the page and the value is the count of outlinks
OutLinks = {}

#A list of pages with no outlinks
SinkPages = []

#A Dictionary to keep track of the pagerank for a page , key is the page and value is the pagerank for that page
PageRank = {}

#Dictionary to keep track of the new pagerank calculated for the pages in the file 
NewPageRank = {}

#List containing the perplexity values
Perplexity = []

#A list for the perplexity to display in output
PerplexityOutPut =[]
#Constant for the perplexity
PERPLEXITYCONSTANT = 4

#Damping factor
d = 0.85

#Read the input file
def ReadInputFile(inputfile):
    with open(inputfile) as f:
        for line in f:
            line = line.rstrip('\n') #remove the \n character from the end of line         
            pages = line.split()     #split pages at space
            p = pages.pop(0)         #Get the first page 
            CalculateInLinks(p,pages)

        
#Process the pages and determine the values of inlinks and outlinks for pages
def CalculateInLinks(page,pages):
    global TotalPages        
    TotalPages[page] = 0
    #pages = set(pages)
    if len(pages) > 0: #check to see if there are inlinks for  a page
        Inlinks[page] =  pages
        InlinkCount[page] = len(pages) # Store the count for the inlinks
    else:
        InlinkCount[page] = 0

#Calculate the Number of Outlinks for a particular link
def ProcessOutlinks():
    global Inlinks
    for p in Inlinks:
        links = Inlinks[p]
        for link in links:
            OutLinks[link] = 0
        
#Helper function for Calculating the outlinks for a page
def CalculateOutLinks():
    global OutLinks,Inlinks
    for p in Inlinks:
        links = Inlinks[p]
        for link in links:
            OutLinks[link] = OutLinks[link] + 1
    
#Calculate the number of Sink pages
def CalculateSinkPages():
    global SinkPages
    SinkPages = set(TotalPages.keys()) - set(OutLinks.keys())
    
#Compute the page rank as per the given algorithm
def CalculatePageRank():
    global PageRank, TotalPages , OutLinks
    LenTotalPages =  float(len(TotalPages))
    if not PageRank:
        for page,value in TotalPages.iteritems():
            PageRank[page] = float(1/LenTotalPages)
    while not ConvergenceChecker():
        sinkPageRank = 0
        for page in SinkPages:                                       
            sinkPageRank += PageRank[page]
        for page in TotalPages:
            NewPageRank[page] = (1.0 - d) / LenTotalPages
            NewPageRank[page] += (d * sinkPageRank) / LenTotalPages                            
            if page in Inlinks:
                inlist = Inlinks[page]           
                for inPage in inlist:    
                        NewPageRank[page] += d * PageRank[inPage] / OutLinks[inPage]          
        for newPage in TotalPages:
            PageRank[newPage] = NewPageRank[newPage]
            
            
#calculate the page rank iteratively            
def CalculatePageRankIteratively():
    global PageRank, TotalPages
    LenTotalPages =  float(len(TotalPages))
    i = 1      
    while i <= 100:
        if not PageRank:
            for page,value in TotalPages.iteritems():
                PageRank[page] = float(1/LenTotalPages)
        sinkPageRank = 0
        for page in SinkPages:                                       
            sinkPageRank += PageRank[page]
        for page in TotalPages:
            NewPageRank[page] = (1.0 - d) / LenTotalPages
            NewPageRank[page] += (d * sinkPageRank) / LenTotalPages                            
            if page in Inlinks:
                inlist = Inlinks[page]           
                for inPage in inlist:      
                    NewPageRank[page] += d * PageRank[inPage] / OutLinks[inPage]          
        for newPage in TotalPages:
            PageRank[newPage] = NewPageRank[newPage]
        if i==1 or i==10 or i == 100:
            print("After iteration {} the page rank for page 'A' is {}".format(i,float(PageRank['A'])))
            print("After iteration {} the page rank for page 'B' is {}".format(i,float(PageRank['B'])))
            print("After iteration {} the page rank for page 'C' is {}".format(i,float(PageRank['C'])))
            print("After iteration {} the page rank for page 'D' is {}".format(i,float(PageRank['D'])))
            print("After iteration {} the page rank for page 'E' is {}".format(i,float(PageRank['E'])))
            print("After iteration {} the page rank for page 'F' is {}".format(i,float(PageRank['F'])))
            print("=============================NEXT ITERATION=======================================")
        i = i+1

#Check if the Convergence is achieved or not , function to check the convergence
def ConvergenceChecker():   
    lengthPrep = len(Perplexity)
    Perplexity.append(PerplexityCalclator())
    if lengthPrep < PERPLEXITYCONSTANT:
        return False 
    if (Perplexity[-1] == Perplexity[-2]) and (math.fabs(Perplexity[-2] == Perplexity[-3])) and (math.fabs(Perplexity[-3] == Perplexity[-4])):
        return True
    return False

#Function to Calculate the perplexity value
def PerplexityCalclator():
    global TotalPages, PageRank , InlinkCount
    entropyValue = 0
    for page,value in TotalPages.iteritems(): 
        entropyValue += PageRank[page] * math.log(PageRank[page],2)
    PerplexityValue = math.pow(2,-entropyValue)
    PerplexityOutPut.append(PerplexityValue)
    return int(PerplexityValue)

#Sort the page rank and print
def PrintPageRankAfterSorting():
    PageRankAfterSorting = sorted(PageRank.items(), key=lambda x: x[1], reverse = True)
    print('Sorted Top 50 pages according to there page ranks')
    x = 0
    while(x < 50):
        print("{} : {}".format(str(x),str(PageRankAfterSorting[(x)])))
        x += 1

#Sort the Inlins and print
def PrintInlinksAfterSorting():
    InLinksAfterSorting = sorted(Inlinks,key = lambda x : len(Inlinks[x]), reverse = True)
    x = 0
    print('Sorted Top 50 pages according to there InLinks count')
    while(x < 50):
        print("Index {} : Page = {} having In Links Count = {}".format(str(x),str([InLinksAfterSorting[(x)]]),str(len(Inlinks[InLinksAfterSorting[(x)]]))))
        x += 1

#Print the values of the calculated perplexities
def PrintPerplexity():
    global PerplexityOutPut
    for index,prep in enumerate(PerplexityOutPut):
        print("Index is {} and Calculated Perplexity is {}".format(str(index),str(prep)))

#Clear the existing data for the iterative page ranker
def ClearIterativeDataFromDataStructures():
    TotalPages.clear()
    Inlinks.clear()
    InlinkCount.clear()
    PageRank.clear()
    NewPageRank.clear()
    OutLinks.clear()
    SinkPages = []
    
#Calculate the iterative page rank for 1 , 10 and 100 iterations
def CalculateIterativePageRank(InputfileName):    
    ReadInputFile(InputfileName)
    ProcessOutlinks()
    CalculateOutLinks()
    CalculateSinkPages()
    CalculatePageRankIteratively()
    ClearIterativeDataFromDataStructures()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        inputFile = sys.argv[1] 
        try: 
            ReadInputFile(inputFile)
            ProcessOutlinks()
            CalculateOutLinks()
            CalculateSinkPages()
            CalculatePageRank()
            print("Total Pages = {} , Inlinks Length = {} , OutLinks Length = {} , Sink Pages Length = {}".format(len(TotalPages),len(Inlinks),len(OutLinks),len(SinkPages)))
            PrintPageRankAfterSorting()
            PrintInlinksAfterSorting()
            print("Please see below the perplexity values")
            PrintPerplexity()                        
        except:
            print("HINT : IF no file is provided as input then the program will run iteratively for small graph other wise it will run till Convergence")       
    else:
        print("You have not provided any file name so Starting the Iterative Page Rank Algorithm")
        CalculateIterativePageRank("Test.txt")





    
    

