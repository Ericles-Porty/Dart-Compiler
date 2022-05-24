import ply.yacc as yacc
from src.tokens import *
from src.syntatic.syntax_abstract import *

def p_header(p):
    '''import : program
                | IMPORT string SEMICOLON
                | IMPORT string SEMICOLON import
                '''
    p[0] = p[1]

def p_program(p):
    '''program : funcdecl
                | funcdecl program                
                | CLASS ID body
                | CLASS ID body program
                '''
    if (len(p) == 3):
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = FuncDeclConcrete(p[1], p[2])

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
    elif (len(p) == 2):
        p[0] = BodyConcrete(p[1])
    elif (len(p) == 3):
        p[0] = BodyConcrete(None)

def p_stms(p):
    ''' stms : stm
            | stm stms'''
    if (len(p) == 2):
        p[0] = SingleStm(p[1])
    else:
        p[0] = CompoundStm(p[1], p[2])

def p_stm(p):
    ''' stm :  exp SEMICOLON
             | WHILE LPAREN exp RPAREN body
             | FOR LPAREN exp SEMICOLON exp SEMICOLON exp RPAREN body
             | s             
             | RETURN exp SEMICOLON'''
    if (len(p) == 3):
        p[0] = StmExp(p[1])
    elif (p[1] == 'while'):
        p[0] = StmWhile(p[3], p[5])
    elif (p[1] == 'return'):
        p[0] = StmReturn(p[2])
        print(p[2])
        print('######################################################')
        print('entrou')
    else:
        print('Gerei None', p[1])

def p_s(p):
    ''' s :   s1 
            | s2 '''

def p_e(p):
    ''' e : LPAREN exp RPAREN '''

def p_s1(p):
    ''' s1 :  IF e s1 ELSE s1 
            | IF e body ELSE body 
            | IF e s1 ELSE body 
            | IF e body ELSE s1
            | stms '''

def p_s2(p):
    ''' s2 :  IF e s 
            | IF e body 
            | IF e s1 ELSE s2 
            | IF e body ELSE s2 '''

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
       p[0] = MulExp(p[1], p[3])


def p_exp3_times(p):
    '''exp3 : exp4 TIMES exp3
            | exp4'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = PotExp(p[1], p[3])

def p_exp4_times(p):
    '''exp4 : exp5 DIV exp4
            | exp5'''

def p_exp5_div_part_int(p):
    '''exp5 : exp6 DIV_PART_INT exp5
            | exp6'''

def p_exp6_div_rest(p):
    '''exp6 : exp7 DIV_REST exp6
            | exp7'''

def p_exp7_invert_signal(p):
    '''exp7 : SUB LPAREN exp8 RPAREN 
            | exp8'''

def p_exp8_equals(p):
    '''exp8 : exp9 EQUALS exp8  
            | exp9'''

def p_exp9_diff(p):
    '''exp9 : exp10 DIFF exp9  
            | exp10'''

def p_exp10_greater(p):
    '''exp10 : exp11 GREATER exp10  
            | exp11'''

def p_exp11_less(p):
    '''exp11 : exp12 LESS exp11 
            | exp12'''

def p_exp12_greater_equals(p):
    '''exp12 : exp13 GREATER_EQ exp12 
            | exp13'''

def p_exp13_less_equals(p):
    '''exp13 : exp14 LESS_EQ exp13 
            | exp14'''

def p_exp14_invert_expr(p):
    '''exp14 : INVERT_EXPR exp15
            | exp15'''

def p_exp15_or(p):
    '''exp15 : exp16 OR exp15
            | LPAREN exp16 OR exp15 RPAREN
            | exp16'''

def p_exp16_and(p):
    '''exp16 : exp17 AND exp16
            | LPAREN exp17 AND exp16 RPAREN
            | exp17'''

def p_exp17_call(p):
    '''exp17 : call
            | NUMBER
            | ID
            | TRUE
            | FALSE
            | NULL'''
    # if isinstance(p[1], sa.Call):
    #     p[0] = sa.CallExp(p[1])
    # elif isinstance(p[1], int):
    #     p[0] = sa.NumExp(p[1])
    # elif (p[1] == 'true' or p[1] == 'false'):
    #     p[0] = sa.BooleanExp(p[1])
    # else:
    #     p[0] = sa.IdExp(p[1])

def p_string(p):
    '''
    string : DOUBLE_QUOTES ID DOUBLE_QUOTES  
    '''

def p_is(p):
    '''is : IS type
    '''

def p_types(p):
  ''' type : ID
  '''
  
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
