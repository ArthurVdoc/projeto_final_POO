import customtkinter as ctk
from tkinter import messagebox
from DatabaseJSON import DatabaseJSON
import subprocess

# Banco de dados
Login = DatabaseJSON("usuariosmoney.json")
Login.criar()

# Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Ranking de Usuários")
janela.geometry("400x400")

def Rank():
    usuarios = Login.extrair()
    # Ordenar por valor (dinheiro), do maior para o menor
    ranking_ordenado = sorted(usuarios.items(), key=lambda item: item[1], reverse=True)

    texto = "🏆 Ranking:\n\n"
    for i, (nome, valor) in enumerate(ranking_ordenado, start=1):
        texto += f"{i}. {nome} — {valor}\n"
    
    return texto

def menu():
    janela.quit()
    subprocess.Popen(["python", "Login.py"])

# Mostrar ranking na interface
label_rank = ctk.CTkLabel(janela, text=Rank(), justify="left", font=ctk.CTkFont(size=14))
label_rank.pack(pady=20)

btn_return = ctk.CTkButton(janela, text="Menu Principal", command=menu)
btn_return.pack(pady=10)

janela.mainloop()