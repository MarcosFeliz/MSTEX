print ("Bem vindo ao MSTEX!!")
print("-Você deve escrever letra por letra;")
print("-5 letras ao total;")
print("-Escreva tudo em MAIÚSCULO") 

print ("-Bom jogo ;)\n\n")
print("Consegue adivinhar a palavra da vez? Você tem 5 chances.")
print("")
palavra = ("COSTA")

letra1 = input("Informe a Primeira letra: ")
letra2 = input("Informe a Segunda letra: ")
letra3 = input("Informe a Terceira letra: ")
letra4 = input("Informe a Quarta letra: ")
letra5 = input("Informe a Quinta letra: ")

if letra1 == ("C"):
    print ("A primeira letra está correta!!")
elif letra1 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else:
    print ("A primeira letra está incorreta!!")

if letra2 == ("O"):
    print ("A Segunda letra está correta!!")
elif letra2 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Segunda letra está incorreta!!")

if letra3 == ("T"):
    print ("A Terceira letra está correta!!")
elif letra3 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Terceira letra está incorreta!!")

if letra4 == ("S"):
    print ("A Quarta letra está correta!!")
elif letra4 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quarta letra está incorreta!!")
    
if letra5 == ("A"):
    print ("A Quinta letra está correta!!")
elif letra5 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quinta letra está incorreta!!")

print ("Palavra escrita: {}{}{}{}{}".format(letra1,letra2,letra3,letra4,letra5))
if letra1 == "C" and letra2 == "O" and letra3 == "S" and letra4 == "T" and letra5 == "A" :
    print ("\nVocê acertou!\nIMPOSSÍVEL")
    print("De primeira!? Cê é o bixão mermo hein doido. A palavra correta é {}".format(palavra))
    exit()
else: 
    print ("\nVocê tem mais uma tentativa!!\n")

letra1 = input("Informe a Primeira letra: ")
letra2 = input("Informe a Segunda letra: ")
letra3 = input("Informe a Terceira letra: ")
letra4 = input("Informe a Quarta letra: ")
letra5 = input("Informe a Quinta letra: ")

if letra1 == ("C"):
    print ("A primeira letra está correta!!")
elif letra1 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else:
    print ("A primeira letra está incorreta!!")

if letra2 == ("O"):
    print ("A Segunda letra está correta!!")
elif letra2 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Segunda letra está incorreta!!")

if letra3 == ("T"):
    print ("A Terceira letra está correta!!")
elif letra3 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Terceira letra está incorreta!!")

if letra4 == ("S"):
    print ("A Quarta letra está correta!!")
elif letra4 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quarta letra está incorreta!!")
    
if letra5 == ("A"):
    print ("A Quinta letra está correta!!")
elif letra5 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quinta letra está incorreta!!")

print ("Palavra escrita: {}{}{}{}{}".format(letra1,letra2,letra3,letra4,letra5))
if letra1 == "C" and letra2 == "O" and letra3 == "S" and letra4 == "T" and letra5 == "A" :
    print ("\nVocê acertou!\nINCRÍVEL\nSó precisou de duas!?\nA palavra correta é {}".format(palavra))
    exit()
else: 
    print ("\nVocê tem mais uma tentativa!!\n")

letra1 = input("Informe a Primeira letra: ")
letra2 = input("Informe a Segunda letra: ")
letra3 = input("Informe a Terceira letra: ")
letra4 = input("Informe a Quarta letra: ")
letra5 = input("Informe a Quinta letra: ")

if letra1 == ("C"):
    print ("A primeira letra está correta!!")
elif letra1 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else:
    print ("A primeira letra está incorreta!!")

if letra2 == ("O"):
    print ("A Segunda letra está correta!!")
elif letra2 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Segunda letra está incorreta!!")

if letra3 == ("T"):
    print ("A Terceira letra está correta!!")
elif letra3 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Terceira letra está incorreta!!")

if letra4 == ("S"):
    print ("A Quarta letra está correta!!")
elif letra4 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quarta letra está incorreta!!")
    
if letra5 == ("A"):
    print ("A Quinta letra está correta!!")
elif letra5 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quinta letra está incorreta!!")

print ("Palavra escrita: {}{}{}{}{}".format(letra1,letra2,letra3,letra4,letra5))
if letra1 == "C" and letra2 == "O" and letra3 == "S" and letra4 == "T" and letra5 == "A" :
    print ("\nVocê acertou!\nBRABÍSSIMO\nDe trivela!\nA palavra correta é {}".format(palavra))
    exit()

else: 
    print ("\nVocê tem mais uma tentativa!!\n")

letra1 = input("Informe a Primeira letra: ")
letra2 = input("Informe a Segunda letra: ")
letra3 = input("Informe a Terceira letra: ")
letra4 = input("Informe a Quarta letra: ")
letra5 = input("Informe a Quinta letra: ")

if letra1 == ("C"):
    print ("A primeira letra está correta!!")
elif letra1 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else:
    print ("A primeira letra está incorreta!!")

if letra2 == ("O"):
    print ("A Segunda letra está correta!!")
elif letra2 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Segunda letra está incorreta!!")

if letra3 == ("T"):
    print ("A Terceira letra está correta!!")
elif letra3 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Terceira letra está incorreta!!")

if letra4 == ("S"):
    print ("A Quarta letra está correta!!")
elif letra4 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quarta letra está incorreta!!")
    
if letra5 == ("A"):
    print ("A Quinta letra está correta!!")
elif letra5 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quinta letra está incorreta!!")

print ("Palavra escrita: {}{}{}{}{}".format(letra1,letra2,letra3,letra4,letra5))
if letra1 == "C" and letra2 == "O" and letra3 == "S" and letra4 == "T" and letra5 == "A" :
    print ("\nVocê acertou!\nQuase!\nEssa foi por pouco! A palavra correta é {}".format(palavra))
    exit()
else: 
    print ("\nVocê tem mais uma tentativa!!\n")

letra1 = input("Informe a Primeira letra: ")
letra2 = input("Informe a Segunda letra: ")
letra3 = input("Informe a Terceira letra: ")
letra4 = input("Informe a Quarta letra: ")
letra5 = input("Informe a Quinta letra: ")

if letra1 == ("C"):
    print ("A primeira letra está correta!!")
elif letra1 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra1 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else:
    print ("A primeira letra está incorreta!!")

if letra2 == ("O"):
    print ("A Segunda letra está correta!!")
elif letra2 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra2 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Segunda letra está incorreta!!")

if letra3 == ("T"):
    print ("A Terceira letra está correta!!")
elif letra3 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra3 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Terceira letra está incorreta!!")

if letra4 == ("S"):
    print ("A Quarta letra está correta!!")
elif letra4 == ("A"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra4 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quarta letra está incorreta!!")
    
if letra5 == ("A"):
    print ("A Quinta letra está correta!!")
elif letra5 == ("O"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("S"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("T"):
    print ("Essa letra há na palavra, mas não nessa posição!")
elif letra5 == ("C"):
    print ("Essa letra há na palavra, mas não nessa posição!")
else :
    print ("A Quinta letra está incorreta!!")

print ("Palavra escrita: {}{}{}{}{}".format(letra1,letra2,letra3,letra4,letra5))
if letra1 == "C" and letra2 == "O" and letra3 == "S" and letra4 == "T" and letra5 == "A" :
    print ("\nVocê acertou!\nUFA!\nEssa passou raspando!A palavra correta é {}".format(palavra))
    exit()
else: 
    print ("GAME OVER!!\nA palavra é: {}".format(palavra))