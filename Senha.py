import customtkinter as ctk
from tkinter import messagebox
from DatabaseJSON import DatabaseJSON
import subprocess

# Banco de dados
Login = DatabaseJSON("usuarios.json")

# Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Alterar senha")
janela.geometry("400x500")

# Função: alterar visualização da senha 1
def alternar_senha1():
    entrada_senha.configure(show="" if check_senha1.get() else "*")

# Função: alterar visualização da senha 2
def alternar_senha2():
    confirmar_novasenha.configure(show="" if check_senha2.get() else "*")

# Função: alterar senha
def alterar_senha():
    usuarios = Login.extrair()
    usuario = entrada_usuario.get().strip()
    senha = entrada_senha.get()
    confirmarsenha = confirmar_novasenha.get()

    if not usuario or not senha or not confirmarsenha:
        messagebox.showwarning("Erro", "Preencha todos os campos.")
        return
    
    if usuario not in usuarios:
        messagebox.showerror("Erro", f"Usuário '{usuario}' não encontrado.")
    else:
        if senha == usuarios[usuario]:
            Login.alterar(usuario, confirmarsenha)
            messagebox.showinfo("Alterar senha", f"Senha de '{usuario}' alterada com sucesso!")
            janela.quit()
            subprocess.Popen(["python", "Login.py"])
        
        else:
            messagebox.showwarning("Erro", f"Senha incompátivel com o {usuario}")

def voltar():
    janela.quit()
    subprocess.Popen(["python", "Login.py"])

# Campo de usuário
entrada_usuario = ctk.CTkEntry(janela, placeholder_text="Usuário")
entrada_usuario.pack(pady=10)

# Campo senha
entrada_senha = ctk.CTkEntry(janela, placeholder_text="Insira senha atual", show="*")
entrada_senha.pack(pady=5)

# Checkbox senha 1
check_senha1 = ctk.BooleanVar()
mostrar_checkbox1 = ctk.CTkCheckBox(janela, text="Mostrar senha", variable=check_senha1, command=alternar_senha1)
mostrar_checkbox1.pack()

# Campo confirmar senha
confirmar_novasenha = ctk.CTkEntry(janela, placeholder_text="Digite a nova senha", show="*")
confirmar_novasenha.pack(pady=5)

# Checkbox senha 2
check_senha2 = ctk.BooleanVar()
mostrar_checkbox2 = ctk.CTkCheckBox(janela, text="Mostrar senha", variable=check_senha2, command=alternar_senha2)
mostrar_checkbox2.pack()

# Botão de alteração
btn_alterarsenha = ctk.CTkButton(janela, text="Alterar senha", command=alterar_senha)
btn_alterarsenha.pack(pady=20)

#Botão voltar

btn_voltar = ctk.CTkButton(janela, text="Menu Principal", command=voltar)
btn_voltar.pack(pady=20)

# Loop principal
janela.mainloop()