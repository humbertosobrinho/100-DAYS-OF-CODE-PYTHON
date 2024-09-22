

try: 
    year = int(input("What's your year birthday"))
except ValueError:
    print("Você digitou um número invalido")
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")