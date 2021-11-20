import pandas
import plotly.express as px
import pandas as pd
from sklearn import preprocessing


def main():
    sDS = pandas.read_csv('../../SpotifyTop2000/Spotify-2000.csv')
    sDS.sort_values('Year')

    column_names_to_normalize = ['Liveness']
    x = sDS[column_names_to_normalize].values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    sDS_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index=sDS.index)
    sDS[column_names_to_normalize] = sDS_temp

    fig3 = px.scatter_3d(sDS, x='Popularity',
                         y='Energy',
                         z='Danceability',
                         color='Beats Per Minute (BPM)',
                         size='Valence',
                         symbol='Loudness (dB)',
                         opacity='Liveness',
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
