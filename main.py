#comentario de notas teste#
p1 = float(input("Digite a primeira nota:"))
p2 = float(input("Digite a segunda nota:"))
p3 = float(input("Digite a terceira nota:"))

notaMedia = (p1 + p2 + p3)/3
print(notaMedia)

if(notaMedia < 7):
   print("Reprovado!")

elif (notaMedia == 7):
   print("Ok, está na média")

else:
   print("Parabéns, aprovado")

print("programa encerrado!")