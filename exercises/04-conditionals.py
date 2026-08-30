# crie um programa para validar a entrada de atletas em uma competição olímpica.
# para entrar, o atleta deverá ter entre 18 e 35 anos.
# ele também precisa ter um bom condicionamento físico ou permissão médica.

age = int(input("how old are you? "))
fitness = input("do you have physical fitness? ")
medicalclearance = input("do you have medical clearance? ")

if age < 18 or age > 35:
    print("You are not in the age group")
elif fitness.lower() == "yes":
    print("You have been approved")
elif medicalclearance.lower() == "yes":
    print ("You have been approved")
else:
    print("You lack physical fitness or medical clearance")    
    