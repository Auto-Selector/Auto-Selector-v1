import pickle
import os

global database
global databaseIndex
databaseIndex = []
database = []

##Check if the database file exist and either creates it or opens it
def load():
    if os.path.isfile('database.txt'):
        with open('database.txt', 'rb') as f:
            database = pickle.load(f)
            f.close()
            if not os.path.exists('img'):
                os.mkdir('img')
            return database
    else:
        with open('database.txt', 'w') as f:
            f.close()
            with open('database.txt', 'wb') as f:
                database = []
                pickle.dump(database, f)
                if not os.path.exists('img'):
                    os.mkdir('img')
                return database

            
##saves and closes the database
def save(listName):
    with open('database.txt', 'wb') as f:
        pickle.dump(listName, f)
        return True

##takes the inputs and makes a new opMode in the database
def newOpMode(listname, name, side, location, score, concistency, imageName):
    newOpMode = []
    newOpMode.append(name)
    databaseIndex.append(name)
    newOpMode.append(side)
    newOpMode.append(location)
    newOpMode.append(score)
    newOpMode.append(concistency)
    newOpMode.append(imageName)
    listname.append(newOpMode)
    return listname

##reads a given opmode from its name
def read(name, listName):
    desiredOpMode = [opMode for opMode in listName if name.lower() == str(opMode[0]).lower()] 
    return desiredOpMode[0]

def delete(name, listName):
    index = next((i for i, opMode in enumerate(listName) if name.lower() == str(opMode[0]).lower()), None)
    if index != 'None':
        listName.pop(index)
        return True
    elif index == 'None':
        return False
