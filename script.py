#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator
import re

infile_path = "/home/gonzzz/Downloads/project2.txt"
outfile_path = "dict.txt"

with open(infile_path, 'r') as text_file:
    data=text_file.read().decode('cp1255').encode('utf-8', errors='replace')
    #print data

    data = data.replace(r'-', r'.')
    data = data.replace(r'+', r'.')
    data = data.replace(r'%', r'.')
    data = data.replace(r'/', r'.')
    data = data.replace(r'*', r'.')
    data = data.replace('\t', r'.')
    data = data.replace('\n', r'.')
    data = data.replace('\r', r'.')
    data = data.replace('\v', r'.')
    data = data.replace(r"''", r'.')
    data = data.replace(" ", '.')
    data = data.replace(",", '.')
    data = data.replace(")", '.')
    data = data.replace("(", '.')
    data = data.replace("0", '.')
    data = data.replace("1", '.')
    data = data.replace("2", '.')
    data = data.replace("3", '.')
    data = data.replace("4", '.')
    data = data.replace("5", '.')
    data = data.replace("6", '.')
    data = data.replace("7", '.')
    data = data.replace("8", '.')
    data = data.replace("9", '.')

    print "--------------------------------- data after striping  ------------------------------------"
    print data

    data=data.split(".")
    print "--------------------------------- data after spliting  -------------------------------------"
    print data

aDict = dict()


for word in data:

    if word != '' and  not re.search('[a-zA-Z]', word):

        word = word.decode('utf-8').encode('cp1255', errors='replace')

        if word not in aDict :
            aDict[word] = 1
        else:
            aDict[word] = aDict[word] + 1
    else:
        #print "skipping word:" + word
        pass

with open(outfile_path, "a") as outfile:

    sortedList = sorted(aDict.items(), key=operator.itemgetter(1))

    for t in sortedList:
        print t[0].decode('cp1255').encode('utf-8',errors='replace') + ":" + str(t[1])
        outfile.write(t[0].decode('cp1255').encode('utf-8',errors='replace') + ":" + str(t[1]) )
        outfile.write("\n")

print "------------------------- Done , results written to " + outfile_path + "---------------------------"
