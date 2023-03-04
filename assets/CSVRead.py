import csv
string=input("Enter the category : ")

file=open('Categories.csv')
csvfile=csv.reader(file)
flag=-1
for col in csvfile:
    if flag==-1:    
        cat=col
        flag=1
    for word in col:
        if word.lower()==string.lower():
            print("Found")
            flag=col.index(word)
            print("Index = ",flag)
            print("Category = ",cat[flag])
            break;
