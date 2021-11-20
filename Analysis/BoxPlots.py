import plotly.express as px


def box(dataSet=None):
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

        choice1 = input("Which attribute box plot to show ")
        if int(choice1) == 1:
            fLenghtBox = px.box(data_frame=dataSet, y='Year')
            fLenghtBox.show()
        elif int(choice1) == 2:
            fWidthBox = px.box(data_frame=dataSet, y='Energy')
            fWidthBox.show()
        elif int(choice1) == 3:
            fSizeBox = px.box(data_frame=dataSet, y='Beats Per Minute (BPM)')
            fSizeBox.show()
        elif int(choice1) == 4:
            fConcBox = px.box(data_frame=dataSet, y='Danceability')
            fConcBox.show()
        elif int(choice1) == 5:
            fConc1Box = px.box(data_frame=dataSet, y='Loudness (dB)')
            fConc1Box.show()
        elif int(choice1) == 6:
            fAsymBox = px.box(data_frame=dataSet, y='Liveness')
            fAsymBox.show()
        elif int(choice1) == 7:
            fM3LongBox = px.box(data_frame=dataSet, y='Valence')
            fM3LongBox.show()
        elif int(choice1) == 8:
            fM3TransBox = px.box(data_frame=dataSet, y='Acousticness')
            fM3TransBox.show()
        elif int(choice1) == 9:
            fAlphaBox = px.box(data_frame=dataSet, y='Speechiness')
            fAlphaBox.show()
        elif int(choice1) == 10:
            fDistBox = px.box(data_frame=dataSet, y='Popularity')
            fDistBox.show()

