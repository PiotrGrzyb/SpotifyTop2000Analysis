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
                        color='Energy'
                        )

    # fig.show()
    spotifyDataSet2 = spotifyDataSet.sort_values(by='Year', ascending='True')
    fig2 = px.scatter_3d(spotifyDataSet2, x='Popularity',
                         y='Energy',
                         z='Danceability',
                         color='Beats Per Minute (BPM)',
                         size='Valence',
                         hover_name='Title',
                         animation_frame='Year',
                         animation_group='Artist',
                         size_max=55, range_z=[0, 100], range_y=[0, 100], range_x=[0, 100]
                         )

    fig2.show()


if __name__ == '__main__':
    main()
