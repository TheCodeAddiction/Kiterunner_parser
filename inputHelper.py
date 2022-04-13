def getFilePath(user_arguments):
    amountOfArgs = len(user_arguments)
    fileFlag = "-f"
    for i in range(amountOfArgs):
        if user_arguments[i] == fileFlag:
            return user_arguments[i + 1]
    return 0


def getHttpMethods(user_arguments):
    amountOfArgs = len(user_arguments)
    httpFlag = "-h"
    for i in range(amountOfArgs):
        if user_arguments[i] == httpFlag:
            arr = user_arguments[i + 1].split(",")
            return arr
    return 0


def getResponseCodes(user_arguments):
    amountOfArgs = len(user_arguments)
    responseCodeFlag = "-c"
    for i in range(amountOfArgs):
        if user_arguments[i] == responseCodeFlag:
            arr = user_arguments[i + 1].split(",")
            return arr
    return 0
