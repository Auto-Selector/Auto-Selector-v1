import database
from PIL import Image as image

global opModes
opModes = database.load()
global opMode
opMode = []
choice = 0
while True:
    choice = int(input(" 1 to print the masterlist. 2 to read a spcific opmode. \n3 to add another opmode. 4 to save. 5 to reset changes. 6 to delete an opmode"))
    if choice == 1:
        print(*opModes,sep='\n')
    if choice == 2:
        name = str(input("Enter the name: "))
        result = database.read(name, opModes)
        if len(result) > 1:
            print("Name: " + str(result[0]))
            print("Aliance: " + str(result[1]))
            print("Start Location: " + str(result[2]))
            print("Max Score: " + str(result[3]))
            print("Concistancy rating: " + str(result[4]))
            print("Image Name: " + str(result[5]))
            try:
                image.open("img/"+str(result[5])).show()
            except:
                print("the file does not exist. Did you put an extention?")
        else:
            print("That OpMode does not exist")

    if choice == 3:
        name = str(input("enter the name: "))
        side = str(input("enter the side: "))
        location = str(input("enter the location: "))
        score = str(input("enter the max score: " ))
        concistancy = str(input("enter the concistency(1-10): "))
        imageName = str(input("What is your image name? "))
        opModes = database.newOpMode(opModes, name, side, location, score, concistancy, imageName)
    if choice == 4:
        database.save(opModes)
    if choice == 5:
        opModes = database.load()
    if choice == 6:
        name = str(input("Enter the name: "))
        complete = database.delete(name, opModes)
        if complete:
            print(str(name) + " was sucessfully deleted")
        if not complete:
            print("OpMode does not exist")