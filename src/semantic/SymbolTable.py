from lib2to3.pgen2.token import NUMBER


symbolTable = []
INT = 'int'
DOUBLE = 'double'
BOOL = 'boolean'
STRING = 'string'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
VARIABLE = 'var'
SCOPE = 'scope'
CLASS = 'class'

Number = [INT, DOUBLE]

Types = Number + [STRING]


def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope


def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]


def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE: type}


def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION,
                             PARAMS: params, TYPE: returnType}


def addClass(name):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: CLASS}


def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None
