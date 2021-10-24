import pandas
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np


def main():
    spotifyDataSet = pandas.read_csv('../SpotifyTop2000/Spotify-2000.csv')
    # Check if data set is loaded
    # print(spotifyDataSet.head())
    # Check dataset columns
    # print(spotifyDataSet.info())
    fig = px.scatter_3d(spotifyDataSet, x='Year',
                    y='Popularity',
                    z='Beats Per Minute (BPM)',
                    color='Energy')

    fig.show()


if __name__ == '__main__':
    main()