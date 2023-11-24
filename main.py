import database

global opModes
opModes = database.load()
global opMode
opMode = []
choice = 0
while True:
    choice = int(input(" 1 to print the masterlist. 2 to read a spcific opmode. \n3 to add another opmode. 4 to save. 5 to reset changes."))
    if choice == 1:
        print(*opModes,sep='\n')
    if choice == 2:
        name = str(input("Enter the name: "))
        result = database.read(name, opModes)
        print("Name: " + str(result[0]))
        print("Aliance: " + str(result[1]))
        print("Start Location: " + str(result[2]))
        print("Max Score: " + str(result[3]))
        print("Concistancy rating: " + str(result[4]))

    if choice == 3:
        name = str(input("enter the name: "))
        side = str(input("enter the side: "))
        location = str(input("enter the location: "))
        score = str(input("enter the max score: " ))
        concistancy = str(input("enter the concistency(1-10): "))
        opModes = database.newOpMode(opModes, name, side, location, score, concistancy)
    if choice == 4:
        database.save(opModes)
    if choice == 5:
        opModes = database.load()