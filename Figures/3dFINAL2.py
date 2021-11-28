import pandas
import plotly.express as px


def main():
    spotifyDataSet = pandas.read_csv('../Spotify-2000Group.csv')
    spotifyDataSet2 = spotifyDataSet.sort_values(by=['Loudness (dB)', 'Top Genre'], ascending='True')
    fig3 = px.scatter_3d(spotifyDataSet, x='Popularity',
                         y='Energy',
                         z='Danceability',
                         color='Beats Per Minute (BPM)',
                         size='Valence',
                         symbol='Top Genre',
                         hover_name='Title',
                         animation_frame='Loudness (dB)',
                         animation_group='Top Genre',
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
    fig3.data[0].marker.symbol = 'diamond-open'
    fig3.data[1].marker.symbol = 'cross'
    fig3.data[2].marker.symbol = 'circle-open'
    fig3.data[3].marker.symbol = 'x'
    #fig3.data[4].marker.symbol = 'diamond'
    #fig3.data[5].marker.symbol = 'square'

    fig3.show()


if __name__ == '__main__':
    main()
