from src.lexic.lexic import lexer
from src.syntatic.syntatic import parser




# lexer.input('''if(1==2 if || 2>=8)  is else return ''')

# for tok in lexer:
#   print(f'Chave:{tok.type}\t\t Valor:{tok.value}\t\t Linha:{tok.lineno}\t\t Posicao:{tok.lexpos}') 

def main():
  while True:
      try:
          s = input('Digite > ')
      except EOFError:
          break
      if not s: continue
      result = parser.parse(s)
      print(result)

if __name__ == "__main__":
  main()
