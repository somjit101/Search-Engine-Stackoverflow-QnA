import csv

# Not Using Pandas here as it loads all of the data into RAM at once.


cnt = 0
# Read Questions from Dataset 
with open('./data/Questions.csv', encoding="latin1") as csvfile:

        readCSV = csv.reader(csvfile, delimiter=',', )
        next(readCSV, None)  # skip the headers

        for row in readCSV:

                # keep count of # rows processed
                cnt += 1
                #print(cnt)

print(cnt, len(row))



cnt = 0
# Read Answers from Dataset
with open('./data/Answers.csv', encoding="latin1") as csvfile:

        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV, None)  # skip the headers

        for row in readCSV:

                # keep count of # rows processed
                cnt += 1

print(cnt, len(row))
