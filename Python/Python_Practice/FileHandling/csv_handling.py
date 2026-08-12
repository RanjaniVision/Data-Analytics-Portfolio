'''file reader in csv file'''

'''import csv
with open("data.csv","r") as file:
    reader =csv.reader(file)
    for row in reader:
        print(row)

'''write a new one write mean new data only displayed in csv file'''
import csv
with open("data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Ink",30])
    writer.writerow(["Eraser",20])

import csv
with open("data.csv","w",newline="") as file:
    writer = csv.writer(file)'''
  
  #This storted dictionary 
import csv
with open("data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        totalsales=totalsales+int(row["Sales"])
        print(row)