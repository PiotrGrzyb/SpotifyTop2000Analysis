import pandas


def stats(dataSet=None):
    runStats = True
    while runStats:
        print("[1] Min")
        print("[2] Max")
        print("[3] Mean")
        print("[4] Standard deviation")
        print("[5] Median")
        print("[6] Q3 - Q1")
        print("[7] Q 0.10")
        print("[8] Q 0.90")
        print("[9] Quit")
        choiceA = input("What to view: ")

        if int(choiceA) == 1:
            minValue = dataSet.min()
            print(minValue)
        elif int(choiceA) == 2:
            maxValue = dataSet.max()
            print(maxValue)
        elif int(choiceA) == 3:
            averageValue = dataSet.mean()
            print(averageValue)
        elif int(choiceA) == 4:
            standardDeviation = dataSet.std()
            print(standardDeviation)
        elif int(choiceA) == 5:
            medianValue = dataSet.median()
            print(medianValue)
        elif int(choiceA) == 6:
            q1 = dataSet.quantile(0.25)
            q3 = dataSet.quantile(0.75)
            iqrValue = q3 - q1
            print(iqrValue)
        elif int(choiceA) == 7:
            q01 = dataSet.quantile(0.1)
            print(q01)
        elif int(choiceA) == 8:
            q09 = dataSet.quantile(0.9)
            print(q09)
        elif int(choiceA) == 9:
            return 0
