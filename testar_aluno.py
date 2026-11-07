# testar_aluno.py
from aluno import Aluno

# 1. Criar pelo menos três alunos
aluno1 = Aluno("Maria Silva", "2024001")
aluno2 = Aluno("João Souza", "2024002")
aluno3 = Aluno("Ana Lima", "2024003")

lista_alunos = [aluno1, aluno2, aluno3]

# 2. Adicionar dados válidos (deixando o aluno3 sem notas)
aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(7.0)
aluno1.registrar_falta()
aluno1.registrar_falta()

aluno2.adicionar_nota(5.0)
aluno2.adicionar_nota(6.0)
for _ in range(6):
    aluno2.registrar_falta()

# 3. Testar pelo menos três operações inválidas
print("--- Testando Operações Inválidas ---")

if not aluno1.adicionar_nota(11):
    print("Nota inválida: use um valor entre 0 e 10.")

if not aluno1.adicionar_nota(-2):
    print("Nota inválida: use um valor entre 0 e 10.")

if not str(aluno2.set_matricula("   ")):
    print("Matrícula inválida: não pode ser vazia.")

print("\n--- Relatório de Alunos (Total de Aulas: 40) ---")
# 4. Percorrer a lista, imprimir dados e a situação de aprovação
for aluno in lista_alunos:
    print(aluno)
    if aluno.verificar_aprovacao(40):
        print("Situação: aprovado")
    else:
        print("Situação: reprovado")

# 5. Encontrar e mostrar o aluno com a maior média
campeao_da_quadra = None

for aluno in lista_alunos:
    if campeao_da_quadra is None or aluno.calcular_media() > campeao_da_quadra.calcular_media():
        campeao_da_quadra = aluno

print("\n--- Destaque Academico ---")
if campeao_da_quadra and campeao_da_quadra.notas:
    print(f"Maior media: {campeao_da_quadra.nome} ({campeao_da_quadra.calcular_media():.2f})")
else:
    print("Nenhum aluno possui notas registradas.")
