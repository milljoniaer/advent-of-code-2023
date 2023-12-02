import re

TEST = True
INPUT = 'test-input-2.txt' if TEST else 'input-2.txt'

file1 = open(INPUT, 'r')
Lines = file1.readlines()

def sanitize_digits(line):
    digitsWritten = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(line)):
        for index, digitWritten in enumerate(digitsWritten): 
            current_part = line[0:i]
            current_part = current_part.replace(digitWritten, str(index + 1))
            line = current_part + line [i:]
            i = len(current_part)
    print(line)
    return line
 
sum = 0
for line in Lines:
    line = sanitize_digits(line)
    firstDigit = re.match(r'.*?(\d)', line).group(1)
    lastDigit = re.match(r'.*?(\d)(?=[^\d]*$)', line).group(1)
    calibrationValue = int(firstDigit) * 10 + int(lastDigit)
    print(calibrationValue)
    sum += calibrationValue

print("Sum: " + str(sum))
    