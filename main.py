import ply.lex as lex

tokens = ('ID', 'NUMBER', 'CLASS', 'IS', 'VAR', 'RETURN', 'WHILE',  'IF', 'ELSE',  'TRUE', 'FALSE', 'NULL', 'SUM', 'SUB', 'TIMES', 'DIV', 'DIV_PART_INT', 'DIV_REST', 'EQUALS', 'DIFF', 'GREATER_EQ', 'LESS_EQ', 'GREATER', 'LESS', 'INVERT_EXPR', 'OR', 'AND', 'AND_BIN', 'OR_BIN', 'INVERT_BIN', 'XOR', 'LPAREN', 'RPAREN', 'COMMA' ,'SEMICOLON',  'ASSIGN', 'COMMENT_BLOCK', 'COMMENT_DOCUMENTATION', 'COMMENT_LINE') 
  
t_CLASS = r'class'
t_IS = r'is'
t_VAR = r'var'
t_RETURN = r'return'
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_TRUE = r'true'
t_FALSE = r'false'
t_NULL = r'null'

t_SUM = r'\+'
t_SUB=r'-'
t_TIMES = r'\*'
t_DIV=r'/'
t_DIV_PART_INT = r'~/'
t_DIV_REST = r'%'

t_EQUALS= r'=='
t_DIFF = r'!='
t_GREATER_EQ = r'>='
t_LESS_EQ = r'<='
t_GREATER = r'>'
t_LESS = r'<'

t_INVERT_EXPR = r'!'
t_OR = r'\|\|'
t_AND = r'&&'

t_AND_BIN = r'&'
t_OR_BIN = r'\|'
t_INVERT_BIN = r'~'
t_XOR = r'\^'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_ASSIGN = r'='

def t_COMMENT_BLOCK(t):
  r'/\*(.|\n)*\*/'
  t.lineno += t.value.count('\n')
  pass

def t_COMMENT_DOCUMENTATION(t):
  r'///.*'
  pass
  
def t_COMMENT_LINE(t):
  r'//.*'
  pass

  
def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  if t.value == 'id':
    return t
  for obj in tokens:
    if str(obj) == str(t.value).upper():
      t.type = obj
      return t
  return t
  
def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

lexer = lex.lex()

lexer.input('''if(1=2 || 2>=8)  is else return ''')

for tok in lexer:
  print(f'Chave:{tok.type}\t\t Valor:{tok.value}\t\t Linha:{tok.lineno}\t\t Posicao:{tok.lexpos}') 
