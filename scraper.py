import scraperwiki
import lxml.html
import requests
import json
import urllib

html = requests.get("http://bechdeltest.com/?list=all").text
root = lxml.html.fromstring(html)
movieList = ["http://bechdeltest.com"+link.get('href') for link in root.cssselect("div[class='movie'] a:nth-of-type(3)")]

for link in movieList:
 htmlMovie = requests.get(link).text
 rootMovie = lxml.html.fromstring(htmlMovie)
#Basic Movie Info
 title = rootMovie.cssselect("h2 a:nth-of-type(1)")[0].text_content()
 year = title.split(' ')[-1].replace('(','').replace(')','')
#Bechdel Test Result
 criteriaPassed = rootMovie.cssselect("h2 img")[0].get('alt').replace('[[',"").replace(']]','')
 if criteriaPassed == "3":
  passedTest = "Yes"
  two_women = "Yes"
  women_talk = "Yes"
  women_talk_no_men = "Yes"
  statusDetails = "Two or more named women characters, they talk to each other about something other than a man"
 if criteriaPassed == "2":
  passedTest = "No"
  two_women = "Yes"
  women_talk = "Yes"
  women_talk_no_men = "No"
  statusDetails = "Two or more named women characters, they only talk to each other about men"
 if criteriaPassed == "1":
  passedTest = "No"
  two_women = "Yes"
  women_talk = "No"
  women_talk_no_men = "No"
  statusDetails = "Two or more named women characters, they don't talk to each other"
 if criteriaPassed == "0":
  passedTest = "No"
  two_women = "No"
  women_talk = "No"
  women_talk_no_men = "No"
  statusDetails = "Less than two named women characters"
 if '(although dubious).' in rootMovie.cssselect("p")[0].text_content():
  clarity = "Dubious"
 else:
  clarity = "Not Dubious"
 movieID = link.split("/")[4]
 sourceUrl = link
 imdbUrl = rootMovie.cssselect("h2 a")[0].get('href')
 imdbID = imdbUrl.split('title/')[1].replace('/','')
 omdbUrl = "http://www.omdbapi.com/?i="+imdbID
#Omdb Data
 response = urllib.urlopen(omdbUrl)
 omdbData = json.loads(response.read())
 poster = omdbData['Poster']
 release = omdbData['Release']
 genre = omdbData['Genre']
 director = omdbData['Director']
 runtime = omdbData['Runtime']
 plot = omdbData['Plot']
 country = omdbData['Country']
 imdbRating = omdbData['imdbRating']
 imdbVotes = omdbData['Votes']
 print poster,release,genre,director,runtime,plot,country,imdbRating,imdbVotes
 break
 break
#Write to Database

