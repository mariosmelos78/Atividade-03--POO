# testar_televisao.py
from televisao import Televisao

# 1. Criar pelo menos três televisores
tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

lista_tvs = [tv1, tv2, tv3]

# 2. Ligar algumas e deixar pelo menos uma desligada
tv1.ligar()
tv2.ligar()

# 3. Aplicar operações válidas
tv1.trocar_canal(5)
tv1.aumentar_volume(15)

tv2.trocar_canal(12)
tv2.aumentar_volume(60)

# 4. Testar pelo menos três operações inválidas e mostrar mensagens explicativas
print("--- Testando Operações Inválidas ---")

# Inválida 1: Trocar canal com a TV desligada
if not tv3.trocar_canal(20):
    print("Trocar canal com a TV desligada: Falhou (A TV precisa estar ligada)")

# Inválida 2: Ligar uma TV que já está ligada
if not tv1.ligar():
    print("Ligar de novo a TV 1: Falhou (A TV ja esta ligada)")

# Inválida 3: Canal acima do limite permitido
if not tv2.trocar_canal(150):
    print("Canal 150 na TV 2: Falhou (O canal deve ser entre 1 e 100)")

print("\n--- Estado Atual das TVs ---")
# 5. Percorrer a lista e imprimir cada televisor
for tv in lista_tvs:
    print(tv)
