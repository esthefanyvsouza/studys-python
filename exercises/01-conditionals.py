# crie um programa onde o preço do pão será guardado por uma variável.
# após isso o usuário digitará quanto dinheiro ele tem.
# caso ele tenha dinheiro suficente, uma mensagem será exibida efetuando a compra.
# caso contrário, a mensagem exibida será negativa.

valueb = 0.5
money = float(input("how much money do you have? "))

if money >= valueb:
    print ("you bought it")
else:
    print ("you don't have the money to buy the bread")    
    