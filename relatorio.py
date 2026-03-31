# pedindo dados ao usuário
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
nota = float(input("Digite a nota final: "))

# criando o relatório
with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("=== RELATÓRIO ===\n")
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Idade: {idade}\n")
    arquivo.write(f"Nota final: {nota}\n")
    
    if nota >= 7:
        arquivo.write("Status: Aprovado\n")
    else:
        arquivo.write("Status: Reprovado\n")

print("Relatório gerado com sucesso!")