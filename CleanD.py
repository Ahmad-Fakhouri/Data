import csv
counts = {} #Creating an empty Dict to create the key and value from the DB 
with open ("favorites.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        lang = row['language'].upper().strip() # to enter the language row in the csv we save it in a var to use it in our code 
        # we add .upper() and .strip() to make the data clean if the data in the DB is lower or some of the letters are not the same in size or there's spaces 
        if lang not in counts: # here we will be asking if the language that mentioned in csv is not the counts Dict
            counts[lang] = 0  # Create the language in the counts Dict and put the value 0 if it was not there 
        counts[lang] += 1  # when you found the language add 1  to the value of the key for every time you find it 

for c in counts:
    print(f"{c} : {counts[c]}") #That will print the key and the cvalue of the Dict 
