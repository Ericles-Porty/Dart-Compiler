from src.lexic.lexic import lexer
from src.syntatic.syntatic import parser
from src.syntatic.syntax_abstract import *
from src.visitor.abstract_visitor import *
from src.visitor.visitor import *
from src.visitor.semantic_visitor import *


# lexer.input('''if(1==2 if || 2>=8)  is else return ''')

# for tok in lexer:
#   print(f'Chave:{tok.type}\t\t Valor:{tok.value}\t\t Linha:{tok.lineno}\t\t Posicao:{tok.lexpos}')

def main():
    s = '''
    import "oi";
    int main(int ok){
      int i =0;
      if (i==0){
        }
        for(int i=0;i<10;i+1){
          i is int;
        }
      }
    class uva{ }
    class uva{ }
    '''
    s2 = '''typedef int GeeksForGeeks(int a);
    
            static int main(int ok){
              Orde order;
              order = new Order(new UvaItem(new UvaItem()));
              Uva uva = new Uva("a");
              Uva uva = new Uva(5);

              GeeksForGeeks(a, b);

              this.nome = nome;
            }'''

    s3 = ''' import "algo";
             int metodo();
             class Algo {} 
             void main(int a) {
               /*int a = true;
                while(a == 9) {
                  int bok = 5;
                  for(int i=0; i<5; i++){
                    int i = 5;
                  }

                  if(i==2){
                    int a=0;
                  } else { 
                    int a=0;
                  }

                  if(i==3)
                    int a=0;
                  else { 
                    int a=0;
                  }

                  if(i==5) {
                    int a=0;
                  }

                  if(i==6) {
                    if(i==6) {
                      int a=0;
                    }
                  }

                  if(i==7) {
                    while(i == 0){
                      i is int;
                    }
                  }

                  if(i==7) {
                    if(i==6) {
                      if(i==6) {
                        int a=0;
                      }
                    }
                  } else {
                    if(i==7) {
                      while(i == 0){
                        int akfsdfd = 0;
                      }
                    }
                  }

                  if(i==9) {
                    while(i == 0){
                      i is int;
                    }
                  } else {
                    if(i==8) {
                      if(i==6) {
                        if(i==6) {
                          int a=0;
                        }
                      }
                    } else {
                      if(i==8) {
                        while(i == 0){
                          i is int;
                        }
                      }
                    }
                  }

               }*/
               int a;
               od od = new od();
               od od;
               od = new od(new odItem(new odItem()));
               od = new od(5);

               static int a = 1+1;
               int f = 5 - 5;
               int s = 3*3;
               int d = 5/5;
               int g = 5~/3;
               int j = 4%3;
               -(4==5);
               int j = -(4==5);
               int a = 9!=9;
               int b = 9>9;
               int c = 8<8;
               int b = 9>=9;
               int c = 8<=8;
               int c = !(a==b);
               8||8;
               8 && 8;
               a = 'q';
               string a = "Aq";
            
               string a = 'Aq';
               a is int;
               this.cor = cor;
               i--;
             }'''

    operacoes = ''' void main() {
                  int a = 9+9*9+9;
                }'''
    result = parser.parse(s3)
    # print(result)
    # visitor = SemanticVisitor()
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
