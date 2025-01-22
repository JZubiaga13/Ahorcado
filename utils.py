def juego():
    palabra=input("J1 NO MIRES \nJ2-Indique la palabra a adivinar: ").upper()
    p_oculta= (["_"] * len(palabra))
    p_lista=list(palabra)
    letras_usadas=[]
    victoria = "🥳"
    muerte = "😵"
    vidas = 3
    print(*p_oculta)

    while vidas>0 and "_" in p_oculta:
        print("Recuerda que has usado:", letras_usadas)
        letra= input("Que letra usas").upper()
        letras_usadas.append(letra)
        if letra in p_lista: 
            print("HAS ACERTADO")
            for n,letras in enumerate(p_lista):
                if letras==letra:
                    p_oculta[n] = letra
            print("Quedan letras por descubrir:",(p_oculta))
        else:
            vidas=vidas-1
            print("Nooo, prueba otra letra \nTe quedan", vidas, "vidas.")
                
    if vidas==0 or not"_" in p_oculta:
        if vidas==0:
            print("GAME OVER ", muerte,"\nRevancha?¿")
        elif not"_" in p_oculta:
            print("CONSEGUIDO", victoria, "LA PALABRA ERA", palabra.upper(), "\nOtra partida?")