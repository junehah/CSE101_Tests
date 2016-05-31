#!/usr/bin/python
#!python
# -*- coding: utf-8 -*-
# Author - June Hah
import os, sys, shutil, imp
#--solutions
from sum_test import summation
from leap_year_test import leap_year
from conversion_test import conversion
from prime_test import prime
from RPS import playRockPaperScissors
#--file that creates folders with ubitname as title recursively
#from cse101_recursive_mkdir.py import createFolders
inputPath = os.getenv('HOME') + '/Documents/101'
path = os.getenv('HOME') + '/Documents/101/lab8'
os.chdir('/home/jables/Documents/101/lab8/')

def createFolders():
    for f in os.listdir(path):
        f_name, f_ext = os.path.splitext(f)
        counter = 0
        i = 0
        #extracting ubitname ==> will be in variable name
        name = f_name
        name = name[6:]
        while name[i]!='_' and i!= len(f_name):
            counter = counter + 1
            i = i + 1
        name = name[:counter]
        #creating folder with ubitname as its title
        #in the chance the assignment requires multiple files, code will avoid
        #making duplicate folders: hence the try-catch statements
        try:
            os.mkdir(name)
            print('\033[1;33m'+'--------'+'folder made'+'--------'+'\033[0;0m')
        except:
            print('\033[1;33m'+'--------'+'folder already made.  ignoring duplicate'+'--------'+'\033[0;0m')

        #moving folders into the made folders
        #this part is NOT in the try in case of duplicate folders
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

    for folder in os.listdir(path):
        tempPath = path + '/' + folder
        print ('\033[1;43m'+'--------' + folder+'--------' + '\033[0;0m')
        #writing to the output file for clarification
        result.write('--------'+folder+'--------\n')
        for f in os.listdir(tempPath):
            if 'Task1' in str(f):
                count = 0
                fileCount = 0
                try:
                    module = imp.load_source('convertFtoC', tempPath + '/' + f)
                    for line in problem1:
                        #print('\033[1;33m'+"task1"+'\033[0;0m')
                        fileCount = fileCount + 1
                        studentX = module.convertFtoC(int(line))
                        studentVersion1.write(str(studentX) + '\n')
                        solutionY = conversion(int(line))
                        mySolution1.write(str(solutionY) + '\n')
                        if studentX == solutionY:
                            count = count + 1
                    if count == fileCount:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Task 1 -' + '\033[1;32m'+'passed'+'\033[0;0m')
                        result.write(folder + ' Task 1---Passed\n')
                    else:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Task 1 -' + '\033[1;31m'+'failed'+'\033[0;0m')
                        result.write(folder + ' Task 1---Failed\n')
                except:
                    print('\033[1;33m'+'--Task1.pyc already exists'+'\033[0;0m')
            #print('\033[1;31m'+'------task 2 checks--'+'\033[0;0m')
            elif 'Task2' in str(f):
                count = 0
                fileCount = 0
                try:
                    module = imp.load_source('isLeapYear', tempPath + '/' + f)
                    #for each line in the input.txt
                    for line in problem2:
                        fileCount = fileCount + 1
                        studentX = module.isLeapYear(int(line))
                        solutionY = leap_year(int(line))
                        if studentX == solutionY:
                            count = count + 1
                    if count == fileCount:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Task 2 -' + '\033[1;32m'+'passed'+'\033[0;0m')
                        result.write(folder + ' Task 2---Passed\n')
                    else:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Task 2 -' + '\033[1;31m'+'failed'+'\033[0;0m')
                        result.write(folder + ' Task 2---Failed\n')
                except:
                    print('\033[1;33m'+'--Task2.pyc already exists'+'\033[0;0m')
            #print('\033[1;36m'+'------task 3 checks--'+'\033[0;0m')
            elif 'Task3' in str(f):
                #loading in the function from a particular file
                count = 0
                fileCount = 0
                try:
                    module = imp.load_source('sumUpTo', tempPath + '/' + f)
                    for line in problem3:
                        fileCount = fileCount + 1
                        studentX = module.sumUpTo(int(line))
                        solutionY = summation(int(line))
                        if studentX == solutionY:
                            count = count + 1
                    if count == fileCount:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Task 3 -' + '\033[1;32m'+'passed'+'\033[0;0m')
                        result.write(folder + ' Task 3---Passed\n')
                    else:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Task 3 -' + '\033[1;31m'+'failed'+'\033[0;0m')
                        result.write(folder + ' Task 3---Failed\n')
                except:
                    print('\033[1;33m'+'--Task3.pyc already exists'+'\033[0;0m')
            elif 'Extra_Credit1' in str(f):
                count = 0
                fileCount = 0
                try:
                    module = imp.load_source('isPrime', tempPath + '/' + f)
                    for line in primeProblem:
                        fileCount = fileCount + 1
                        studentX = module.isPrime(int(line))
                        solutionY = prime(int(line))
                        if studentX == solutionY:
                            count = count + 1
                    if count == fileCount:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Extra Credit 1 -' + '\033[1;32m'+'passed'+'\033[0;0m')
                        result.write(folder + ' Extra Credit 1---Passed\n')
                    else:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Extra Credit 1 -' + '\033[1;31m'+'failed'+'\033[0;0m')
                        result.write(folder + ' Extra Credit 1---Failed\n')
                except:
                    print('\033[1;33m'+'--Extra_Credit1.pyc already exists'+'\033[0;0m')
            elif 'Extra_Credit2' in str(f):
                count = 0
                fileCount = 0
                try:
                    module = imp.load_source('playRockPaperScissors', tempPath + '/' + f)
                    for line in rpcProblem:
                        fileCount = fileCount + 1
                        studentX = module.playRockPaperScissors(int(line))
                        solutionY = prime(int(line))
                        if studentX == solutionY:
                            count = count + 1
                    if count == fileCount:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Extra Credit 2 -' + '\033[1;32m'+'passed'+'\033[0;0m')
                        result.write(folder + ' Extra Credit 2---Passed\n')
                    else:
                        print ('\033[1;36m'+folder+'\033[0;0m' + '-' + ' Extra Credit 2 -' + '\033[1;31m'+'failed'+'\033[0;0m')
                        result.write(folder + ' Extra Credit 2---Failed\n')
                except:
                    print('\033[1;33m'+'--Extra_Credit2.pyc already exists'+'\033[0;0m')
            else:
                print ('\033[1;36m'+folder+'\033[0;0m' + '-' + 'No python files found-' + '\033[1;31m'+'failed'+'\033[0;0m')
                result.write(folder + 'No python files found---Failed\n')
    #--closing files
    problem1.close()
    problem2.close()
    problem3.close()
    primeProblem.close()
    rpcProblem.close()
    result.close()

python_test()
