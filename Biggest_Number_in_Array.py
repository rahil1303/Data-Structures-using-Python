def findbiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1,len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    print(biggestNumber)
    
print(findbiggestNumber([4,3,6,8]))
