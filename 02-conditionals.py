# crie uma variável que guarde uma valor de temperatura em celsius, e exiba uma mensagem diferente para cada situação
# "cold" quando estiver baixa, "normal" pra quando estiver normal e "hot" para quando estiver alta.
# "scorching hot" quando estiver muito alta, "freezing" quando estiver muito baixa.

temperature = int(input("what's the temperature? "))

if temperature <= 0:
    print("today is a freezing day")
elif temperature <= 15:
    print("today is a cold day")
elif temperature >= 50: 
    print("today is a scorching hot day")
elif temperature >= 30:
    print("today is a hot day")
else:
    print("today is a normal day")        
    