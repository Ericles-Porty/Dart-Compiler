from src.lexic.lexic import lexer
from src.syntatic.syntatic import parser
from src.syntatic.syntax_abstract import *
from src.visitor.abstract_visitor import *
from src.visitor.visitor import * 




lexer.input('''if(1==2 if || 2>=8)  is else return ''')

# for tok in lexer:
#   print(f'Chave:{tok.type}\t\t Valor:{tok.value}\t\t Linha:{tok.lineno}\t\t Posicao:{tok.lexpos}') 

def main():
    s = '''
    import "oi";
    int main(int ok){while(1==2) {} }
    class uva{ }
    '''
    result = parser.parse(s)
    print(result)
    visitor = Visitor()
    # print(visitor)
    for r in result:
        r.accept(visitor)
  # while True:
  #     try:
  #         s = input('Digite > ')
  #     except EOFError:
  #         break
  #     if not s: continue
  #     result = parser.parse(s)
  #     print(result)

if __name__ == "__main__":
  main()
