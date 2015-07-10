import scraperwiki
import lxml.html
import requests

html = requests.get("http://bechdeltest.com/?list=all").text
root = lxml.html.fromstring(html)
movieList = ["http://bechdeltest.com"+link.get('href') for link in root.cssselect("div[class='movie'] a:nth-of-type(3)")]

for link in movieList:
 htmlMovie = requests.get(link).text
 rootMovie = lxml.html.fromstring(htmlMovie)
 movieID = link.split("/")[4]
 title = rootMovie.cssselect("h2 a text()")
 print title
 break
 #movieTitle = 
 #year = 
 #result =
 #pass =
 #amovie.attrib['id']each link, get:
#Movie Title
#Movie ID
#Year
#IMDB link
#Pass or Fail
#Number of tests passed
#Description of outcome
#Dubious?
#MovieLink

#for movie in movieList:
# movieID = movie.attrib['id']
# title = movie.text_content().encode('utf-8')
 #imdbUrl = movie.attrib['href'] [0]
 #passed = movieList.cssselect( "img").attrib['alt']
 #passInfo = movieList.cssselect( "img").attrib['title']
 #link = movie.attrib['href'] [1]
 #data = {
  #'movieID': movieID,
  #'Title': title,
  #'IMDb Profile': imdbUrl,
  #'Number of Criteria Passed': passed,
  #'Details on Criteria Passed': passInfo,
  #'Source and Discussion': link
  #}
 #scraperwiki.sqlite.save(unique_keys = ['movieID'], data=data)
 #print data

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
