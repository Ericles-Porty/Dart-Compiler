from abc import abstractmethod
from abc import ABCMeta

'''
Declaracao de import
import
'''


class Importe(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ImporteConcrete(Importe):
    def __init__(self, string):
        self.string = string

    def accept(self, visitor):
        return visitor.visitImporteConcrete(self)


'''
Declaracao de funcao
FuncDecl
'''


class FuncDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body

    def accept(self, visitor):
        return visitor.visitFuncDeclConcrete(self)


'''
Assinatura de classe
Classe
'''


class Classe(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ClasseConcrete(Classe):
    def __init__(self, type, id, body):
        self.type = type
        self.id = id
        self.body = body

    def accept(self, visitor):
        return visitor.visitClasseConcrete(self)


'''
Assinatura de funcao
Signature
'''


class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SignatureConcrete(Signature):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams

    def accept(self, visitor):
        return visitor.visitSignatureConcrete(self)


'''
Parametros de assinatura de funcao
SigParams
'''


class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleSigParams(SigParams):
    def __init__(self, type, id):
        self.type = type
        self.id = id

    def accept(self, visitor):
        return visitor.visitSingleSigParams(self)


class CompoundSigParams(SigParams):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams

    def accept(self, visitor):
        return visitor.visitCompoundSigParams(self)

class StmsignatureType(SigParams):
    def __init__(self, staticT, type, id, sigParams):
        self.staticT = staticT
        self.type = type
        self.id = id
        self.sigParams = sigParams

    def accept(self, visitor):
        return visitor.visitStmsignatureType(self)


'''
Corpo de uma funcao
Body
'''


class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BodyConcrete(Body):
    def __init__(self, stms):
        self.stms = stms

    def accept(self, visitor):
        return visitor.visitBodyConcrete(self)


'''
Comandos
Stms
'''


class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SingleStm(Stms):
    def __init__(self, stm):
        self.stm = stm

    def accept(self, visitor):
        return visitor.visitSingleStm(self)


class CompoundStm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms

    def accept(self, visitor):
        return visitor.visitCompoundStm(self)


'''
Comando
Stm
'''


class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitStmExp(self)


class StmVar(Stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitStmVar(self)


class StmVariableDeclaration(Stm):
    def __init__(self, type_type, type_var, name):
        self.type_type = type_type
        self.type_var = type_var
        self.name = name

    def accept(self, visitor):
        return visitor.visitStmVariableDeclaration(self)

class StmVariableDeclarationValue(Stm):
    def __init__(self, type_type, type_var, name, exp):
        self.type_type = type_type
        self.type_var = type_var
        self.name = name
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitStmVariableDeclarationValue(self)

class StmWhile(Stm):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block

    def accept(self, visitor):
        return visitor.visitStmWhile(self)


class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitStmReturn(self)


class StmFore(Stm):
    def __init__(self, exp1, exp2, exp3, body):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.body = body

    def accept(self, visitor):
        return visitor.visitStmFore(self)

# class StmForeInline(Stm):
#     def __init__(self, exp1, exp2, exp3, stm):
#         self.exp1 = exp1
#         self.exp2 = exp2
#         self.exp3 = exp3
#         self.stm = stm

#     def accept(self, visitor):
#         return visitor.visitStmForeInline(self)


class StmIfe(Stm):
    def __init__(self, expif, s11, s12):
        self.expif = expif
        self.s11 = s11
        self.s12 = s12

    def accept(self, visitor):
        return visitor.visitStmIfe(self)

class StmClasseNew(Stm):
    def __init__(self, s1, s2, paramsClass):
        self.s1 = s1
        self.s2 = s2
        self.paramsClass = paramsClass

    def accept(self, visitor):
        return visitor.visitStmClasseNew(self)

class StmClasseNewParams(Stm):
    def __init__(self, s1, paramsClass):
        self.s1 = s1
        self.paramsClass = paramsClass

    def accept(self, visitor):
        return visitor.visitStmClasseNewParams(self)

'''
Expressoes
Exp
'''


class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitAssignExp(self)


class AssignThis(Exp):
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def accept(self, visitor):
        return visitor.visitAssignThis(self)


class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitSomaExp(self)


class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMulExp(self)


class SubExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitSubExp(self)


class PotExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitPotExp(self)


class DivExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDivExp(self)


class DivPartExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDivPartExp(self)


class DivRestExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDivRestExp(self)


class InvertExp(Exp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitInvertExp(self)


class EqualsExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitEqualsExp(self)


class DiffExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDiffExp(self)


class GreaterExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitGreaterExp(self)


class LessExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitLessExp(self)


class GreaterEqualsExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitGreaterEqualsExp(self)


class LessEqualsExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitLessEqualsExp(self)


class InvertBooleanExp(Exp):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitInvertBooleanExp(self)


class OrExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitOrExp(self)


class AndExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitAndExp(self)


class CallExp(Exp, Stm):
    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        return visitor.visitCallExp(self)


class NumExp(Exp):
    def __init__(self, num):
        self.num = num

    def accept(self, visitor):
        return visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitIdExp(self)


class StringExp(Exp):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitStringExp(self)


class BooleanExp(Exp):
    def __init__(self, boolValue):
        self.boolValue = boolValue

    def accept(self, visitor):
        return visitor.visitBooleanExp(self)


class IsExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitIsExp(self)

class PlusPlusExp(Exp):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitPlusPlusExp(self)


'''
Chamada de funcao
Call
'''


class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class ParamsCall(Call):
    def __init__(self, id, params):
        self.id = id
        self.params = params

    def accept(self, visitor):
        return visitor.visitParamsCall(self)


class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitNoParamsCall(self)


'''
Parametros de uma chamada de funcao
Params
'''


class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params

    def accept(self, visitor):
        return visitor.visitCompoundParams(self)


class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitSingleParam(self)
