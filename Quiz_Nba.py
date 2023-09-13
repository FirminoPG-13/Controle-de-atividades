import os
q1={
    "Valor":"5",
    "gabarito":"b",
    "enunciado":"Qual é o time que draftou o Vince Carter",
    "opc1":"Hawks",
    "opc2":"Raptors",
    "opc3":"Mavericks",
    "opc4":"Magic"
}
q2={
    "Valor":"10",
    "gabarito":"a",
    "enunciado":"Qual é o time que venceu o campeonato da nba na temporada 94-95",
    "opc1":"Rockets",
    "opc2":"SuperSonics",
    "opc3":"Lakers",
    "opc4":"Magic"
}
q3={
    "Valor":"5",
    "gabarito":"d",
    "enunciado":"Quem é o único jogador da história a ter um recorde de 8-0 em finais",
    "opc1":"Elgin Baylor",
    "opc2":"Michael Jordan",
    "opc3":"Bil Walton",
    "opc4":"John Havlicek"
}
q4={
    "Valor":"10",
    "gabarito":"c",
    "enunciado":"Quem foi a primeira escolha do draft 2009",
    "opc1":"Stephen Curry",
    "opc2":"James Harden",
    "opc3":"Blake Griffin",
    "opc4":"Rick Rubio"
}
prova=[]
gabarito=['b','a','d','c']
marca=[]
prova.append(q1)
prova.append(q2)
prova.append(q3)
prova.append(q4)
v=0
cont=4
for num,q in enumerate(prova):
    print(num+1,")",q["enunciado"])
    print("a)",q["opc1"])
    print("b)",q["opc2"])
    print("c)",q["opc3"])
    print("d)",q["opc4"])
    print("\n")
    m=str((input("Informa a letra da resposta escolhida: ")))
    os.system("cls")
    if m == "b":m.append("opc2")
    if m == "a":m.append("opc1")
    if m == "d":m.append("opcd")
    if m == "c":m.append("opc3")
    
    pts=0
for i in range(cont):
    if m[i]==gabarito[i]:
        print("Questão",i+1,"certa") 
        pts=pts+int(prova[i]["Valor"])
    else: print("Questão",i+1,"errada. Resposta correta é:",gabarito[i])
print("Sua pontuação foi:",pts)

     

       
    
     
