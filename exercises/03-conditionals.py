# crie uma variável que guarde um horário.
# exiba uma mensagem de cumprimento relativa ao horário.
# entre 6-11 "Good Morning", entre 12-17 "Good Afternoon", entre 18-23 "Good Evening".
# caso contrário "Good Late Night".

hour = int(input("what time is it? "))

if hour >= 6 and hour <= 11:
    print("Good Morning")
elif hour >= 12 and hour <= 17:
    print("Good Afternoon")
elif hour >= 18 and hour <= 23:
    print("Good Evening")
else:
    print("Good Late Night")
    