from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visitImporteConcrete(self, importeConcrete):
        pass

    @abstractmethod
    def visitClasseConcrete(self, classeConcrete):
        pass

    @abstractmethod
    def visitFuncDeclConcrete(self, funcDeclConcrete):
        pass

    @abstractmethod
    def visitStmsignatureType(self, signatureType):
        pass

    @abstractmethod
    def visitSignatureConcrete(self, signatureConcrete):
        pass

    @abstractmethod
    def visitSingleSigParams(self, singleSigParams):
        pass

    @abstractmethod
    def visitCompoundSigParams(self, compoundSigParams):
        pass

    @abstractmethod
    def visitBodyConcrete(self, bodyConcrete):
        pass

    @abstractmethod
    def visitSingleStm(self, singlestm):
        pass

    @abstractmethod
    def visitCompoundStm(self, compoundStm):
        pass

    @abstractmethod
    def visitStmWhile(self, stmWhile):
        pass

    @abstractmethod
    def visitStmExp(self, stmExp):
        pass

    @abstractmethod
    def visitStmFore(self, stmFore):
        pass

    @abstractmethod
    def visitStmReturn(self, stmReturn):
        pass

    @abstractmethod
    def visitStmClasseNew(self, injecaoClass):
        pass

    @abstractmethod
    def visitStmClasseNewParams(self, injecaoClass):
        pass

    @abstractmethod
    def visitAssignExp(self, assignExp):
        pass

    @abstractmethod
    def visitSomaExp(self, somaExp):
        pass

    @abstractmethod
    def visitSubExp(self, subExp):
        pass

    @abstractmethod
    def visitMulExp(self, mulExp):
        pass

    @abstractmethod
    def visitDivExp(self, divExp):
        pass

    @abstractmethod
    def visitDivPartExp(self, divPartExp):
        pass

    @abstractmethod
    def visitDivRestExp(self, divRestExp):
        pass

    @abstractmethod
    def visitInvertExp(self, invertExp):
        pass

    @abstractmethod
    def visitEqualsExp(self, equalsExp):
        pass

    @abstractmethod
    def visitDiffExp(self, diffExp):
        pass

    @abstractmethod
    def visitGreaterExp(self, greaterExp):
        pass

    @abstractmethod
    def visitLessExp(self, lessExp):
        pass

    @abstractmethod
    def visitGreaterEqualsExp(self, greaterEqualsExp):
        pass

    @abstractmethod
    def visitLessEqualsExp(self, lessEqualsExp):
        pass

    @abstractmethod
    def visitInvertBooleanExp(self, invertBooleanExp):
        pass

    @abstractmethod
    def visitOrExp(self, orExp):
        pass

    @abstractmethod
    def visitAndExp(self, andExp):
        pass

    @abstractmethod
    def visitPotExp(self, potExp):
        pass

    @abstractmethod
    def visitCallExp(self, callExp):
        pass

    @abstractmethod
    def visitIdExp(self, idExp):
        pass

    @abstractmethod
    def visitBooleanExp(self, booleanExp):
        pass

    @abstractmethod
    def visitNumExp(self, numExp):
        pass

    @abstractmethod
    def visitIsExp(self, isExp):
        pass

    @abstractmethod
    def visitAssignThis(self, assignThis):
        pass

    @abstractmethod
    def visitPlusPlusExp(self, plusExp):
        pass

    @abstractmethod
    def visitMinusMinusExp(self, minusExp):
        pass

    @abstractmethod
    def visitStringExp(self, stringExp):
        pass

    @abstractmethod
    def visitStmVar(self, stmExp):
        pass

    @abstractmethod
    def visitStmVariableDeclaration(self, variable):
        pass

    @abstractmethod
    def visitStmVariableDeclarationValue(self, variable):
        pass

    @abstractmethod
    def visitParamsCall(self, paramsCall):
        pass

    @abstractmethod
    def visitNoParamsCall(self, paramsCall):
        pass

    @abstractmethod
    def visitSingleParam(self, singleParam):
        pass

    @abstractmethod
    def visitCompoundParams(self, compoundParams):
        pass

    @abstractmethod
    def visitStmIfe(self, stmIfe):
        pass

    