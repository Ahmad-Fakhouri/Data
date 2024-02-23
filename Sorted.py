import csv
counts = {} #Creating an empty Dict to create the key and value from the DB 
with open ("favorites.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        lang = row['language'].upper().strip() 
        if lang not in counts: 
            counts[lang] = 0  
        counts[lang] += 1  


# This function returns the value of the key of the Dict
def get_values(lang):
    return counts[lang]

#sorted is a function that sort the elements from A to Z 
#Reverse when it's false the elements will be sort from A - Z but if it was true it will be from Z-A 
# The key takes a function that's why we did the Get_value function 
# i don't need to pass any value in the function because the sorted function takes the  
# keys of the count and pass it to the get_value  
for c in sorted(counts,key =get_values,reverse=False):
    print(f"{c} : {counts[c]}") 
# Every time the loops starts it in every cycle it goes to the counts and take the key and pass it to 
# the function get_values and the function return the values and then it start sorting it by values
# because of the sorted if the reverse  was false it will start from  low to  high if it's was true it will be 
# from high to low 