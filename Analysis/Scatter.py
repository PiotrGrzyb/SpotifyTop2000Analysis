import plotly.express as px


def scatter(dataSet=None):
    print("[1] Year - Loudness (dB)")
    print("[2] Energy - Loudness (dB)")
    print("[3] Energy - Valence")
    print("[4] Energy - Acousticness")
    print("[5] Danceability - Valence")
    print("[6] Loudness (dB) - Acousticness")
    choice1 = input("Which attribute scatter plot to show ")
    if int(choice1) == 1:
        Scatter = px.scatter(dataSet, x="Year", y="Loudness (dB)", trendline="ols", trendline_color_override="red")
        Scatter.show()
    elif int(choice1) == 2:
        Scatter = px.scatter(dataSet, x="Energy", y="Loudness (dB)", trendline="ols", trendline_color_override="red")
        Scatter.show()
    elif int(choice1) == 3:
        Scatter = px.scatter(dataSet, x="Energy", y="Valence", trendline="ols", trendline_color_override="red")
        Scatter.show()
    elif int(choice1) == 4:
        Scatter = px.scatter(dataSet, x="Energy", y="Acousticness", trendline="ols", trendline_color_override="red")
        Scatter.show()
    elif int(choice1) == 5:
        Scatter = px.scatter(dataSet, x="Danceability", y="Valence", trendline="ols", trendline_color_override="red")
        Scatter.show()
    elif int(choice1) == 6:
        Scatter = px.scatter(dataSet, x="Loudness (dB)", y="Acousticness", trendline="ols",
                             trendline_color_override="red")
        Scatter.show()
