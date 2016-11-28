def election(trials):
    import random as rand
    import matplotlib.pyplot as plt
    import csv

    def loadData():
        """
        take in a csv and return an array with lists of states, electoral votes,
        prob(Clinton) and prob(Trump)
        """
        state_name = []
        elec_votes = []
        dem_perc = []
        rep_perc = []

        with open('electorate2016.csv', 'rb') as pollingInfo:
            reader = csv.reader(pollingInfo)
            #initialize row_num
            row_num = 0
            for row in reader:
                #don't collect the first row of data because this is text
                if row_num > 0:
                    # we need data from columns 0, 2, 3, and 4
                    for i in [0,2,3,4]:
                        if i == 0:
                            state_name.append(row[i])
                        elif i == 2:
                            elec_votes.append(int(row[i]))
                        elif i == 3:
                            dem_perc.append(float(row[i]))
                        elif i == 4:
                            rep_perc.append(float(row[i]))
                row_num += 1

        return [state_name, elec_votes,dem_perc, rep_perc]

