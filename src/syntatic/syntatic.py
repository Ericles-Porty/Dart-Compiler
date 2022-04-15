import ply.yacc as yacc
from src.tokens import tokens

def p_exp_exp(p):
  '''exp : NUMBER'''
  
def p_exp_exp1(p):
   '''exp1 : exp'''
    
def p_exp_SUM(p):
    '''exp : exp SUM exp1'''

def p_exp_SUB(p):
    '''exp : exp SUB exp1'''


def p_error(p):
    print('Syntax error in input! Parser State')
  
parser = yacc.yacc()
