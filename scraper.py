# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
import scraperwiki
import lxml.html
import requests

html = requests.get("http://bechdeltest.com/?list=all").text
root = lxml.html.fromstring(html)
data = {
 'MovieId' : [movieID.attrib['id'] for movieid in root.cssselect("div[class='movie'] a"),'Movie' : [title.text_content().encode('utf-8')] for title in root.cssselect("div[class='movie'] a"),
 }
scraperwiki.sqlite.save(unique_keys = ['MovieId'], data=data)
#for el in root.cssselect("div[class='movie'] a"):
 #title = el.text_content().encode('utf-8')
 #print title
#data = {
 # 'Title' : [title.text_content() for title in root.cssselect("div[class= 'movie'] a ")][2]
  
#scraperwiki.sqlite.save(unique_keys = ['Product'], data=data)

#for el in root.cssselect("div[class='movie'] a"):
#testsPassed = root.cssselect("//div[@class='movie']/a[1]/img/@alt")
#testComment = root.cssselect("//div[@class='movie']/a[2]/img/@title")
#bechdelUrl = root.cssselect("//div[@class='movie']/a[2]/@href")
#imdbUrl = root.cssselect("//div[@class='movie']/a[1]/@href)")
#movieId = root.cssselect("//div[@class='movie']/a[2]/@id)")

# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['movieID'], data={"Movie Title" : title, "Tests Passed" : testsPassed, "Test Passed Details" : testComment, "Profile" : bechdelUrl, "IMDb Link" : imdbUrl})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
