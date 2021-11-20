import pandas
import plotly.express as px


def histograms(dataSet=None):
    print("[1] Year")
    print("[2] Energy")
    print("[3] Beats Per Minute (BPM)")
    print("[4] Danceabillity")
    print("[5] Loudness (dB)")
    print("[6] Liveness")
    print("[7] Valence")
    print("[8] Acousticness")
    print("[9] Speechiness")
    print("[10] Popularity")
    print("[11] Top Genre")
    print("[12] Artist")

    choice1 = input("Which attribute histogram to show ")

    if int(choice1) == 1:
        Histogram = px.histogram(data_frame=dataSet, x='Year')
        Histogram.show()
    elif int(choice1) == 2:
        Histogram = px.histogram(data_frame=dataSet, x='Energy')
        Histogram.show()
    elif int(choice1) == 3:
        Histogram = px.histogram(data_frame=dataSet, x='Beats Per Minute (BPM)')
        Histogram.show()
    elif int(choice1) == 4:
        Histogram = px.histogram(data_frame=dataSet, x='Danceabillity')
        Histogram.show()
    elif int(choice1) == 5:
        Histogram = px.histogram(data_frame=dataSet, x='Loudness (dB)')
        Histogram.show()
    elif int(choice1) == 6:
        Histogram = px.histogram(data_frame=dataSet, x='Liveness')
        Histogram.show()
    elif int(choice1) == 7:
        Histogram = px.histogram(data_frame=dataSet, x='Valence')
        Histogram.show()
    elif int(choice1) == 8:
        Histogram = px.histogram(data_frame=dataSet, x='Acousticness')
        Histogram.show()
    elif int(choice1) == 9:
        Histogram = px.histogram(data_frame=dataSet, x='Speechiness')
        Histogram.show()
    elif int(choice1) == 10:
        Histogram = px.histogram(data_frame=dataSet, x='Popularity')
        Histogram.show()
    elif int(choice1) == 11:
        Histogram = px.histogram(data_frame=dataSet, x='Top Genre')
        Histogram.show()
    elif int(choice1) == 12:
        Histogram = px.histogram(data_frame=dataSet, x='Artist')
        Histogram.show()
