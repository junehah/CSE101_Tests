import filecmp, os

def conversion():
    answer = open('Task1_Answers.txt', 'w')
    readfrom = open('Task1_input.txt','r')
    for line in readfrom:
        result = (int(line)-32)*5/9
        print result
        answer.write(str(result) + '\n')

    answer.close()
    readfrom.close()
conversion()
#conversion(20)
