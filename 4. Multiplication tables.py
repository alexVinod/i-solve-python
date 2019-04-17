from prettytable import PrettyTable
num = int(input("Enter Number for Table :"))
t = PrettyTable(['Number', 'Times',"Output"])
for i in range(1,11):
    t.add_row([num, i,int(num*i)])
print(t)
