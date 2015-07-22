import scraperwiki
import lxml.html
import requests
import json
import urllib

html = requests.get("http://bechdeltest.com/?list=all").text
root = lxml.html.fromstring(html)
movieList = ["http://bechdeltest.com"+link.get('href') for link in root.cssselect("div[class='movie'] a:nth-of-type(2)")]
rows_scraped = 0
number_movies = len(movieList)
for link in movieList:
 htmlMovie = requests.get(link).text
 rootMovie = lxml.html.fromstring(htmlMovie)
#Basic Movie Info
 title = rootMovie.cssselect("h2 a:nth-of-type(1)")[0].text_content().strip()
 year = title.split(' ')[-1].replace('(','').replace(')','')
#Bechdel Test Result
 criteria_passed = rootMovie.cssselect("h2 img")[0].get('alt').replace('[[',"").replace(']]','')
 if criteria_passed == "3":
  passed_test = "Yes"
  two_women = "Yes"
  women_talk = "Yes"
  women_talk_no_men = "Yes"
  status_details = "Two or more named women characters, they talk to each other about something other than a man"
 if criteria_passed == "2":
  passed_test = "No"
  two_women = "Yes"
  women_talk = "Yes"
  women_talk_no_men = "No"
  status_details = "Two or more named women characters, they only talk to each other about men"
 if criteria_passed == "1":
  passed_test = "No"
  two_women = "Yes"
  women_talk = "No"
  women_talk_no_men = "No"
  status_details = "Two or more named women characters, they don't talk to each other"
 if criteria_passed == "0":
  passed_test = "No"
  two_women = "No"
  women_talk = "No"
  women_talk_no_men = "No"
  status_details = "Less than two named women characters"
 if '(although dubious).' in rootMovie.cssselect("p")[0].text_content():
  clarity = "Dubious"
 else:
  clarity = "Not Dubious"
 date_added = rootMovie.cssselect("p")[0].text_content().split(' on ')[1].split(' ')[0]
 movie_id = link.split("/")[4]
 source_url = link
 imdb_url = rootMovie.cssselect("h2 a")[0].get('href')
 imdb_id = imdb_url.split('title/')[1].replace('/','')
 omdb_url = "http://www.omdbapi.com/?i="+imdb_id
#Omdb Data
 response = urllib.urlopen(omdb_url)
 omdb_data = json.loads(response.read())
 if 'Poster' in omdb_data:
   poster = omdb_data['Poster']
 else:
  poster = ''
 if 'Released' in omdb_data:
  release = omdb_data['Released']
 else:
  release = ''
 if 'Genre' in omdb_data:
  genre = omdb_data['Genre']
 else:
  genre = ''
 if 'Director' in omdb_data:
  director = omdb_data['Director']
 else:
  director = ''
 if 'Runtime' in omdb_data:
  runtime = omdb_data['Runtime'].split(' min')[0]
 else:
  runtime = ''
 if 'Plot' in omdb_data:
  plot = omdb_data['Plot']
 else:
  plot = ''
 if 'Country' in omdb_data:
  if omdb_data['Country'] == "Federal Republic of Yugoslavia":
   county = "Yugoslavia"
  else:
   country = omdb_data['Country']
 else:
  country = ''
 if 'Actors' in omdb_data:
  actors = omdb_data['Actors']
 else:
  actors = ''
 if 'Awards' in omdb_data:
  awards = omdb_data['Awards']
 else:
  awards = ''
 if 'imdbRating' in omdb_data:
  imdb_rating = omdb_data['imdbRating']
 else:
  imdb_rating = ''
 if 'imdbVotes' in omdb_data:
  imdb_votes = omdb_data['imdbVotes']
 else:
  imdb_votes = ''
 if imdb_votes:
  popularity = round(float(imdb_votes)*float(imdb_rating),2)
 print popularity
#IMDb Data: Producer and Keywords
 htmlIMDB = requests.get(imdb_url).text
 rootIMDB = lxml.html.fromstring(htmlIMDB)
 keywords = rootIMDB.cssselect("span[itemprop='keywords'").text_content().strip()
 print keywords
 break

#Write to Database
 data = {
  'Movie' : title,
  'Passes Bechdel Test' : passed_test,
  'Criteria Passed' : criteria_passed,
  'Clarity of Outcome' : clarity,
  'Outcome Details' : status_details,
  'Has at Least Two Named Women' : two_women,
  'Women Talk to Each Other, But Only About Men' : women_talk,
  'Women Talk To Each Other About Something Other Than Men' : women_talk_no_men,
  'Date Bechdel Result Added' : date_added,
  'Year Released' : year,
  'Date Released': release,
  'Movie Poster' : poster,
  'Genre' : genre,
  'Director' : director,
  'Main Actors' : actors,
  'Runtime (min)' : runtime,
  'Plot' : plot,
  'Country' : country,
  'IMDb Rating' : imdb_rating,
  'IMDb Votes' : imdb_votes,
  'Source on Bechdel Test' : source_url,
  'IMDb Profile' : imdb_url,
  'API Source' : omdb_url,
  }
#Save to Database
 scraperwiki.sqlite.save(unique_keys=["source on Bechdel Test"], data=data)
 rows_scraped = rows_scraped+1
 data = {}
 progress = round((float(rows_scraped)/float(number_movies)),2)
 print "Saved "+str(rows_scraped)+" / "+str(number_movies)+" movies ---> Process: "+str(progress)+"%"
#Result
print "You are awesome, you saved all movies!"
