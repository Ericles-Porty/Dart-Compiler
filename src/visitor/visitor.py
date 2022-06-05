from src.visitor.abstract_visitor import *
from src.semantic.SymbolTable import Types
# global tab
tab = 0


def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p


class Visitor(AbstractVisitor):

    def visitImporteConcrete(self, importeConcrete):
        print(blank(), 'import ', sep='', end='')
        importeConcrete.string.accept(self)
        print(';')

    def visitFuncDeclConcrete(self, funcDeclConcrete):
        funcDeclConcrete.signature.accept(self)
        if(funcDeclConcrete.body != None):
            funcDeclConcrete.body.accept(self)
        elif(funcDeclConcrete.body == None):
            print(';')

    def visitClasseConcrete(self, classeConcrete):
        print(blank(), classeConcrete.type, ' ', end='', sep='')
        print(classeConcrete.id, end='', sep='')
        classeConcrete.body.accept(self)

    def visitSignatureConcrete(self, signatureConcrete):
        print(blank(), signatureConcrete.type, ' ', end='', sep='')
        print(signatureConcrete.id, '(', end='', sep='')
        if (signatureConcrete.sigParams != None):
            signatureConcrete.sigParams.accept(self)
        print(')', end='')

    def visitSingleSigParams(self, singleSigParams):
        print(singleSigParams.type, ' ', end='', sep='')
        print(singleSigParams.id, end='', sep='')

    def visitCompoundSigParams(self, compoundSigParams):
        print(compoundSigParams.type, ' ', end='', sep='')
        print(compoundSigParams.id, ', ', end='', sep='')
        compoundSigParams.sigParams.accept(self)

    def visitStmsignatureType(self, signatureType):
        print(signatureType.staticT, ' ', end='', sep='')
        print(signatureType.type, ' ', end='', sep='')
        print(signatureType.id, '(', end='', sep='')
        if (signatureType.sigParams != None):
            signatureType.sigParams.accept(self)
        print(')', end='')

    def visitStmClasseNew(self, injecaoClass):
        print(blank(), end='')
        if (injecaoClass.s1 != None):
            print(injecaoClass.s1, end=' ', sep='')
        print(injecaoClass.s2, end='', sep='')
        print(end=' = ', sep='')
        injecaoClass.paramsClass.accept(self)
        print(';')

    def visitStmClasseNewParams(self, injecaoClass):
        print('new ', end='', sep='')
        print(injecaoClass.name, '(', end='', sep='')
        if (injecaoClass.paramsClass != None):
            injecaoClass.paramsClass.accept(self)
        print(')', end='')

    def visitBodyConcrete(self, bodyConcrete):
        global tab
        print('{ ')
        tab = tab + 3
        if (bodyConcrete.stms != None):
            bodyConcrete.stms.accept(self)
        tab = tab - 3
        print(blank(), '} ', sep='')

    def visitSingleStm(self, singleStm):
        singleStm.stm.accept(self)

    def visitCompoundStm(self, compoundStm):
        compoundStm.stm.accept(self)
        compoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        print(blank(), sep='', end='')
        stmExp.exp.accept(self)
        print(';')

    def visitStmVar(self, stmVar):
        stmVar.exp.accept(self)

    def visitStmVariableDeclaration(self, variable):
        # if variable.type_var in Types:
        if(variable.type_type != None):
            print(variable.type_type, ' ', end='')
        print(variable.type_var, ' ', variable.name, end='', sep='')

    def visitStmVariableDeclarationValue(self, variable):
        # if variable.type_var in Types:
        if(variable.type_type != None):
            print(variable.type_type, '', end='')
        if(variable.type_var != None):
            print(variable.type_var, end=' ')
        print(variable.name, ' = ', sep='', end='')
        variable.exp.accept(self)

    def visitStmWhile(self, stmWhile):
        print(blank(), 'while (', end='', sep='')
        stmWhile.exp.accept(self)
        print(')', end='', sep='')
        stmWhile.block.accept(self)

    def visitStmReturn(self, stmReturn):
        print(blank(), 'return ', end='', sep='')
        stmReturn.exp.accept(self)
        print(';')

    def visitStmFore(self, stmFore):
        print(blank(), 'for(', end='', sep='')
        stmFore.exp1.accept(self)
        print(';', end='')
        stmFore.exp2.accept(self)
        print(';', end='')
        stmFore.exp3.accept(self)
        print(')')
        print(blank(), end='')
        stmFore.body.accept(self)

    # def visitStmForeInline(self, stmFore):
    #     print(blank(), 'for(', end='', sep='')
    #     stmFore.exp1.accept(self)
    #     print(';', end='')
    #     stmFore.exp2.accept(self)
    #     print(';', end='')
    #     stmFore.exp3.accept(self)
    #     print(')')
    #     print(blank(), end='')
    #     stmFore.stm.accept(self)

    def visitStmIfe(self, stmIfe):
        print(blank(), 'if(', end='', sep='')
        stmIfe.expif.accept(self)
        print(')', end='')
        stmIfe.s11.accept(self)
        # print(blank(),  end='', sep='')
        if stmIfe.s12 != None:
            print(blank(),  end='', sep='')
            print('else ')
            print(blank(),  end='', sep='')
            # print(stmIfe.s12)
            stmIfe.s12.accept(self)

        # s12 else

    def visitAssignExp(self, assignExp):
        # print("visitAssignExp")
        assignExp.exp1.accept(self)
        print(' = ', end='')
        assignExp.exp2.accept(self)

    def visitAssignThis(self, assignThis):
        print("This.", end='')
        print(assignThis.s1, end='')
        print(' =', assignThis.s2, end='')
        # assignThis.s2.accept(self)

    def visitSomaExp(self, somaExp):
        # print("visitSomaExp")
        somaExp.exp1.accept(self)
        print(' + ', end='')
        somaExp.exp2.accept(self)

    def visitMulExp(self, mulExp):
        # print("visitMulExp")
        mulExp.exp1.accept(self)
        print(' * ', end='')
        mulExp.exp2.accept(self)

    def visitSubExp(self, subExp):
        # print("visitMulExp")
        subExp.exp1.accept(self)
        print(' - ', end='')
        subExp.exp2.accept(self)

    def visitPotExp(self, potExp):
        # print("visitPotExp")
        potExp.exp1.accept(self)
        print(' ^ ', end='')
        potExp.exp2.accept(self)

    def visitDivExp(self, divExp):
        # print("visitPotExp")
        divExp.exp1.accept(self)
        print(' / ', end='')
        divExp.exp2.accept(self)

    def visitDivPartExp(self, divPartExp):
        # print("visitPotExp")
        divPartExp.exp1.accept(self)
        print(' ~/ ', end='')
        divPartExp.exp2.accept(self)

    def visitDivRestExp(self, divRestExp):
        # print("visitPotExp")
        divRestExp.exp1.accept(self)
        print(' % ', end='')
        divRestExp.exp2.accept(self)

    def visitInvertExp(self, invertExp):
        # print("visitPotExp")
        print(' -(', end='', sep='')
        invertExp.exp.accept(self)
        print(')', end='')

    def visitEqualsExp(self, equalsExp):
        # print("visitPotExp")
        equalsExp.exp1.accept(self)
        print(' == ', end='')
        equalsExp.exp2.accept(self)

    def visitDiffExp(self, diffExp):
        # print("visitPotExp")
        diffExp.exp1.accept(self)
        print(' != ', end='')
        diffExp.exp2.accept(self)

    def visitGreaterExp(self, greaterExp):
        # print("visitPotExp")
        greaterExp.exp1.accept(self)
        print(' > ', end='')
        greaterExp.exp2.accept(self)

    def visitLessExp(self, lessExp):
        # print("visitPotExp")
        lessExp.exp1.accept(self)
        print(' < ', end='')
        lessExp.exp2.accept(self)

    def visitGreaterEqualsExp(self, greaterEqualsExp):
        # print("visitPotExp")
        greaterEqualsExp.exp1.accept(self)
        print(' >= ', end='')
        greaterEqualsExp.exp2.accept(self)

    def visitLessEqualsExp(self, lessEqualsExp):
        # print("visitPotExp")
        lessEqualsExp.exp1.accept(self)
        print(' <= ', end='')
        lessEqualsExp.exp2.accept(self)

    def visitInvertBooleanExp(self, invertBooleanExp):
        # print("visitPotExp")
        print(' ! ', end='')
        invertBooleanExp.exp.accept(self)

    def visitOrExp(self, orExp):
        # print("visitPotExp")
        orExp.exp1.accept(self)
        print(' || ', end='')
        orExp.exp2.accept(self)

    def visitAndExp(self, andExp):
        # print("visitPotExp")
        andExp.exp1.accept(self)
        print(' && ', end='')
        andExp.exp2.accept(self)

    def visitCallExp(self, callExp):
        # print("visitCallExp")
        callExp.call.accept(self)

    def visitNumExp(self, numExp):
        # print("visitNumExp")
        print(numExp.num, end='')

    def visitIdExp(self, idExp):
        # print("visitIdExp")
        print(idExp.id,  end='')
        # print(idExp.id, ';', end='')

    def visitStringExp(self, stringExp):
        print('"', stringExp.id, '"', end='', sep='')

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.boolValue, end='')

    def visitIsExp(self, IsExp):
        print(IsExp.exp1, ' is ', IsExp.exp2, sep='', end='')

    def visitPlusPlusExp(self, PlusExp):
        print(PlusExp.id, '++', end='', sep='')

    def visitMinusMinusExp(self, MinusExp):
        print(MinusExp.id, '--', end='', sep='')

    def visitParamsCall(self, paramsCall):
        # print("visitParamsCall")
        print(paramsCall.id, '(', end='', sep='')
        paramsCall.params.accept(self)
        print(')', end='')

    def visitNoParamsCall(self, simpleCall):
        # print("visitSimpleCall")
        print(blank(), simpleCall.id, '()', end='', sep='')

    def visitCompoundParams(self, compoundParams):
        # print("visitCompoundParams")
        compoundParams.exp.accept(self)
        print(', ', end='')
        compoundParams.params.accept(self)

    def visitSingleParam(self, singleParam):
        # print("visitSingleParam")
        singleParam.exp.accept(self)
