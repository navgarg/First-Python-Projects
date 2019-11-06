class Mobile():
    mobileName = ""
    price = 0
    modelNumber = 0;
    def free():
        pass
    def insert(obj, mobileName, modelNumber, price):
        obj.mobileName = mobileName
        obj.modelNumber = modelNumber
        obj.price = price
    def getCurrentPrice(obj, mobileName, modelNumber):
        if mobileName == obj.mobileName and modelNumber == obj.modelNumber:
            return obj.price
        return 0
    def getPrice(obj):
        return price
    def getMobileName(obj):
        return mobileName
    def getModelNumber(obj):
        return modelNumber
    def setPrice(obj, price):
        obj.price = price
    def setModelNumber(obj, modelNumber):
        obj.modelNumber = modelNumber
    def setMobileName(obj, mobileName):
        obj.mobileName = mobileName
arr = []
def isInt(num):
    try:
        result = int(num)
        if result>0:
            return result
        else:
            print("Invalid integer")
            return 0
    except ValueError:
        print("Invalid integer")
    return 0
def createObject(noOfObjects):
    for i in range(noOfObjects):
        arr.append(Mobile())
def printAll(array):
    for i in array:
        print(i.__dict__)
print("This Program maintains a list of all the mobiles you enter.")
noOfDetailsCheck = input("Enter number of details: ")
while isInt(noOfDetailsCheck) == 0:
   noOfDetailsCheck = input("Enter number of details: ")
noOfDetails = isInt(noOfDetailsCheck)
createObject(noOfDetails)
for i in range(noOfDetails):
    mobileName = input("Enter mobile name: ")
    priceCheck = input("Enter price: ")
    while isInt(priceCheck) == 0:
        priceCheck = input("Enter price: ")
    price = isInt(priceCheck)
    modelNumberCheck = input("Enter model number: ")
    while isInt(modelNumberCheck) == 0:
        modelNumberCheck = input("Enter model number: ")
    modelNumber = isInt(modelNumberCheck)
    arr[i].insert(mobileName, modelNumber, price)
print("Enter your choice")
choice = int(input("Enter 1 for all details and 2 for particular details: "))
if choice == 1:
    print("Details: ")
    printAll(arr)
    #print(arr[0].getMobileName())
    #print(arr[1].getMobileName())
elif choice == 2:
    mobileName = input("Enter mobile name: ")
    modelNumber = int(input("Enter model number: "))
    for i in range(noOfDetails):
        result = arr[i].getCurrentPrice(mobileName, modelNumber)
        if result != 0:
            print("Price: ", result)
            count = 1
            break
    if count == 0:
        print("No such details exist")
    
        
