#!/usr/bin/python
#!python
# -*- coding: utf-8 -*-
# Author - June Hah

import os, sys, shutil, imp
from subprocess import check_call

#--solutions
from solutions.conversion_test import conversion
from solutions.sum_test import summation
from solutions.prime_test import prime
from solutions.RPS import playRPS
from solutions.leap_year_test import leap_year

#--Paths - (CHANGE THIS IF NEEDED)
path = os.getenv('HOME') + '/Documents/101/lab8'
inputPath = os.getenv('HOME') + '/Documents/101/test_cases'
os.chdir('/home/jables/Documents/101/lab8/')

#--recursively creates folders based on their UBITNAMEs
def createFolders():
    for f in os.listdir(path):
        f_name, f_ext = os.path.splitext(f)
        counter = 0
        i = 0
        #--extracting ubitname ==> will be in variable name
        name = f_name
        name = name[6:]
        while name[i]!='_' and i!= len(f_name):
            counter = counter + 1
            i = i + 1
        name = name[:counter]
        #--creating folder with ubitname as its title
        #--in the chance the assignment requires multiple files, code will avoid
        #--making duplicate folders: hence the try-catch statements
        try:
            os.mkdir(name)
            print('\033[1;33m'+'--------'+'folder made'+'--------'+'\033[0;0m')
        except:
            print('\033[1;33m'+'--------'+'folder already made.  ignoring duplicate'+'--------'+'\033[0;0m')

        #--moving folders into the made folders
        #--this part is NOT in the try in case of duplicate folders
        if name in f_name:
            old = str(path) + '/' + str(f_name) + f_ext
            new = str(path) + '/' + str(name) + '/' + str(f_name) + f_ext
            shutil.move(old, new)

