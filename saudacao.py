from datetime import datetime

# Captura a hora atual do sistema
hora = datetime.now().hour

# Verifica o horário e escolhe a saudação
if hora < 12:
    print("Bom dia!")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")

print("Seu dia está automatizado com Python")
