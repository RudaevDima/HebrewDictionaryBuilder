#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('/home/gonzzz/Downloads/project2.txt', 'r') as myfile:
    data=myfile.read().decode('cp1255').encode('utf-8',errors='replace')
    #print data


    data2 = data.replace(r'-', r'.')
    data2 = data2.replace(r'+', r'.')
    data2 = data2.replace(r'%', r'.')
    data2 = data2.replace(r'/', r'.')
    data2 = data2.replace(r'*', r'.')
    data2 = data2.replace(r'\t', r'.')
    data2 = data2.replace(r'\n', r'.')
    data2 = data2.replace(r'\r', r'.')
    data2 = data2.replace(r'\v', r'.')
    data2 = data2.replace(r"''", r'.')
    data2 = data2.replace(" ",'.')
    data2 = data2.replace(",",'.')
    data2 = data2.replace(")", '.')
    data2 = data2.replace("(", '.')
    data2 = data2.replace("0", '.')
    data2 = data2.replace("1", '.')
    data2 = data2.replace("2", '.')
    data2 = data2.replace("3", '.')
    data2 = data2.replace("4", '.')
    data2 = data2.replace("5", '.')
    data2 = data2.replace("6", '.')
    data2 = data2.replace("7", '.')
    data2 = data2.replace("8", '.')
    data2 = data2.replace("9", '.')

    print "-------------------------------------------------------------------------------------"
    print data2

    data3=data2.split(".")
    print "-------------------------------------------------------------------------------------"
    print "-------------------------------------------------------------------------------------"
    print data3

aDict = dict()


for word in data3:

    if word != '':

        word2 = word.decode('utf-8').encode('cp1255',errors='replace')
        if word2 not in aDict :
            aDict[word2] = 1
        else:
            aDict[word2] = aDict[word2] + 1
    else:
        #print "skipping word:" + word
        pass

with open("dict.txt", "a") as outfile:

    for pair in  aDict:
        print str(aDict[pair]) + " : "+ pair.decode('cp1255').encode('utf-8',errors='replace')
        outfile.write(str(aDict[pair]) + " : "+ pair.decode('cp1255').encode('utf-8',errors='replace') + "\n")


print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
