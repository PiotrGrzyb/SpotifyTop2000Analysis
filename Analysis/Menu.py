import pandas
import plotly.express as px
from SetStats import stats
from BoxPlots import box
from Histo import histograms
from Scatter import scatter

def main():
    run = True
    while run:
        spotifyDataSet = pandas.read_csv('../../SpotifyTop2000/Spotify-2000.csv')

        print("[1] Stats")
        print("[2] Box plot")
        print("[3] Histograms")
        print("[4] Correlation matrix")
        print("[5] Scatter with regression")
        print("[6] Quit")
        choice = input("What you want to view?:")

        if int(choice) == 1:
            if int(stats(spotifyDataSet)) == 0:
                continue
            else:
                pass
        elif int(choice) == 2:
            box(spotifyDataSet)

        elif int(choice) == 3:
            histograms(spotifyDataSet)

        elif int(choice) == 4:
            fig = px.imshow(spotifyDataSet.corr())
            fig.show()

        elif int(choice) == 5:
            scatter(spotifyDataSet)

        elif int(choice) == 6:
            run = False


if __name__ == '__main__':
    main()
