import re
import sys

from inputHelper import getFilePath, getHttpMethods, getResponseCodes
from regexHelper import buildResponseCodeRegex, buildHttpMethodRegex

pathToFile = getFilePath(sys.argv)
httpMethods = getHttpMethods(sys.argv)
responseCodes = getResponseCodes(sys.argv)

responseCodeReg = buildResponseCodeRegex(responseCodes)
httpMethodReg = buildHttpMethodRegex(httpMethods)
file = open(pathToFile, "r")
for line in file:
    if re.findall(httpMethodReg, line):
        print(line)
