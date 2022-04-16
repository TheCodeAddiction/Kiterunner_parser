def getFilePath(user_arguments):
    amountOfArgs = len(user_arguments)
    fileFlag = "-f"
    for i in range(amountOfArgs):
        if user_arguments[i] == fileFlag:
            return user_arguments[i + 1]
    return 0


def getHelp(user_arugments):
    helpFlag = "-h"
    helpFlagv2 = "--help"
    for arg in user_arugments:
        if arg == helpFlag or arg == helpFlagv2:
            return True
    return False


def printHelp():
    print('-f <path_output_file>\tspesifiy the file you want filtered\n')
    print('-hm method1,method2,method3...\tfilters on HTTP methods (GET, POST etc.)\n')
    print('-c code1,code2,code3...\tfilters on HTTP Reponse code (200,404,301 etc.)\n')
    print('-h or --help prints this message\n')


def getHttpMethods(user_arguments):
    amountOfArgs = len(user_arguments)
    httpFlag = "-hm"
    for i in range(amountOfArgs):
        if user_arguments[i] == httpFlag:
            arr = user_arguments[i + 1].split(",")
            return arr
    return False


def getResponseCodes(user_arguments):
    amountOfArgs = len(user_arguments)
    responseCodeFlag = "-c"
    for i in range(amountOfArgs):
        if user_arguments[i] == responseCodeFlag:
            arr = user_arguments[i + 1].split(",")
            return arr
    return False
