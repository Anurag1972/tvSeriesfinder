import csv

file=open("data.tsv","r")

reader=csv.DictReader(file,delimiter="\t")

tv_series=open("tvseries.csv","w")

writer=csv.writer(tv_series)

writer.writerow(["tconst","primarytitle","startyear","genres"])

for row in reader:
    if row["startYear"]=="\\N":
        continue
    startyear=int(row["startYear"])

    if startyear< 1972 :
        continue
    if row["titleType"] =="tvSeries" and row["isAdult"]=="0":
            writer.writerow([row["tconst"],row["primaryTitle"],row["startYear"],row["genres"]])




