import csv
with open("sales_data.csv", r) as csvFile:

file = csvFile.readline()

idName = str(input("Search by invoice id (id) or customer last name(lname)? "))

if(idName != "id" or idName != "lname")
    print("Error: User must input either id or lname!")

searchTerm = str(input("Enter your search term: "))

terms = 0

if idName == "id":
    for identifier in csvFile:
        
        terms += 1
        
        print(identifier)
        
print("{} records found.".format(terms))

if idName == "lname":
    for lastName in csvFile:
        terms += 1
        print(idName)

print("{} records found.".format(terms))
