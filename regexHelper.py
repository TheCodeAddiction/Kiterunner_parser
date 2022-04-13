def buildResponseCodeRegex(httpCodes):
    reg = ""
    for code in httpCodes:
        reg += "\s" + code + "\s|"
    reg = reg[:-1]
    return reg


def buildHttpMethodRegex(httpMethods):
    reg = ""
    for method in httpMethods:
        reg += method + "|"
    reg = reg[:-1]
    return reg

