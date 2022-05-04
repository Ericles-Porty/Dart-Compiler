import ply.yacc as yacc
from src.tokens import tokens

def p_program(p):
    '''program : funcdecl
                | funcdecl program
                '''
    if (len(p) == 3):
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_funcdecl(p):
    '''funcdecl : signature body'''
    # p[0] = sa.FuncDeclConcrete(p[1], p[2])

def p_signature(p):
    '''signature : ID ID LPAREN sigparams RPAREN
                 | ID ID LPAREN RPAREN'''
    # if (isinstance(p[4], sa.SigParams)):
    #     p[0] = sa.SignatureConcrete(p[1], p[2], p[4])
    # else:
    #     p[0] = sa.SignatureConcrete(p[1], p[2], None)

def p_sigparams(p):
    '''sigparams : ID ID
                  | ID ID COMMA sigparams
    '''
    # if (len(p) == 3):
    #     p[0] = sa.SingleSigParams(p[1], p[2])
    # else:
    #     p[0] = sa.CompoundSigParams(p[1], p[2], p[4])

def p_body(p):
    ''' body : LKEY stms RKEY
             | LKEY RKEY'''
    # if (len(p) == 4):
    #     p[0] = sa.BodyConcrete(p[2])
    # else:
    #     p[0] = sa.BodyConcrete(None)

def p_stms(p):
    ''' stms : stm
            | stm stms'''
    # if (len(p) == 2):
    #     p[0] = sa.SingleStm(p[1])
    # else:
    #     p[0] = sa.CompoundStm(p[1], p[2])

def p_stm(p):
    ''' stm :  exp SEMICOLON
             | WHILE LPAREN exp RPAREN body
             | RETURN exp SEMICOLON'''
    # if (len(p) == 3):
    #     p[0] = sa.StmExp(p[1])
    # elif (p[1] == 'while'):
    #     p[0] = sa.StmWhile(p[3], p[5])
    # elif (p[1] == 'return'):
    #     p[0] = sa.StmReturn(p[2])
    # else:
    #     print('Gerei None', p[1])

def p_exp_assign(p):
    ''' exp :    exp EQUALS exp1
              | exp1'''
    # if (len(p) == 2):
    #     p[0] = p[1]
    # else:
    #     p[0] = sa.AssignExp(p[1], p[3])

def p_exp1_sum(p):
    '''exp1 : exp1 SUM exp2
         | exp2'''
    # if len(p) == 2:
    #     p[0] = p[1]
    # else:
    #     p[0] = sa.SomaExp(p[1], p[3])


def p_exp2_sub(p):
   '''exp2 : exp2 SUB exp3
           | exp3'''
#    if len(p) == 2:
#        p[0] = p[1]
#    else:
#        p[0] = sa.MulExp(p[1], p[3])


def p_exp3_times(p):
    '''exp3 : exp4 TIMES exp3
            | exp4'''
    # if len(p) == 2:
    #     p[0] = p[1]
    # else:
    #     p[0] = sa.PotExp(p[1], p[3])

def p_exp4_times(p):
    '''exp4 : exp5 DIV exp4
            | exp5'''

def p_exp5_div_part_int(p):
    '''exp5 : exp6 DIV_PART_INT exp5
            | exp6'''

def p_exp6_div_rest(p):
    '''exp6 : exp7 DIV_REST exp6
            | exp7'''

def p_exp7_div_rest(p):
    '''exp7 : SUB exp8 
            | exp8'''

def p_exp4_call(p):
    '''exp4 : call
            | NUMBER
            | ID
            | TRUE
            | FALSE'''
    # if isinstance(p[1], sa.Call):
    #     p[0] = sa.CallExp(p[1])
    # elif isinstance(p[1], int):
    #     p[0] = sa.NumExp(p[1])
    # elif (p[1] == 'true' or p[1] == 'false'):
    #     p[0] = sa.BooleanExp(p[1])
    # else:
    #     p[0] = sa.IdExp(p[1])


def p_call_id_params(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''
    # if len(p) == 5:
    #     p[0] = sa.ParamsCall(p[1], p[3])
    # else:
    #     p[0] = sa.NoParamsCall(p[1])


def p_params_ids(p):
    '''params : exp COMMA params
            | exp '''
    # if len(p) == 2:
    #     p[0] = sa.SingleParam(p[1])
    # elif len(p) == 4:
    #     p[0] = sa.CompoundParams(p[1], p[3])

def p_error(p):
    print("Syntax error in input!")
  
parser = yacc.yacc()
