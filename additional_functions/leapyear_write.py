import filecmp, os

def leap_year():
    answer = open('Task2_Answers.txt', 'w')
    readfrom = open('Task2_input.txt','r')
    for line in readfrom:
        x = int(line)
        if (x%4==0 and x%100!=0):
            answer.write('true' + '\n')
        else:
            answer.write('false' + '\n')
    answer.close()
    readfrom.close()
leap_year()
