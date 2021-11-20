import pandas
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np


def main():
    spotifyDataSet = pandas.read_csv('../../SpotifyTop2000/Spotify-2000.csv')
    spotifyDataSet2 = spotifyDataSet.sort_values(by=['Loudness (dB)','Top Genre'], ascending='True')
    fig3 = px.scatter_3d(spotifyDataSet2, x='Popularity',
                         y='Energy',
                         z='Danceability',
                         color='Beats Per Minute (BPM)',
                         size='Valence',
                         symbol='Top Genre',
                         hover_name='Title',
                         animation_frame='Loudness (dB)',
                         animation_group='Year',
                         size_max=55, range_z=[0, 100], range_y=[0, 100], range_x=[0, 100]
                         )
    fig3.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    fig3.add_layout_image(
        dict(
            source="logo.png",
            xref="paper", yref="paper",
            x=1, y=1.05,
            sizex=0.2, sizey=0.2,
            xanchor="right", yanchor="bottom"
        )
    )

    fig3.show()


if __name__ == '__main__':
    main()
