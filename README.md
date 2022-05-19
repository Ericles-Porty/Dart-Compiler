# Dart-Analyzer
Analisador léxico, sintático e semântico para a linguagem Dart.
*******
## Sumário
 * [1. Introdução](#intro)
 * [2. Lexemas do Dart ](#lexemas)
    * [2.1. Comentários ](#coments)
    * [2.2. Palavras Reservadas  ](#reservadas)
    * [2.3. Operadores e Delimitadores ](#opede)
        * [2.3.1. Aritméticos ](#arit)
        * [2.3.2. Relacionais ](#relacionais)
        * [2.3.3. Lógicos ](#logicos)
        * [2.3.4. Bit a Bit ](#bitabit)
    * [2.4. Literais String ](#lit-string)
    * [2.5. Literais numérica ](#lit-numerica)
    * [2.6. Literais booleano ](#lit-booleano)
    * [2.7. Identificador ](#identificador)
    * [2.8. Variáveis ](#variaveis)
 * [3. Flutter](#flutter)
 * [4. Referências](#referencia)

*******

  <div id='intro'/>

# 1. Introdução 

  O Dart é uma linguagem de programação case sensitive orientada a objetos multiparadigma criada pelo google, sua primeira conferência foi apresentada na GOTO na Dinamarca em 2011, a linguagem é bem versátil e pode ser utilizada na criação de aplicativos mobile, desktop, web, na criação de scripts e backend, a portabilidade dela funciona semelhante a portabilidade da linguagem java. 

  Dart foi construído na intenção de substituir Javascript, porém falhou, mas por outro lado conseguiu se dar muito bem no desenvolvimento de outras plataformas, principalmente com seu framework Flutter centrado no desenvolvimento mobile, mas que também desenvolve para web e desktop.

  A linguagem Dart possui uma sintaxe com estilo baseado no C. Isso faz com que sua sintaxe seja muito similar à linguagens atualmente populares, como Java e C#. Porém, o Dart tenta reduzir um pouco os ruídos característicos de linguagens baseadas no C.

  <div id='lexemas'/>

# 2. Lexemas do Dart 

  <div id='coments'/>

## 2.1. Comentários
    // Comentário in-line, comenta uma linha
    /*Comentário de um bloco */
    /// Comentário de documentação 

  <div id='reservadas'/>

## 2.2. Palavras Reservadas 
  Algumas palavras reservadas para a linguagem são: 

|  | | | |  | |
| ----------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| abstract | assert | await| case | class | continue |
| dynamic | enum | extends| factory | final |for |
| implements |in | is | mixin | null | operator |
| show | super | sync | throw | try | var |
| as | async | break | catch | const | covariant |
| else | export | external | false | finally | Function |
| import | interface | library | new | on | part |
| static | switch | this | true | typedef | void |
| do | if | set | yield | default | get |
| rethrow | while | deferred | hide | return | with |


foram utilizadas nesse estudo:

|  | | | |  | |
| ----------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| abstract | assert | await| case | get | continue |
| dynamic | enum | extends|  | final |for |
|  |in | is | mixin | null | operator |
|  |  | sync | throw |  | var |
| as | async | break | catch | const |  |
| else | export |  | false |  | Function |
| import |  | library | new | on | part |
| static | this | true | typedef | void | do | 
| if | set | yield |  |  | |  



  <div id='opede'/>

## 2.3. Operadores e Delimitadores

  <div id='arit'/>
 
### 2.3.1. Aritméticos

| Símbolo | Operação |
| ------------------- | ------------------- |
| + | Somar |
| - | Subtrair |
| -expr | Reverter o sinal da expressão |
| * | Multiplicar |
| / | Dividir |
| ~/ | Parte inteira da divisão| 
| % | Resto da divisão |

  <div id='relacionais'/>
 
### 2.3.2. Relacionais


| Símbolo | Operação |
| ------------------- | ------------------- |
| == | Igualdade |
| != | Diferença |
| > | Maior que |
| < | Menor que |
| >= | Maior igual |
| <= | Menor igual |

  <div id='logicos'/>
 
### 2.3.3. Lógicos

| Símbolo | Operação |
| -------------- | -------------- |
| !expr | Inverte o boolean da expressão |
| \|\| | Ou lógico |
| && | E lógico |

  <div id='bitabit'/>
 
### 2.3.4. Bit a Bit

| Símbolo | Operação |
| ------------ | ------------ |
| & | E |
| \| | Ou | 
| ^ | Xor |
| ~expr | Troca o valor binário |
| << | Desvio para esquerda |
| >> | Desvio para direita |
| >>> | Desvio sem sinal para direita |

  <div id='lit-string'/>
 
## 2.4. Literais String

String é um conjunto de caracteres encadeados que é transformado em uma ou mais palavras.

    Ex:     String frase = “Essa é uma frase”;
            var palavra = ‘Palavra’;

  <div id='lit-numerica'/>
 
## 2.5. Literais numérica
  Dart tem as variáveis numéricas de 2 tipos primitivos, int para números inteiros e double para números reais, ambas pertencem a classe num.
  
    Ex:     int inteiro = 10;
            double real = 10.10;
            num numero = 2;
            num numera = 2.2;

  <div id='lit-booleano'/>
 
## 2.6. Literais booleano
  Para valores booleanos o dart armazena em um bit o valor de 1 (true) ou 0 (false).
  
    Ex:     bool verdade = true;
            bool mentira = false; 

  <div id='identificador'/>
 
## 2.7. Identificador
  Os identificadores são a nomenclatura das variáveis, elas tem algumas regras a serem seguidas:
* Identificadores não podem ter caracteres especiais, com exceção do _ (serve como o private do encapsulamento em POO) e o $.
* Não podem ser usado as palavras-chave
* Não podem começar com número.

  <div id='variaveis'/>
 
## 2.8. Variáveis
  No dart existem vários tipos diferentes de variáveis, são elas int, double, float, String, void, dynamic, var e num.

| Tipo | Valor |
| --- | --- |
| int         |inteiro|
| double      |real|
| String      |palavra|
| dynamic     |qualquerTipo|
| var         |descubra|
| num         |numero|  
            
  <div id='flutter'/>

# 3. Flutter 
  Flutter é um framework da google que utiliza dart para construir projetos nativamente compilados em aplicações multiplataforma usando o mesmo código fonte. Sendo um framework de código aberto sobre a BSD License e multiplataforma.

  O framework está em constante atualização e vem ganhando popularidade pelo seu modo de compilação Hot Reload, já que ele renderiza os objetos de forma que vão sendo atualizados na tela. 

  <div id='referencia'/>
  
# Referências 

* https://dart.dev/
* https://flutter.dev/
* https://www.treinaweb.com.br/blog/o-que-e-dart
* https://medium.com/flutter-comunidade-br/introdu%C3%A7%C3%A3o-a-linguagem-de-programa%C3%A7%C3%A3o-dart-b098e4e2a41e
* https://www.devmedia.com.br/sintaxe-dart-tipos-nao-tao-primitivos/40368
