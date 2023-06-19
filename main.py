import tkinter as tk
from tkinter import messagebox

def fazer_chute(resposta_label):
    global limite_inferior, limite_superior
    numero_chute = (limite_inferior + limite_superior) // 2
    resposta = resposta_entry.get().lower()
    
    if resposta == "maior":
        limite_inferior = numero_chute + 1
    elif resposta == "menor":
        limite_superior = numero_chute - 1
    elif resposta == "igual":
        messagebox.showinfo("Adivinhação", "O computador adivinhou! O número é: {}".format(numero_chute))
        janela.destroy()
    else:
        messagebox.showwarning("Adivinhação", "Resposta inválida. Por favor, digite 'maior', 'menor' ou 'igual'.")
    
    resposta_entry.delete(0, tk.END)
    resposta_entry.focus_set()
    
    resposta_label.config(text="O número em que você está pensando é maior, menor ou igual a: {}".format(numero_chute))

def jogo_adivinhacao(numero_min, numero_max):
    global limite_inferior, limite_superior, resposta_entry, janela
    janela = tk.Tk()
    janela.title("Jogo de Adivinhação")
    
    instrucao_label = tk.Label(janela, text="Pense em um número entre {} e {}.".format(numero_min, numero_max))
    instrucao_label.pack(pady=10)
    
    input_frame = tk.Frame(janela)
    input_frame.pack()
    
    resposta_label = tk.Label(input_frame, text="O número em que você está pensando é maior, menor ou igual a: {}".format((numero_min + numero_max) // 2))
    resposta_label.pack(side=tk.LEFT)
    
    resposta_entry = tk.Entry(input_frame, width=10)
    resposta_entry.pack(side=tk.LEFT)
    resposta_entry.focus_set()
    
    chute_button = tk.Button(janela, text="Chutar", command=lambda: fazer_chute(resposta_label))
    chute_button.pack(pady=10)
    
    limite_inferior = numero_min
    limite_superior = numero_max
    
    janela.mainloop()
    
    if limite_inferior > limite_superior:
        messagebox.showinfo("Adivinhação", "Não foi possível adivinhar o número. Verifique se você forneceu informações corretas.")


# Exemplo de uso
jogo_adivinhacao(1, 100)
