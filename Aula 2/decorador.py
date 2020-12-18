def header(function):
    def decorator(nome)
        print("###Bem vindo ao meu site")
        print("")
        return function(nome)
    return decorator

def footer(function):
    def decorator(nome)
        print('###Copyrigth - 2020')
        function(nome)
    return decorator
@footer
@header
def produto (nome):
 
    print(f'Produto: {nome} - R$ 2K')
   
@footer
@header
def sobre():
    
    print('Esta é minha loja ...')


produto ('Cadeira gamer')
produto ('Teclado mecanico')
