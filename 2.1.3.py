name1 = input("Name 1? \n")
name2 = input("Name 2? \n")

if name1[0].lower() < name2[0].lower():
    print("Alphabetical Order: True")
else:
    print("Alphabetical Order: False")

if name1 == name2: 
    print("Same name twice: True")
else:
    print("Same name twice: False")