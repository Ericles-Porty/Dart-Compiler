reservadas = {
  'while' : 'WHILE',
  'for' : 'FOR',
  'true' : 'TRUE',
  'false' : 'FALSE',
  'return' : 'RETURN',
  # 'int' : 'INT',
  # 'var' : 'VAR',
  'class' : 'CLASS',
  'is' : 'IS',
  'if' : 'IF',
  'else' : 'ELSE',
  'null' : 'NULL',
  'static' : 'STATIC',
  'import' : 'IMPORT'
  # 'string' : 'STRING'
}

tokens = ['ID', 'NUMBER', 'DOUBLE_QUOTES','SUM', 'SUB', 'TIMES', 'DIV', 'DIV_PART_INT', 'DIV_REST', 'EQUALS', 'DIFF', 'GREATER_EQ', 'LESS_EQ', 'GREATER', 'LESS', 'INVERT_EXPR', 'OR', 'AND', 'AND_BIN', 'OR_BIN', 'INVERT_BIN', 'XOR', 'LPAREN', 'RPAREN', 'COMMA' ,'SEMICOLON',  'ASSIGN', 'COMMENT_BLOCK', 'COMMENT_DOCUMENTATION', 'COMMENT_LINE', 'LKEY', 'RKEY'] + list(reservadas.values())
