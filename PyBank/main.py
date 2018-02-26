import os
import csv

csvpath1 = os.path.join('budget_data_1.csv')
monthcount1 = 0
monthcount2 = 0

totalrevenue1 = 0
totalrevenue2 = 0

previous_row1 = 0
previous_row2 = 0

revenuechangelist1 = []
revenuechangelist2 = []

with open(csvpath1, newline = '') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=',')
    #print(csvreader1)

    first_row = next(csvreader1)
    
   
    for row in csvreader1:
        monthcount1 = monthcount1 + 1
        totalrevenue1 = totalrevenue1 + float(row[1])
        revenuechange1 = float(row[1]) - previous_row1
        revenuechangelist1.append(revenuechange1)
        previous_row1 = float(row[1])
        
        
        #print(row[1])
        #print(float(row[1]))
        #print(totalrevenue1)  

    #for row in csvreader1:
         #print(row)
   
    #subtract header
    


csvpath2 = os.path.join('budget_data_2.csv')

with open(csvpath2, newline = '') as csvfile2:
    csvreader2 = csv.reader(csvfile2,delimiter=',')
    #print(csvreader2)

    first_row = next(csvreader2)
    

    for row in csvreader2:
        monthcount2 = monthcount2 + 1  
        totalrevenue2 = totalrevenue2 + float(row[1])
        revenuechange2 = float(row[1]) - previous_row2
        revenuechangelist2.append(revenuechange2)
        previous_row2 = float(row[1])
        #print(row)
        #print(float(row[1]))
        #print(totalrevenue2)

    #for row in csvreader2:
        #print(row)
    data2 = list(csvreader2)
    #subtract header
    row_count2 = len(data2) - 1
        
print("Financial Analysis" + "\n + ----------------------------------" )

Total_Months = monthcount1 + monthcount2
print("Total Months: " + str(Total_Months))

Total_Revenue = totalrevenue1 + totalrevenue2
print("Total Revenue: "+ '$' + str(Total_Revenue))

Average_Revenue_Change = (revenuechange1 + revenuechange2) / Total_Months
print("Average Revenue Change: " + '$' + str(Average_Revenue_Change))

Greatest_Increase_in_Revenue1 = max(revenuechangelist1)
Greatest_Decrease_in_Revenue1 = min(revenuechangelist1)
Greatest_Increase_in_Revenue2 = max(revenuechangelist2)
Greatest_Decrease_in_Revenue2 = min(revenuechangelist2)
Greatest_Increase_in_Revenue = max(Greatest_Increase_in_Revenue1,Greatest_Increase_in_Revenue2)
Greatest_Decrease_in_Revenue = min(Greatest_Decrease_in_Revenue2,Greatest_Decrease_in_Revenue2)
print("Greatest Increase in Revenue: " + '$' + str(Greatest_Increase_in_Revenue))
print("Greatest Decrease in Revenue: " + '$' + str(Greatest_Decrease_in_Revenue))
