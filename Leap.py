s=int(input("Enter the starting year "))
e=int(input("Enter ending year "))
leaps=[year for year in range(s,e) if year%4==0]
print(leaps)