def python_test():
    #--recursively creates folders
    try:
        createFolders()
    except:
        print('\033[1;33m'+'--folder already created!'+'\033[0;0m')

    #--opening the test cases
    problem1 = open(inputPath + '/Task1_input.txt', 'r')
    problem2 = open(inputPath + '/Task2_input.txt', 'r')
    problem3 = open(inputPath + '/Task3_input.txt', 'r')
    primeProblem = open(inputPath + '/EC_Task4_input.txt', 'r')
    rpcProblem = open(inputPath + '/EC_Task5_input.txt', 'r')
    result = open(inputPath + '/output.txt', 'w')

    #--Actual part of the script to run files
    #--If there is compilation error, it will skip it.  Meaning it wont appear
    #     on terminal nor output.txt
    for folder in os.listdir(path):
        tempPath = path + '/' + folder
        noop = 0
        print ('\033[1;43m'+'--------' + folder+'--------' + '\033[0;0m')
        result.write("-----" + folder + "-----\n")
        for f in os.listdir(tempPath):
            #--checking if there isa Task1 file
            if 'Task1' in str(f):
                if 'Task1.pyc' in str(f):
                    noop = 0
                else:
                    print ('\033[1;35m'+'-------- Task 1 --------' + '\033[0;0m')
                    result.write('******** Task 1 ********\n')
                    count = 0
                    fileCount = 0
                    try:
                        module = imp.load_source('convertFtoC', tempPath + '/' + f)
                        for line in problem1:
                            tempLine = line.replace('\n', '')
                            fileCount = fileCount + 1
                            studentX = module.convertFtoC(int(line))
                            solutionY = conversion(int(line))
                            if studentX == solutionY:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;32m'+'passed'+'\033[0;0m')
                                result.write(tempLine + ' === passed\n')
                            else:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;31m'+'failed'+'\033[0;0m')
                                result.write(tempLine + ' === failed\n')
                    except:
                        noop = 0
                        #print('\033[1;33m'+'--Task1.pyc already exists'+'\033[0;0m')

            #--checking if there is a Task2 file
            elif 'Task2' in str(f):
                if 'Task2.pyc' in str(f):
                    noop = 0
                else:
                    print ('\033[1;35m'+'-------- Task 2 --------' + '\033[0;0m')
                    result.write('******** Task 2 ********\n')
                    count = 0
                    fileCount = 0
                    try:
                        module = imp.load_source('isLeapYear', tempPath + '/' + f)
                        #--for each line in the input.txt
                        for line in problem2:
                            tempLine = line.replace('\n', '')
                            fileCount = fileCount + 1
                            studentX = module.isLeapYear(int(tempLine))
                            solutionY = leap_year(int(tempLine))
                            if studentX == solutionY:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;32m'+'passed'+'\033[0;0m')
                                result.write(tempLine + ' === passed\n')
                            else:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;31m'+'failed'+'\033[0;0m')
                                result.write(tempLine + ' === failed\n')
                    #--this final except is to allow the code to recompile after initial compilation
                    #except SyntaxError:
                        #print ("task 2 syntax error")
                    except:
                        noop = 0
                        #print('\033[1;33m'+'--Task2.pyc already exists'+'\033[0;0m')

            #--checking if there is a Task3 file
            elif 'Task3' in str(f):
                if 'Task3.pyc' in str(f):
                    noop = 0
                else:
                    print ('\033[1;35m'+'-------- Task 3--------' + '\033[0;0m')
                    result.write('******** Task 3 ********\n')
                    count = 0
                    fileCount = 0
                    try:
                        module = imp.load_source('sumUpTo', tempPath + '/' + f)
                        for line in problem3:
                            tempLine = line.replace('\n', '')
                            fileCount = fileCount + 1
                            studentX = module.sumUpTo(int(line))
                            solutionY = summation(int(line))
                            if studentX == solutionY:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;32m'+'passed'+'\033[0;0m')
                                result.write(tempLine + ' === passed\n')
                            else:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;31m'+'failed'+'\033[0;0m')
                                result.write(tempLine + ' === failed\n')
                    except:
                        noop = 0
                        #print('\033[1;33m'+'--Task3.pyc already exists'+'\033[0;0m')

            elif 'Extra_Credit1' in str(f):
                if 'Extra_Credit1.pyc' in str(f):
                    noop = 0
                else:
                    print ('\033[1;35m'+'-------- Extra Credit 1--------' + '\033[0;0m')
                    result.write('******** Extra Credit 1 ********\n')
                    count = 0
                    fileCount = 0
                    try:
                        module = imp.load_source('isPrime', tempPath + '/' + f)
                        for line in primeProblem:
                            tempLine = line.replace('\n', '')
                            fileCount = fileCount + 1
                            studentX = module.isPrime(int(line))
                            solutionY = prime(int(line))
                            if studentX == solutionY:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;32m'+'passed'+'\033[0;0m')
                                result.write(tempLine + ' === passed\n')
                            else:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;31m'+'failed'+'\033[0;0m')
                                result.write(tempLine + ' === failed\n')
                    except:
                        noop = 0
                        #print('\033[1;33m'+'--Extra_Credit1.pyc already exists'+'\033[0;0m')

            elif 'Extra_Credit2' in str(f):
                if 'Extra_Credit2.pyc' in str(f):
                    noop = 0
                else:
                    print ('\033[1;35m'+'-------- Extra Credit 2--------' + '\033[0;0m')
                    result.write('******** Extra Credit 2 ********\n')
                    count = 0
                    fileCount = 0
                    try:
                        module = imp.load_source('playRockPaperScissors', tempPath + '/' + f)
                        for line in rpcProblem:
                            tempLine = line.replace('\n', '')
                            fileCount = fileCount + 1
                            studentX = module.playRockPaperScissors(int(line))
                            solutionY = playRPS(int(line))
                            if studentX == solutionY:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;32m'+'passed'+'\033[0;0m')
                                result.write(tempLine + ' === passed\n')
                            else:
                                print ('Input ''\033[1;36m'+tempLine+'\033[0;0m' + '-' + '\033[1;31m'+'failed'+'\033[0;0m')
                                result.write(tempLine + ' === failed\n')
                    except:
                        noop = 0
                        #print('\033[1;33m'+'--Extra_Credit2.pyc already exists'+'\033[0;0m')
            else:
                print ('\033[1;36m'+folder+'\033[0;0m' + '-' + 'No python files found-' + '\033[1;31m'+'failed'+'\033[0;0m')
                result.write(folder + '- No python files found---Failed\n')
                dontCheck = 1

    #--closing files
    problem1.close()
    problem2.close()
    problem3.close()
    primeProblem.close()
    rpcProblem.close()
    result.close()

#--function call
python_test()
