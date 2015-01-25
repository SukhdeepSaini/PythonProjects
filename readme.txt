Instructions: FOR WEB CRAWLER AND PAGE RANKER

==========================================================================================
WEB CRAWLWER:

I developed this web crawler to perform focussed\Unfocussed crawling of web.

Input: Seed , Keyphrase

Seed: The seed from where to start Crawling
Keyphrase (Optional) : The key to search on a web page

Output: Links crawled up to depth 3 from the seed

If a key phrase is provided along with the seed to the program then it will only crawl those pages that have that key phrase present on it otherwise it will perform unfocussed crawling.
 
In both the cases the crawling is performed till depth 3 from the seed.

==========================================================================================
Compile And Run:

Source Code File: WebCrawler.pyPython Interpreter: Python2.7.5External Library Used: BeautifulSoupUse the python interpreter to compile and run the program as shown below:Python WebCrawler.py “seed” “Keyphrase”Or Python WebCrawler.py “seed”

Output: The program will start running and you can check its progress in the console as it is running. After the program is completed the output is displayed in the console and a file named “result” is also generated which contains the output.PAGE RANKER:======================================================================================
Source Code And Input File:

The source Code of the program is present in MyFirstRanker.py file. I have added the wt2g_inlinks.txt file to the repository which was is the input to the page ranking program.

======================================================================================
Instructions to Compile and Run:

The source code is written and interpreted in Python 2.7.5

Use the Below mentioned command to run the program:

python MyFirstRanker.py <NAME OF FILE>

Example:
python MyFirstRanker.py "wt2g_inlinks.txt”

Note: In case you will not provide the name of the file as an input then the program will run performing iterative calculation of page rank using the Test.txt file present in the repository. The Test.txt is the graph with fever number of pages.

python MyFirstRanker.py
