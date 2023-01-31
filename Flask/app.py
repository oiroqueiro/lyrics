from flask import Flask, render_template, request
from libraries.Dataset import get_lyrics_from_genius
from libraries.Dataset import fasttext_detect_language
from libraries.Dataset import translate_lyrics
from libraries.Dataset import calculate_sentiment
from libraries.Dataset import get_top_words
from libraries.Dataset import get_word_cloud

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():    
    
    if request.method == "GET":

        lyricsresult = ''
        langresult = ''
        sentimentresult = ''
        topwordsresult = ''
        wordcloudresult = 0
        
        return render_template('mainpage.html', lyrics=lyricsresult, language=langresult, sentiment=sentimentresult, topwords=topwordsresult, showImg=wordcloudresult)

    if request.method == "POST":
        inputArtist = request.form['inputArtist']
        inputSong = request.form['inputSong']

        print(inputArtist)
        print(inputSong)
        
        lyricsresult = get_lyrics_from_genius(inputArtist,inputSong)
        langresult = fasttext_detect_language(str(lyricsresult))
        lyricsENresult = translate_lyrics(str(lyricsresult))
        sentimentresult = calculate_sentiment(str(lyricsresult))
        topwordsresult = get_top_words(str(lyricsENresult))
        wordcloudresult = get_word_cloud(topwordsresult)

        return render_template('mainpage.html', lyrics=lyricsresult, language=langresult, 
                    sentiment='POSITIVE ' + '(' + str(sentimentresult) + ')' if sentimentresult>0 else 'NEGATIVE ' + '(' + str(sentimentresult) + ')',
                    topwords=topwordsresult, showImg=wordcloudresult)


if __name__ == "__main__":
    app.run()