football_team = []
repeat = "Y"
while repeat == "Y" :
    name = input("Enter The Player's Name: ")
    football_team.append(name)
repeat = input("Do You want to Enter another Name(Y/N) : ")
print(football_team)