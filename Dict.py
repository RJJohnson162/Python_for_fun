#Working with Dictionaries
#A dictionary is a collection of key-value pairs. It can be used to store data in an organized manner.
Menu = dict()
keys = list()
Values = list()

Menu_items= int (input("Enter the number of items in the Menu: "))

for item in range(Menu_items):
    Key = input ("Enter the name of menu item "+str(item+1)+": ")
    keys.append(Key)
    Value = float(input("Enter price for "+Key+" : Kshs "))
    Values.append(Value)

print("\nHere's your updated menu:\n")
print(dict(zip(keys,Values))) #food menu

#Printing all the food items only
print("\nFood Items Only\n")
print(dict(list(filter(lambda x: 'food' in x[0], zip(keys,Values)))))
