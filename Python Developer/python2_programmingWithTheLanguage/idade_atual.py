from datetime import date

def idade_atual():
    print("Digite o seu ano de nascimento: ")
    ano_como_string = input()
    ano_como_int = int(ano_como_string)
    ano_atual = date.today().year
    idade = ano_atual - ano_como_int
    print ("Sua idade atual é %i" %idade)
