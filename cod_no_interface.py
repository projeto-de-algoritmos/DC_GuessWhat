def jogo_adivinhacao(numero_min, numero_max):
    print("Pense em um número entre {} e {}.".format(numero_min, numero_max))
    input("Aperte Enter quando estiver pronto para continuar...")
    
    limite_inferior = numero_min
    limite_superior = numero_max
    
    while limite_inferior <= limite_superior:
        # Fazer um chute na metade do intervalo atual
        numero_chute = (limite_inferior + limite_superior) // 2
        
        resposta = input("O número em que você está pensando é maior, menor ou igual a {}? (maior/menor/igual): ".format(numero_chute))
        
        if resposta.lower() == "maior":
            limite_inferior = numero_chute + 1
        elif resposta.lower() == "menor":
            limite_superior = numero_chute - 1
        elif resposta.lower() == "igual":
            print("O computador adivinhou! O número é:", numero_chute)
            return
        else:
            print("Resposta inválida. Por favor, digite 'maior', 'menor' ou 'igual'.")
    
    print("Não foi possível adivinhar o número. Verifique se você forneceu informações corretas.")
    
# Exemplo de uso
jogo_adivinhacao(1, 100)
