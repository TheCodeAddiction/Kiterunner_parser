import re
import sys

from inputHelper import getFilePath, getHttpMethods, getResponseCodes, getHelp, printHelp
from regexHelper import buildResponseCodeRegex, buildHttpMethodRegex

if getHelp(sys.argv):
    printHelp()
    quit(1)
pathToFile = getFilePath(sys.argv)
httpMethods = getHttpMethods(sys.argv)
responseCodes = getResponseCodes(sys.argv)
httpMethodReg = ""
responseCodeReg = ""

if not pathToFile:
    print("no file path, use -f to specify a path file")
    quit(1)
if httpMethods:
    httpMethodReg = buildHttpMethodRegex(httpMethods)
    file = open(pathToFile, "r")
    for line in file:
        if re.findall(httpMethodReg, line):
            print(line)
    file.close()

if responseCodes:
    responseCodeReg = buildResponseCodeRegex(responseCodes)
    file = open(pathToFile, "r")
    for line in file:
        if re.findall(responseCodeReg, line):
            print(line)
    file.close()

