from src.visitor.abstract_visitor import *
# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def visitImporteConcrete(self, importeConcrete):
        print (blank(), 'import "', importeConcrete.string, '";', sep='')

    def visitFuncDeclConcrete(self, funcDeclConcrete):
        funcDeclConcrete.signature.accept(self)
        funcDeclConcrete.body.accept(self)

    def visitClasseConcrete(self, classeConcrete):
        print (blank(), classeConcrete.type, ' ', end='', sep='')
        print(classeConcrete.id, end = '', sep='')
        classeConcrete.body.accept(self)

    def visitSignatureConcrete(self, signatureConcrete):
        print (blank(), signatureConcrete.type, ' ', end='', sep='')
        print(signatureConcrete.id, '(', end = '', sep='')
        if (signatureConcrete.sigParams != None):
            signatureConcrete.sigParams.accept(self)
        print(')', end = '')

    def visitSingleSigParams(self, singleSigParams):
        print(singleSigParams.type, ' ', end='', sep='')
        print(singleSigParams.id, end='', sep='')

    def visitCompoundSigParams(self, compoundSigParams):
        print(compoundSigParams.type, ' ', end='', sep='')
        print(compoundSigParams.id, ', ', end='', sep='')
        compoundSigParams.sigParams.accept(self)

    def visitBodyConcrete(self, bodyConcrete):
        global tab
        print ('{ ')
        tab =  tab + 3
        if (bodyConcrete.stms != None):
            bodyConcrete.stms.accept(self)
        tab =  tab - 3
        print (blank(), '} ', sep='')

    def visitSingleStm(self, singleStm):
        singleStm.stm.accept(self)

    def visitCompoundStm(self, compoundStm):
        compoundStm.stm.accept(self)
        compoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        print(blank(),sep='',end='')
        stmExp.exp.accept(self)
        print(';')

    def visitStmWhile(self, stmWhile):
        print (blank(), 'while (', end='', sep='')
        stmWhile.exp.accept(self)
        print (')', end='', sep='')
        stmWhile.block.accept(self)

    def visitStmReturn(self, stmReturn):
        print (blank(), 'return ', end='', sep='')
        stmReturn.exp.accept(self)
        print (';')

    def visitStmFore(self, stmFore):
        print('for(', end='', sep='')
        stmFore.exp1.accept(self)
        print(';', end='')
        stmFore.exp2.accept(self)
        print(';', end='')
        stmFore.exp3.accept(self)
        print(')')
        print(blank(), end='')
        stmFore.block.accept(self)

    def visitStmIfe(self, stmIfe):
        print(blank(), 'if(', end='', sep='')
        stmIfe.expif.accept(self)
        print(')',end ='')
        stmIfe.s11.accept(self)
        print(blank(),  end='', sep='')
        if stmIfe.s12 != None:
            print('else{')
            # print(stmIfe.s12)
            stmIfe.s12.accept(self)
            print('}')

        #s12 else

    def visitAssignExp(self, assignExp):
        # print("visitAssignExp")
        assignExp.exp1.accept(self)
        print(' = ', end='')
        assignExp.exp2.accept(self)

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
        print(' - ', end='')
        invertExp.exp.accept(self)

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
        print(' <= ', end='')
        orExp.exp2.accept(self)

    def visitAndExp(self, andExp):
        # print("visitPotExp")
        andExp.exp1.accept(self)
        print(' <= ', end='')
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

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.boolValue, end='')

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