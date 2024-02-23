import csv
counts = {} #Creating an empty Dict to create the key and value from the DB 
with open ("favorites.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        lang = row['language'].upper().strip() 
        if lang not in counts: 
            counts[lang] = 0  
        counts[lang] += 1  


# def get_values(lang):
#     return counts[lang]
#lambda anonymous function takes the parameter and the returns easier way to make a function if the function only 
# returns
for c in sorted(counts,key =lambda lang:counts[lang],reverse=False):
    print(f"{c} : {counts[c]}") 