import os
import csv

csvpath1 = os.path.join('election_data_1.csv')
csvpath2 = os.path.join('election_data_2.csv')
#total number of votes cast
votecount1 = 0
votecount2 = 0
#complete list of candidates who received votes
candidates1 = []
candidates2 = []
#total number votes for each candidate
Cordin = 0
Seth = 0
Vestal = 0
Torres = 0

Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open(csvpath1, newline = '') as csvfile1:
    csvreader1 = csv.reader(csvfile1,delimiter=',')

    first_row = next(csvreader1)

    for row in csvreader1:
        votecount1 = votecount1 + 1
        if row[2] not in candidates1:
            candidates1.append(row[2])
            print(row[2])
            
        if row[2] == "Cordin":
            Cordin = Cordin + 1
        elif row[2] == "Seth":
            Seth = Seth + 1
        elif row[2] == "Vestal":
            Vestal = Vestal + 1
        elif row[2] == "Torres":
            Torres = Torres + 1

with open(csvpath2, newline = '') as csvfile2:
    csvreader2 = csv.reader(csvfile2,delimiter=',')

    first_row = next(csvreader2)

    for row in csvreader2:
        votecount2 = votecount2 + 1
        if row[2] not in candidates2:
            candidates2.append(row[2])
            print(row[2])
            
        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Li":
            Li = Li + 1
        elif 'Tooley' in row[2]:
            OTooley = OTooley + 1      

Total_Votes = votecount1 + votecount2

Vestal_Percent = float(Vestal / Total_Votes)*100
Torres_Percent = float(Torres / Total_Votes)*100
Seth_Percent = float(Seth / Total_Votes)*100
Cordin_Percent = float(Cordin / Total_Votes)*100

Khan_Percent = float(Khan / Total_Votes)*100
Correy_Percent = float(Correy / Total_Votes)*100
Li_Percent = float(Li/Total_Votes)*100
OTooley_Percent = float(OTooley/Total_Votes)*100




print("Election Results"+ "\n" + "-----------------------------")
print("Total Votes: "+ str(Total_Votes)+"\n")
print("-----------------------------")
print("Vestal: "+str(Vestal_Percent)+"%" + "(" + str(Vestal) + ")")
print("Torres: "+str(Torres_Percent)+"%" + "("+ str(Torres)+")")
print("Seth: "+str(Seth_Percent)+"%" + "("+ str(Seth)+")")
print("Cordin: "+str(Cordin_Percent)+"%" + "("+ str(Cordin)+")")

print("Khan: "+str(Khan_Percent)+"%" + "(" + str(Khan) + ")")
print("Correy: "+str(Correy_Percent)+"%" + "("+ str(Correy)+")")
print("Li: "+str(Li_Percent)+"%" + "("+ str(Li)+")")
print("O\'Tooley: "+str(OTooley_Percent)+"%" + "("+ str(OTooley)+")")
print("-----------------------------")
print("Winner: " + max(candidates2))
