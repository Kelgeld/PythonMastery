number = "15496254783"
cleanNumber = ''
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '34765':
        cleanNumber += number[i]

newNumber = int(cleanNumber)
print("The number is {} ".format(newNumber))

for char in number:
    if char in '2548':
        cleanedNumber += char

intCleanedNum = int(cleanedNumber)
print("The number is {} ".format(intCleanedNum))

for state in ["not pinin","no more","a stiff", "bereft of life"]:
    #print("This parrot is {} ".format(state))
    print("This parrot is "+ state)

