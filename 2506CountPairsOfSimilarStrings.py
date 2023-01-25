class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        i = 0
        j = i + 1

        stringsAreSimilar = False
        countSimilarStringPairs = 0

        while i <= len(words)-1:
            while j <= len(words) - i:
                print('\n')
                print('SIMILARITY CHECK 1: Looking for ' + words[i] + ' characters in ' + words[j])
                print('i: ' + str(i))
                print('j: ' + str(j))
                for w in words[i]:
                    print('w: ' + w)
                    if w in words[j]:
                        stringsAreSimilar = True
                        print(w + ' exists in ' + words[j])
                    else:
                        stringsAreSimilar = False
                        print(w + ' does not exists in ' + words[j])
                        break

                print('SIMILARITY CHECK 2: Looking for ' + words[j] + ' characters in ' + words[i])
                if stringsAreSimilar == True:
                    for w in words[j]:
                        print('w: ' + w)
                        if w in words[i]:
                            stringsAreSimilar = True
                            print(w + ' exists in ' + words[i])
                        else:
                            stringsAreSimilar = False
                            print(w + ' does not exists in ' + words[i])
                            break

                if stringsAreSimilar == True:
                    countSimilarStringPairs += 1
                    print('Incrementing counter. New countSimilarStringPairs value is: ' + str(countSimilarStringPairs))

                j += 1

                if j == len(words):
                    i += 1
                    print('i = ' + str(i))
                    j = i + 1
                    print('j: ' + str(j))
            i += 1
            print('LEAVING INNER LOOP')
            #i += 1
            #print('i = ' + str(i))
            #j = i+1
            #print('j: ' + str(j))
            #print('j = ' + str(j))

        return 'Total pairs = ' + str(countSimilarStringPairs)


"""
        while i <= len(words)-1:
            print('i: ' + str(i))
            print('j: ' + str(j))
            while j <= len(words)-1:
                for word in words:
                    print('Word: ' + word)
                    for char in word:
                        print('Checking for ' + char + ' in ' + words[j])
                        if char in words[j]:
                            stringsAreSimilar = True
                            print('Character exists in string')
                        else:
                            stringsAreSimilar = False
                            print('Character does not exist in string')
                            break

                    print('\n')

                    print('Checking if strings are similar 1')
                    if stringsAreSimilar == True:
                        for char in words[j]:
                            print('---Checking for ' + char + ' in ' + word)
                            if char in word:
                                stringsAreSimilar = True
                                print('-- Character exists in string')
                            else:
                                stringsAreSimilar = False
                                print('-- Character does not exist in string')
                                break

                    print('Checking if strings are similar 2')
                    if stringsAreSimilar == True:
                        print('*** STRINGS ARE SIMILAR INCREMENTING COUNTER ***')
                        print('countSimilarStringPairs: ' + str(countSimilarStringPairs))
                        countSimilarStringPairs += 1

                        # Reset value to False
                        stringsAreSimilar == False

                    print('FINAL countSimilarStringPairs: ' + str(countSimilarStringPairs))

                    j += 1
                    print('j: ' + str(j))

                    i += 1
                    j = i+1
                print('i: ' + str(i))

            print('Output: ' + str(countSimilarStringPairs))

            if stringsAreSimilar == True
                countSimilarStringPairs += 1

"""

obj_1 = Solution()

print(obj_1.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))

###
### not working need to make code iterate through all string to check if they are similar
###
