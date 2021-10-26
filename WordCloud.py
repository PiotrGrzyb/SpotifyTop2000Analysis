import pandas
import wordcloud
from wordcloud import STOPWORDS, WordCloud
import matplotlib.pyplot as plt

ds = pandas.read_csv('../SpotifyTop2000/Spotify-2000.csv')
spotifyDataSet = ds.sort_values(by='Popularity', ascending='False')

stopwords = set(STOPWORDS)
wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=2000,
                          max_font_size=40,
                          random_state=42
                         ).generate(str(spotifyDataSet['Title']))
print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=900)
