final=0.0
contador=0
while True:
    w1, w2, r = [int(x) for x in input().split()]
    if w1==w2==r==0:
        break
    conta1 = float(w1*(1+(r/30)))
    conta2 = float(w2*(1+(r/30)))
    media_conta =(conta1+conta2)/2
    final+= media_conta
    contador+=1
    if 1<=media_conta<13:
       print("Nao vai da nao")
    elif 13<=media_conta<14:
        print("E 13")
    elif 14<=media_conta<40:
       print("Bora, hora do show! BIIR!")
    elif 40<=media_conta<=60:
        print("Ta saindo da jaula o monstro!")
    elif media_conta>60:
        print("AQUI E BODYBUILDER!!")
final=final/float(contador)
if final>40:
    print()
    print("Aqui nois constroi fibra rapaz! Nao e agua com musculo!")