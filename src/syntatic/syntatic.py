import ply.yacc as yacc
from src.tokens import *
from src.syntatic.syntax_abstract import *


def p_header(p):
    '''import : program
                | IMPORT string SEMICOLON
                | IMPORT string SEMICOLON import
                '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = [ImporteConcrete(p[2])]
    elif(len(p) == 5):
        p[0] = [ImporteConcrete(p[2])] + p[4]


def p_program(p):
    '''program : funcdecl
                | funcdecl program                
                | classe
                | classe program
                '''
    if (len(p) == 3):
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]


def p_classe(p):
    '''classe : CLASS ID body
              '''
    p[0] = ClasseConcrete(p[1], p[2], p[3])

def p_funcdecl(p):
    '''funcdecl : signature body '''
    p[0] = FuncDeclConcrete(p[1], p[2])

def p_funcdeclOne(p):
    '''funcdecl : signature SEMICOLON'''
    p[0] = FuncDeclConcrete(p[1], None)

def p_signatureType(p):
    '''signature : ID ID ID LPAREN sigparams RPAREN
                 | ID ID ID LPAREN RPAREN'''
    if (isinstance(p[5], SigParams)):
        p[0] = StmsignatureType(p[1], p[2], p[3], p[5])
    else:
        p[0] = StmsignatureType(p[1], p[2], p[3], None)

def p_signature(p):
    '''signature : ID ID LPAREN sigparams RPAREN
                 | ID ID LPAREN RPAREN'''
    if (isinstance(p[4], SigParams)):
        p[0] = SignatureConcrete(p[1], p[2], p[4])
    else:
        p[0] = SignatureConcrete(p[1], p[2], None)


def p_sigparams(p):
    '''sigparams : ID ID
                  | ID ID COMMA sigparams
    '''
    if (len(p) == 3):
        p[0] = SingleSigParams(p[1], p[2])
    else:
        p[0] = CompoundSigParams(p[1], p[2], p[4])


def p_body(p):
    ''' body : LKEY stms RKEY
             | LKEY RKEY
             | stms'''
    if (len(p) == 4):
        p[0] = BodyConcrete(p[2])
    elif (len(p) == 3):
        p[0] = BodyConcrete(None)
    elif (len(p) == 2):
        p[0] = BodyConcrete(p[1])


def p_stms(p):
    ''' stms : stm
            | stm stms'''
    if (len(p) == 2):
        p[0] = SingleStm(p[1])
    else:
        p[0] = CompoundStm(p[1], p[2])


def p_variables(p):
    ''' exp17 : variableDeclaration '''
    p[0] = StmVar(p[1])


def p_variableDeclaration(p):
    ''' variableDeclaration : ID ID'''
    p[0] = StmVariableDeclaration(None, p[1], p[2])

def p_variableDeclarationType(p):
    '''variableDeclaration : ID ID ID'''
    print("2")
    p[0] = StmVariableDeclaration(p[1], p[2], p[3])

def p_variableDeclarationValue(p):
    ''' variableDeclaration : ID ID ASSIGN exp17 
                 '''
    p[0] = StmVariableDeclarationValue(None, p[1], p[2], p[4])

def p_variableDeclarationValueType(p):
    ''' variableDeclaration : ID ID ID ASSIGN exp17 
                 '''
    p[0] = StmVariableDeclarationValue(p[1], p[2], p[3], p[5])


def p_while(p):
    ''' stm : WHILE LPAREN exp RPAREN body
    '''
    p[0] = StmWhile(p[3], p[5])


def p_exp(p):
    ''' stm :  exp SEMICOLON
    '''
    p[0] = StmExp(p[1])


def p_for(p):
    ''' stm : FOR LPAREN variableDeclaration SEMICOLON exp SEMICOLON exp RPAREN body
        | FOR LPAREN exp SEMICOLON exp SEMICOLON exp RPAREN body
    '''
    p[0] = StmFore(p[3], p[5], p[7], p[9])


# def p_forInline(p):
#     ''' stm : FOR LPAREN variableDeclaration SEMICOLON exp SEMICOLON exp RPAREN stm
#         | FOR LPAREN exp SEMICOLON exp SEMICOLON exp RPAREN stm
#     '''
#     p[0] = StmForeInline(p[3], p[5], p[7], p[9])


def p_return(p):
    ''' stm : RETURN exp SEMICOLON
    '''
    p[0] = StmReturn(p[2])


def p_class_new(p):
    '''stm : ID ID ASSIGN paramsClass SEMICOLON
             | ID ASSIGN paramsClass SEMICOLON
            '''
    if(len(p) == 4):
        p[0] = StmClasseNew(p[1], p[2], None)
    elif(len(p) == 5):
        p[0] = StmClasseNew(None, p[1], p[3])

def p_exp_class(p):
    ''' exp17 : paramsClass '''
    p[0] = p[1]

def p_class_new_params(p):
    '''paramsClass : NEW ID LPAREN paramsClass RPAREN
                    | NEW ID LPAREN exp17 RPAREN
                    | NEW ID LPAREN RPAREN
              '''
    if (len(p) == 6):
        p[0] = StmClasseNewParams(p[2], p[4])
    else:
        p[0] = StmClasseNewParams(p[2], None)


def p_ife(p):
    '''stm : s'''
    p[0] = p[1]


def p_s(p):
    ''' s :   s1 
            | s2 '''
    p[0] = p[1]


def p_s1_if0(p):
    ''' s1 : stms 
    '''
    p[0] = p[1]


def p_s1_if1(p):
    ''' s1 :  IF LPAREN exp RPAREN s1 ELSE s1 
    '''
    p[0] = StmIfe(p[3], p[5], p[7])


