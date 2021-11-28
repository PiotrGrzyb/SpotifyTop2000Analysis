import pandas
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np


def main():
    sDS = pandas.read_csv('../../SpotifyTop2000/Spotify-2000.csv')
    sDS.sort_values('Year')
    SpotifyRock = sDS.loc[(sDS["Top Genre"] == 'album rock') | (sDS["Top Genre"] == 'classic rock') |
                          (sDS["Top Genre"] == 'modern rock') | (sDS["Top Genre"] == 'alternative rock')]

    SpotifyPop = sDS.loc[(sDS["Top Genre"] == 'dance pop') | (sDS["Top Genre"] == 'dutch pop') |
                         (sDS["Top Genre"] == 'german pop') | (sDS["Top Genre"] == 'classic uk pop')]

    fig4 = px.scatter_3d(SpotifyRock, x='Popularity',
                         y='Energy',
                         z='Danceability',
                         labels='Rock',
                         color='Beats Per Minute (BPM)',
                         size='Valence',
                         hover_name='Title',
                         animation_frame='Year',
                         animation_group='Title',
                         size_max=55, range_z=[0, 100], range_y=[0, 100], range_x=[0, 100]
                         )
    fig5 = px.scatter_3d(SpotifyPop, x='Popularity',
                         y='Energy',
                         z='Danceability',
                         labels='Pop',
                         color='Beats Per Minute (BPM)',
                         size='Valence',
                         hover_name='Title',
                         animation_frame='Year',
                         animation_group='Title',
                         size_max=55, range_z=[0, 100], range_y=[0, 100], range_x=[0, 100]
                         )
    fig4.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    fig3 = go.Figure(data=fig4.data + fig5.data, layout=fig4.layout, frames=fig4.frames)


    fig3.show()


if __name__ == '__main__':
    main()
