import os
clear = lambda: os.system("cls")

shop = True
Bill = []
counter = 0
total = 0

while shop:
    clear()
    counter += 1
    print(f"Book No. {counter}")
    Record = []
    Record.append(      input("Enter the title of the book                     : "))
    Record.append(      input("Enter the name of the author of the book        : "))
    Record.append(int(  input("Enter the rental charges per day for the book   : ")))
    Record.append(int(  input("Enter the No of Days to rent the book for       : ")))
    Record.append(Record[2] * Record[3])
    Bill.append(Record)
    print("")
    shop = (            input("Do you wish to continue? [type yes to continue] : ") == "yes")

clear()
print("------------------------------------------------------------------------------------------------------------------------")
print("| Book No. | Title                          | Author                         | Rental Charges | No. of Days | Amount   |")
print("|----------|--------------------------------|--------------------------------|----------------|-------------|----------|")

for i in range(len(Bill)):
    print(f"| {i+1}        " , end="| ")
    print(Bill[i][0], end="")
    print(" "*(31 - len(Bill[i][0])), end="| ")
    print(Bill[i][1], end="")
    print(" "*(31 - len(Bill[i][1])), end="| ")
    print(Bill[i][2], end="")
    print(" "*(15 - len(str(Bill[i][2]))), end="| ")
    print(Bill[i][3], end="")
    print(" "*(12 - len(str(Bill[i][3]))), end="| ")
    print(Bill[i][4], end="")
    print(" "*(9 - len(str(Bill[i][4]))), end="|\n")
    total += Bill[i][4]


print("|----------------------------------------------------------------------------------------------------------------------|")
print("|  Total", end="")
print(" "*(110 - len(str(total))), end="")
print(total, end=" |\n")
print("------------------------------------------------------------------------------------------------------------------------")