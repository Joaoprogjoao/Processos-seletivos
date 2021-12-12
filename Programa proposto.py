aniversario = input("Hoje é seu aniversário? \n") #recebe a informação sobre o aniversário do usuário

velocidade = input("A qual velocidade estava dirigindo? \n") #recebe a velocidade informada
velocidade = int(velocidade) #converte o valor digitado pelo usuário para uma variável tipo int

def multa(velocidade):#função para não aniversariantes
    if velocidade <= 80:
        print("Boa viagem!")
    elif velocidade > 80 and velocidade <= 90:
        print("Você cometeu uma infração média.")
    elif velocidade > 90:
        print("Você cometeu uma infração grave.")

def multa_leve(velocidade):#função para aniversariantes
    if velocidade <= 85:
        print("Boa viagem!")
    elif velocidade > 85 and velocidade <= 95:
        print("Você cometeu uma infração média.")
    elif velocidade > 95:
        print("Você cometeu uma infração grave.")

if aniversario == "Sim" or aniversario == "sim":#escolhe qual dos critérios serão adotados com base na informação dada
    multa_leve(velocidade)
else:
    multa(velocidade)
