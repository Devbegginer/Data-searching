#Now we're going to create something that we've already studied in Alura, which is the define function, 
#i.e. we're going to create functions, each function will have its own specific functionality. 
#The code that will appear to fetch the items will be in another file.

#build functions 


# depreciation and exclusion

# let`s build a inventory 

def fillInventory(list):
    respost = "YES"
    while respost =="YES":
        equipment = [
                    input("equipment requested: "),
                    float(input("Value of equipment: ")),
                    int(input("Serial of equipment: ")),
                    input("departament of equipment: ")]
        list.append(equipment)
        respost = input("write \"YES\" to continue or \"NO\" for stop : ").upper()

def showInventory(list):
    for element in list:
        print("name.........", element[0])
        print("value........",element[1])
        print("Serial.......",element[2])
        print("Departament..",element[3])

def searchItemInInventory(list):
    search = input("\nEnter the name of the device you want to search for: ")
    for element in list:
        if search == element[0]:
            print("Value..: ", element [1])
            print("Serial.: ", element [2])

def depreciationForItem(list):
    depreciation = input("\n choose the equipment to be depreciated: ")
    for element in list:
        if depreciation == element[0]:
            print("former value: ", element[1])             # element 1 is where the value of equipment
            element[1] = element[1] * 0.9
            print("New value: ", element[1])

def ExclusionSerial(list):
    serial = int(input("enter the serial equipment of the device to be deleted: "))
    for element in list:
        if element[2]== serial:
            list.remove(element) 

# for element in inventory:
#     print("Name.......",element[0])
#     print("Value......",element[1])
#     print("Serial....",element[2])
#     print("Departament.",element[3])

def Resumevalues(list):
    values = []
    for element in list:
        values.append(element[1])
    if len(values)>0:
        print("The most expensive equipment costs: ",max(values))
        print("the most cheap equipment costs: ", min(values))
        print("and the total amount of equipment e: ",sum(values))
    #so, we put all inside in list 
        #one variable where 



#