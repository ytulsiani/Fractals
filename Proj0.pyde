def setup():
    size(900, 900)
    noStroke()
def draw():
    background(255, 255, 255)
    real = (mouseX - 450.0) * 1/150
    imaginary = -(mouseY - 450.0) * 1/150
    z = real + 1j * imaginary
    print(z)
    n = 0
    listOfNumbers = [0 + 1j * 0]
    prevList = [0]
    for i in range(0, 9):
        newList = []
        for j in range(len(prevList)):
            newList.append(prevList[j] + (z**i))
            newList.append(prevList[j] - (z**i))
        listOfNumbers.extend(newList)
        prevList = newList
    for i in range(len(listOfNumbers)):
        if(listOfNumbers[i].real >= 0 and listOfNumbers[i].imag >= 0):
            fill(55,94,151)
        elif (listOfNumbers[i].real < 0 and listOfNumbers[i].imag >= 0):
            fill(251,101,66)
        elif(listOfNumbers[i].real >= 0 and listOfNumbers[i].imag < 0):
            fill(255,187,0)
        else:
            fill(63,104,28)
    #TODO: MAKE SURE I AM USING A COLOR CODE. NEGATIVE POSITIVE? DEPTH (NEED TO USE APPEND IN CODE ABOVE RATHER THAN EXTEND TO DO THIS)?
        ellipse((-(listOfNumbers[i].real * 150) + 450), ((listOfNumbers[i].imag * 150)+ 450), 7, 7)