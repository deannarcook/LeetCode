class Solution(object):
    def sortByBits(self, arr):
        # list to store the binary cardinality of the values in arr
        binaryCardinalityList = []

        for i in arr:
            binaryValue = bin(i).replace('b', '')
            binaryCardinality = 0
            for i in binaryValue:
                binaryCardinality += int(i)
            binaryCardinalityList.append(binaryCardinality)
            print('The binary value of ' + str(i) + ' is ' + binaryValue)
            print('The binary cardinality is ' + str(binaryCardinality))
            print('\n')

        # dictionary to store the integer values and their binary cardinality
        arrBinaryCardinality = {}

        keyIndex = 0

        # combine list of integer values and binary cardinalit of integer values into a dictionary
        for i in binaryCardinalityList:
            arrBinaryCardinality[arr[keyIndex]] = i
            keyIndex += 1

        """
        # OPTION 1 for Sorting Dictionary by Value : sorted() + Function
        def getValueForSort(item):
            return item[1]

        print(sorted(arrBinaryCardinality.items(),key = getValueForSort))
        """

        print(arrBinaryCardinality)

        # OPTION 2 For Sorting by Value - sorted() + Lambda Function
        # item() returns view object containing key:value pairs as a tuple
        # the lambda funtion sets the key to sort on to the value from items()
        sortedByBinaryCardinality = sorted(arrBinaryCardinality.items(), key=lambda x: x[1])

        print(sortedByBinaryCardinality)

        # check for integers with the same binary cardinality

        keys = list(set(arrBinaryCardinality.values()))

        countBinaryCardinality = {}

        for i in keys:
            countBinaryCardinality[i] = keys.count(i)

        print(countBinaryCardinality)
        # build result list

        resultArr = []

        ###
        ### need to find out how to sort by integer when binary cardinality is the same for multiple ints
        ###
        for i in sortedByBinaryCardinality:
            resultArr.append(i[0])

        for i in sortedByBinaryCardinality:
            if i[0] in list(countBinaryCardinality.keys()):
                print('yes')









