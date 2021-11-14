import pandas
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np


def main():
    sDS = pandas.read_csv('../SpotifyTop2000/Spotify-2000.csv')
    sDS.sort_values('Year')
    fig3 = px.scatter_3d(sDS, x='Popularity',
                         y='Energy',
                         z='Danceability',
                         color='Beats Per Minute (BPM)',
                         size='Valence',
                         symbol='Loudness (dB)',
                         hover_name='Title',
                         animation_frame='Year',
                         animation_group='Title',
                         size_max=55, range_z=[0, 100], range_y=[0, 100], range_x=[0, 100]
                         )
    fig3.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))

    fig3.show()


if __name__ == '__main__':
    main()
