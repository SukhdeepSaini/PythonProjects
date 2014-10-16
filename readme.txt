Instructions:

==========================================================================================
Web Crawler: 

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

Output: The program will start running and you can check its progress in the console as it is running. After the program is completed the output is displayed in the console and a file named “result” is also generated which contains the output.