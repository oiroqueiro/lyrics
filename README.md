<h1 style="text-align: center;">Lyrics</h1>
<h2 style="text-align: center;">Mid-Bootcamp Project</h2>
This is the project what I created for my Mid-Bootcamp project in [IronHack](http://www.ironhack.com).

I had some requeriments and restrictions like:

-  Collect the data by myself (cannot download datasets)
- The dataset should have between 30 and 100 observations (rows) and 5 to 10 features (columns)
- I could enrich the dataset with more information obtained with other methods than manual typing (for example, web scraping)
- Need to complete one analysis to answer the questions that I have to solve with this project, also I should supplement the analysis with some hypothesis.

## My project
My questions were about the lyrics of the songs that we use to listen everyday, these question are:

- Do the lyrics have an overall positive sentiment?
- Are women's lyrics more positive than men's
- Are pop's lyrics than hip hop's?

## My solution
### Python:

- Creation of the dataset using python: I decided to collect information from [Spotify Charts](https://charts.spotify.com/) because I wanted to analyze lyrics globally, so I chose the top artist of the week 47 of year 2022. The process I followed was type in a file the artist of that chart and also used [Last.fm](https://www.last.fm/) to type more information like gender, main genre and if is a band.

  Then I complete the dataset searching the 10 most popular songs of every artist in [Spotify](https://open.spotify.com/) using their API.

  After that I used the __lyricsgenius__ library to connect to the website [Genius](https://genius.com/) to download 5 lyrics of the 10 most popular songs in Spotify of every artist (because the name of the songs in Spotify not always has a corresponding name in Genius). At this point I also created one function with Selenium to get the connection token, just in case that the token to connect to Genius change. Right now is stored in a file (secrets.txt) but could get it without store it.

- Once I downloaded all the information, needed to make a treatment to do the sentiment analysis (using the library [__Flair__](https://github.com/flairNLP/flair)) and natural language processing ([__NLTK__](https://www.nltk.org/)).

- Since in the list of songs were used different languages, I decided to translate all to english to simplify the analysis. For this I used the library [__Fasttext__](https://fasttext.cc/) with their pre-trained model to detect the language of the lyrics and then translate them to english with the library [__translators__](https://github.com/uliontse/translators) which if cannot do the translation uses google translator to perform the work.

- I calculated the top words with NLTK functions and update manually their stop words list to include more that where not interesting to my analysis.

- I also created a function to generate one word cloud with the library __wordcloud__ and __PIL__ to show different with shapes that I downloaded.

- In another jupyter notebook I developed the hypothesis analysis and prepared the dataset to the visual analysis with [Tableau](https://public.tableau.com/)

### Tableau

I used Tableau in his public version to create the presentation of the project and the visual analysis of the project, can find in in [__my Tableau__](https://public.tableau.com/app/profile/.scar.iglesias.roqueiro/viz/Mid-BootcampProject_16711135428210/Lyrics)

### Flask
The project include a demo in flask that allows to search a song of one artist and will show the lyrics translated with the sentiment analysis and one wordcloud.