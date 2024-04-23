import fitz
import csv

doc = fitz.open("EB_Redemption_Details.pdf")

def date_format(date):
    date=date.replace("Jan","01")
    date=date.replace("Feb","02")
    date=date.replace("Mar","03")
    date=date.replace("Apr","04")
    date=date.replace("May","05")
    date=date.replace("Jun","06")
    date=date.replace("Jul","07")
    date=date.replace("Aug","08")
    date=date.replace("Sep","09")
    date=date.replace("Oct","10")
    date=date.replace("Nov","11")
    date=date.replace("Dec","12")
    date=date.split("/")
    date=date[2]+'-'+date[1]+"-"+date[0]
    return date
def num_format(num):
    num=num.replace(",","")
    return num

def doc2_format(row):
    row[2]=date_format(row[2])
    row[3]=date_format(row[3])
    row[4]=date_format(row[4])
    row[-4]=num_format(row[-4])
    return row

def doc1_format(row):
    row[1]=date_format(row[1])
    row[-3]=num_format(row[-3])
    return row
    
with open("EB_Redemption_Details.csv","w",newline="") as file:
    writer=csv.writer(file,delimiter="+")
    i=0
    for page in doc:
        table=page.find_tables().tables[0].extract()
        writer.writerows(list(map(doc1_format,table[1:])))
        i+=1
        print(i)
        
doc.close()

doc = fitz.open("EB_Purchase_Details.pdf")

with open("EB_Purchase_Details.csv","w",newline="") as file:
    writer=csv.writer(file,delimiter="+")
    i=0
    for page in doc:
        table=page.find_tables().tables[0].extract()
        writer.writerows(list(map(doc2_format,table[1:])))
        i+=1
        print(i)
doc.close()

