import filecmp, os

def summation():
    answer = open('Task3_Answers.txt', 'w')
    readfrom = open('Task3_input.txt','r')
    for line in readfrom:
        x = int(line)
        summ = 0
        for i in range (1, x+1):
            summ=summ+i
        answer.write(str(summ) + '\n')
    answer.close()
    readfrom.close()
summation()
