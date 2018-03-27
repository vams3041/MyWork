import time
import random
import Calculator
import pprint

loopMax = random.randint(10,50)

print("Request for " + str(loopMax) + " maths received...Beginning mathing sequence...")

operations = ['+']

operations.append('-')
operations.append('/')
operations.append('*')

print("Operation count " + str(len(operations)))

print("Computer will maths using the following operations " + str(operations))


print('\n\n')

for index in range(1):
    firstNumber = random.randint(-99, 99)
    secondNumber = random.randint(-99, 99)

    print("Mathing with " + str(firstNumber) + " and " + str(secondNumber))


    sleepTime = 0


    print("IN FOR LOOP:")

    for operation in operations:
        print('operation = ' + operation)
        Calculator.runOperation(operation, firstNumber, secondNumber)
        print()

    print('\n')
    print("INDEX FOR LOOP")

    for i in range(len(operations)):
        print('i = ' + str(i))

        print('operation = ' + operations[i])
        Calculator.runOperation(operations[i], firstNumber, secondNumber)
        print()

    time.sleep(sleepTime)

    print('\n---------------------\n')


print("Done mathing...Goodbye!")
time.sleep(2)

print("BUT WAIT! There's more! I forgot dictionaries!")


wordsAndThingsDict = {}

wordsAndThingsDict['Apple'] = 'Red thing that tastes good. Specifically not an orange.'
wordsAndThingsDict['Orange'] = 'Makes great juice!'
wordsAndThingsDict[3] = 'The number 3'
wordsAndThingsDict['A list'] = ['oh', 'boy!', 'A list in a dictionary!']
wordsAndThingsDict['Inception'] = {'Nested': 'When one dictionary is a VALUE in a dictionary'}

print(str(wordsAndThingsDict))
print()

print("Loop")

for key, f in wordsAndThingsDict.items():
    print("Key: " + str(key))

    print("Value: " + str(f))
    print()