def p_s1_if2(p):
    ''' s1 :  IF LPAREN exp RPAREN body ELSE body 
    '''
    p[0] = StmIfe(p[3], p[5], p[7])


def p_s1_if3(p):
    ''' s1 :  IF LPAREN exp RPAREN s1 ELSE body 
    '''
    p[0] = StmIfe(p[3], p[5], p[7])


def p_s1_if4(p):
    ''' s1 :  IF LPAREN exp RPAREN body ELSE s1 
    '''
    p[0] = StmIfe(p[3], p[5], p[7])


def p_s2_if1(p):
    ''' s2 :  IF LPAREN exp RPAREN s  
    '''
    p[0] = StmIfe(p[3], p[5], None)


def p_s2_if2(p):
    ''' s2 :  IF LPAREN exp RPAREN body 
    '''
    p[0] = StmIfe(p[3], p[5], None)


def p_s2_if3(p):
    ''' s2 :  IF LPAREN exp RPAREN s1 ELSE s2 
    '''
    p[0] = StmIfe(p[3], p[5], p[7])


def p_s2_if4(p):
    ''' s2 :  IF LPAREN exp RPAREN body ELSE s2
    '''
    p[0] = StmIfe(p[3], p[5], p[7])


def p_exp_assign(p):
    ''' exp :   exp ASSIGN exp1
              | exp1'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = AssignExp(p[1], p[3])


def p_exp1_sum(p):
    '''exp1 : exp1 SUM exp2
         | exp2'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = SomaExp(p[1], p[3])


def p_exp2_sub(p):
    '''exp2 : exp2 SUB exp3
            | exp3'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = SubExp(p[1], p[3])


def p_exp3_times(p):
    '''exp3 : exp4 TIMES exp3
            | exp4'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = MulExp(p[1], p[3])


def p_exp4_div(p):
    '''exp4 : exp5 DIV exp4
            | exp5'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = DivExp(p[1], p[3])


def p_exp5_div_part_int(p):
    '''exp5 : exp6 DIV_PART_INT exp5
            | exp6'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = DivPartExp(p[1], p[3])


def p_exp6_div_rest(p):
    '''exp6 : exp7 DIV_REST exp6
            | exp7'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = DivRestExp(p[1], p[3])


def p_exp7_invert_signal(p):
    '''exp7 : SUB LPAREN exp RPAREN 
            | exp8'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = InvertExp(p[3])


def p_exp8_equals(p):
    '''exp8 : exp9 EQUALS exp8  
            | exp9'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = EqualsExp(p[1], p[3])


def p_exp9_diff(p):
    '''exp9 : exp10 DIFF exp9  
            | exp10'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = DiffExp(p[1], p[3])


def p_exp10_greater(p):
    '''exp10 : exp11 GREATER exp10  
            | exp11'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = GreaterExp(p[1], p[3])


def p_exp11_less(p):
    '''exp11 : exp12 LESS exp11 
            | exp12'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = LessExp(p[1], p[3])


def p_exp12_greater_equals(p):
    '''exp12 : exp13 GREATER_EQ exp12 
            | exp13'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = GreaterEqualsExp(p[1], p[3])


def p_exp13_less_equals(p):
    '''exp13 : exp14 LESS_EQ exp13 
            | exp14'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = LessEqualsExp(p[1], p[3])


def p_exp14_invert_expr(p):
    '''exp14 : INVERT_EXPR LPAREN exp RPAREN
            | exp15'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = InvertBooleanExp(p[3])


def p_exp15_or(p):
    '''exp15 : exp16 OR exp15
            | LPAREN exp16 OR exp15 RPAREN
            | exp16'''
    if len(p) == 4:
        p[0] = OrExp(p[1], p[3])
    elif len(p) == 6:
        p[0] = OrExp(p[2], p[4])
    else:
        p[0] = p[1]


def p_exp16_and(p):
    '''exp16 : exp17 AND exp16
            | LPAREN exp17 AND exp16 RPAREN
            | exp17'''
    if len(p) == 4:
        p[0] = AndExp(p[1], p[3])
    elif len(p) == 6:
        p[0] = AndExp(p[2], p[4])
    else:
        p[0] = p[1]


def p_exp17_call(p):
    '''exp17 : call '''
    p[0] = CallExp(p[1])

def p_exp_id(p):
    '''exp17 : ID
             | NULL'''
    p[0] = IdExp(p[1])

def p_exp_bool(p):
    '''exp17 : TRUE
              | FALSE'''
    p[0] = BooleanExp(p[1])

def p_exp_number(p):
    '''exp17 : NUMBER'''
    p[0] = NumExp(p[1]) 

def p_exp_string(p):
    '''exp17 : string '''
    p[0] = p[1]

def p_string(p):
    '''string : DOUBLE_QUOTES ID DOUBLE_QUOTES  
                | SINGLE_QUOTES ID SINGLE_QUOTES  
    '''
    p[0] = StringExp(p[2])


def p_is(p):
    '''exp17 : ID IS ID
    '''
    p[0] = IsExp(p[1], p[3])

def p_this(p):
    ''' exp17 : THIS SCORE ID ASSIGN ID
              '''
    p[0] = AssignThis(p[3], p[5])

def p_plus_plus(p):
    ''' exp17 : ID SUM SUM'''
    p[0] = PlusPlusExp(p[1])

def p_call_id_params(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = ParamsCall(p[1], p[3])
    else:
        p[0] = NoParamsCall(p[1])


def p_params_ids(p):
    '''params : exp COMMA params
              | exp '''
    if len(p) == 2:
        p[0] = SingleParam(p[1])
    elif len(p) == 4:
        p[0] = CompoundParams(p[1], p[3])


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()
