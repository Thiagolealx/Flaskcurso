# void = função sem retorno
def  ola ():
    imprimir ( "Olá" )


ola ()   # implicitamente retorna Nenhum


# funcao com retorno e anotações opcionais de tipos
def  soma ( a : int , b : int ) ->  int :
    resultado  =  a  +  b
    retorno  resultado


resultado  =  soma ( 5 , 5 )   # exercício
imprimir ( resultado )


# Funções de alta ordem


def  mensagem ( cabeçalho , rodapé ):
    cabeçalho ()
    print ( "Olá você está no CodeShow" )
    rodapé ()


 cabeçalho def ():
    imprimir ( "### inicio" )


def  footer ():
    imprimir ( "### fim" )


mensagem ( cabeçalho = cabeçalho , rodapé = rodapé )