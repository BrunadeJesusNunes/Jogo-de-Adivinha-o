print("**********")
print("Bem vindo ao jogo de Adivinhação!")
peint("**********")

numero_secreto = 96
total_de_tentativas = 3
rodada=1
 
while(rodada <= total_de_tentativas):
    print("Tentativas {} de {}".format(rodada,total_de_tentativas))


chute_str = input("Digite o seu número")
print("Você digitou;" chute-str)
chute = int (chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto 

if(acertou):
    print("parabéns! Você acertou!")
else: 
    if(maior):
        print("O seu chute foi maior do que o número secreto!")
    elif(menor):
        print("O seu chute foi menor do que o número secreto!") 
    
    rodada = rodad + 1
print("Fim de jogo")