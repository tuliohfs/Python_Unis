import tkinter as tk
from tkinter import *
import customtkinter

def calcular_imc():
    try:
        altura = float(entrada_alt.get())
        peso = float(entrada_peso.get())
        
        # Correção da fórmula do IMC
        imc = peso / ((altura / 100) ** 2)

        classificacao = ""

        if imc < 16:
            classificacao = "Desnutrição grave"
        elif imc < 16.9:
            classificacao = "Desnutrição moderada"
        elif imc < 18.5:
            classificacao = "Desnutrição leve"
        elif imc < 25:
            classificacao = "Normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Pré-Obesidade"
        elif imc < 40:
            classificacao = "Obesidade Grau I"
        elif imc < 45:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III (Mórbida)"

        nome = entrada_nome.get()
        endereco = entrada_end.get()

        resultado = f"Nome: {nome}\nEndereço: {endereco}\nIMC: {imc:.2f}\nClassificação: {classificacao}"
        resultado_label.configure(text=resultado)
    except ValueError:
        resultado_label.configure(text="Erro: Insira valores válidos para altura e peso.")

def limpar_resultado():
    resultado_label.configure(text="")

def sair():
    janela.destroy()

# Criar uma janela
janela = customtkinter.CTk()
janela.title("CALCULADORA DE IMC")
janela.geometry("550x250")
janela._set_appearance_mode("dark")
janela.resizable(False, False)

# Criar campos de entrada de texto para os nomes dos arquivos PDF
frame1 = customtkinter.CTkFrame(janela, fg_color="#242424", bg_color="#242424", )
frame1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

label_nome = customtkinter.CTkLabel(frame1, text="NOME PACIENTE:", text_color="white")
label_nome.grid(row=0, column=0, sticky='w')

entrada_nome = customtkinter.CTkEntry(frame1, width=420, height=20)
entrada_nome.grid(row=0, column=1, sticky='w', padx=10)

frame2 = customtkinter.CTkFrame(janela, fg_color="#242424", bg_color="#242424")
frame2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

label_end = customtkinter.CTkLabel(frame2, text="ENDEREÇO:(XXXXXX-XX)", text_color="white")
label_end.grid(row=1, column=0, sticky='w')

entrada_end = customtkinter.CTkEntry(frame2, width=378, height=20)
entrada_end.grid(row=1, column=1, sticky='w', padx=10)

frame3 = customtkinter.CTkFrame(janela, fg_color="#242424", bg_color="#242424")
frame3.grid(row=2, column=0, padx=10, pady=10, sticky='w')

label_alt = customtkinter.CTkLabel(frame3, text="ALTURA:(XXX)", text_color="white")
label_alt.grid(row=2, column=0, sticky='w')

entrada_alt = customtkinter.CTkEntry(frame3, width=190, height=20)
entrada_alt.grid(row=2, column=1, sticky='w', padx=10)

frame4 = customtkinter.CTkFrame(janela, fg_color="#242424", bg_color="#242424")
frame4.grid(row=3, column=0, padx=10, pady=10, sticky='w')

label_peso = customtkinter.CTkLabel(frame4, text="PESO:(XX)", text_color="white")
label_peso.grid(row=3, column=0, sticky='w')

entrada_peso = customtkinter.CTkEntry(frame4, width=210, height=20)
entrada_peso.grid(row=3, column=1, sticky='w', padx=10)

# Botão para processar os arquivos PDF e comparar os lotes e sacas
botao_processar = customtkinter.CTkButton(janela, text="CALCULAR", bg_color="#242424", fg_color="#263d76", command=calcular_imc)
botao_processar.grid(row=4, column=0, sticky='w', padx=20, pady=15)

# Botão para processar os arquivos PDF e comparar os lotes e sacas
botao_limpar = customtkinter.CTkButton(janela, text="LIMPAR", bg_color="#242424", fg_color="#263d76", command=limpar_resultado)
botao_limpar.grid(row=4, column=0, sticky='w', padx=189, pady=15)

# Botão para processar os arquivos PDF e comparar os lotes e sacas
botao_sair = customtkinter.CTkButton(janela, text="SAIR", bg_color="#242424", fg_color="#263d76", command=sair)
botao_sair.grid(row=4, column=0, sticky='n', pady=15)

# Posicionando o Label diretamente onde o novo_frame estava
resultado_label = customtkinter.CTkLabel(janela, text="", text_color="black", width=230, height=100)
resultado_label.grid(row=1, column=0, rowspan=4, padx=310)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
