import pandas
import plotly.express as px
import matplotlib.pyplot as plt


def main():
    spotifyDataSet = pandas.read_csv('../SpotifyTop2000/Spotify-2000.csv')

    # Check if data set is loaded
    # print(spotifyDataSet.head())
    # Check dataset columns
    # print(spotifyDataSet.info())

    # spotifyDataSet.plot.hist(spotifyDataSet, x="Popularity", y="Year")

    # plt.show(block=True)
    # plt.interactive(False)

    # fig = px.scatter(spotifyDataSet, x="Popularity", y="Year")
    # fig.show()

    # fig2 = px.scatter(spotifyDataSet, x="Popularity", y="Year", color="Loudness (dB)")
    # fig2.show()

    fig3 = px.scatter(spotifyDataSet, x="Popularity", y="Top Genre", size="Energy", color="Beats Per Minute (BPM)",
                      hover_name="Title")
    # fig3.show()

    fig4 = px.scatter(spotifyDataSet, x="Popularity", y="Year", size="Energy", color="Beats Per Minute (BPM)",
                      hover_name="Title")
    fig4.add_layout_image(
        dict(
            source="C:/Users/Piotr/PycharmProjects/SpotifyTop2000Analysis/logo.png",
            xref="paper", yref="paper",
            x=1, y=1.05,
            sizex=0.2, sizey=0.2,
            xanchor="right", yanchor="bottom"
        )
    )
    fig4.update_layout(
        autosize=False,
        height=800,
        width=700,
        bargap=0.15,
        bargroupgap=0.1,
        barmode="stack",
        hovermode="x",
        margin=dict(r=20, l=300, b=75, t=125),
    )
    fig4.show()

    # fig5 = px.pie(spotifyDataSet, values="Popularity", names="Top Genre")
    # fig5.show()

    fig6 = px.line(spotifyDataSet, x="Beats Per Minute (BPM)", y="Popularity", line_group="Beats Per Minute (BPM)",
                   hover_name="Beats Per Minute (BPM)",
                   line_shape="spline", render_mode="svg")
    # fig6.show()

    #spotifyDataSet.loc[spotifyDataSet['Popularity'] < 80, 'Top Genre'] = 'Other Genres'
    #fig7 = px.pie(spotifyDataSet, values="Popularity", names="Top Genre")
    #fig7.show()

    #fig8 = px.histogram(spotifyDataSet, x="Top Genre", y="Popularity")
    #fig8.show()

if __name__ == '__main__':
    main()
