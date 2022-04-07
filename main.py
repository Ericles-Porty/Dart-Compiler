import ply.lex as lex

tokens = ('COMMA', 'SUM', 'ID', 'NUMBER', 'TIMES', 'POT', 'LPAREN', 'RPAREN', 'EQUALS', 'DIV', 'SUB', 'RETURN', 'WHILE', 'IF', 'ELSE', 'TRUE', 'FALSE', 'CONTINUE', 'BREAK', 'NULL', 'DIFF', 'LESS', 'GREATER', 'LESS_EQ', 'GREATER_EQ', 'SEMICOLON', 'OR', 'AND', 'ASSIGN') 

t_EQUALS= r'=='
t_SUM = r'\+'
t_TIMES = r'\*'
t_POT = r'\^'
t_SUB=r'-'
t_DIV=r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_RETURN = r'return'
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_TRUE = r'true'
t_FALSE = r'false'
t_CONTINUE = r'continue'
t_BREAK = r'break'
t_NULL = r'null'
t_DIFF = r'!='
t_LESS = r'<'
t_GREATER = r'>'
t_LESS_EQ = r'<='
t_GREATER_EQ = r'>='
t_SEMICOLON = r';'
t_OR = r'\|\|'
t_AND = r'&&'
t_ASSIGN = r'='

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

lexer.input('''if(1=2 || 2>=8) else return \n''')

for tok in lexer:
  print(f'Chave:{tok.type}\t\t Valor:{tok.value}\t\t Linha:{tok.lineno}\t\t Posicao:{tok.lexpos}') 
