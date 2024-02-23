import csv
import sys
get_data = input("language: ").upper().strip() 
counts = 0 #when the user writes a language that's in the DB i will increase the value by 1 for everytime it's
# in the DB 

with open ("favorites.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        lang = row['language'].upper().strip() 
    
        if get_data == lang:
            counts += 1
        else:
            print("Please write a language that it's in the DB ")
            sys.exit(0)

    print (counts)