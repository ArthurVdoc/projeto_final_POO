import customtkinter as ctk
from tkinter import messagebox
from DatabaseJSON import DatabaseJSON
import subprocess

# Instância do banco de dados JSON
Login = DatabaseJSON("usuarios.json")
Login.criar()

# Carrega os usuários do arquivo
def carregar_usuarios():
    return Login.extrair()

# Função de login
def realizar_login():
    usuarios = carregar_usuarios()
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login", f"Bem-vindo, {usuario}!")
        janela.quit()
        #subprocess(["python", "Insira o nome do jogo"])
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Função de cadastro
def cadastrar_usuario():
    janela.quit()
    subprocess.Popen(["python", "Cadastro.py"])

#Oculta e mostra a senha
senha_visivel = False
def alternar_senha():
    global senha_visivel
    senha_visivel = not senha_visivel
    entrada_senha.configure(show="" if senha_visivel else "*")

#Alterar a senha
def alterar_senha():

    janela.quit()
    subprocess.Popen(["python", "Senha.py"])

def deletar():

    janela.quit()
    subprocess.Popen(["python", "Deletar.py"])

def rank():
    janela.quit()
    subprocess.Popen(["python", "Rank.py"])



# Configuração de tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Login Simulador")
janela.geometry("400x400")

# Título
titulo = ctk.CTkLabel(janela, text="Simulador de cidade", font=ctk.CTkFont(size=20, weight="bold"))
titulo.pack(pady=20)

# Campo de usuário
entrada_usuario = ctk.CTkEntry(janela, placeholder_text="Usuário")
entrada_usuario.pack(pady=10)

# Campo de senha
entrada_senha = ctk.CTkEntry(janela, placeholder_text="Senha", show="*")
entrada_senha.pack(pady=10)

# Checkbox senha
check_senha = ctk.BooleanVar()
mostrar_checkbox1 = ctk.CTkCheckBox(janela, text="Mostrar senha", variable=check_senha, command=alternar_senha)
mostrar_checkbox1.pack()

# Botão de login
btn_login = ctk.CTkButton(janela, text="Entrar", command=realizar_login)
btn_login.pack(pady=10)

# Botão de cadastro
btn_cadastrar = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar_usuario)
btn_cadastrar.pack()

#Botão de alterar senha
btn_alterarsenha = ctk.CTkButton(janela, text="Alterar senha", command=alterar_senha)
btn_alterarsenha.pack(pady=10)

#Botão de deletar
btn_deletar = ctk.CTkButton(janela, text="Excluir usuário", command=deletar)
btn_deletar.pack(pady=10)

#Botão de rank
btn_rank = ctk.CTkButton(janela, text="Rank", command=rank)
btn_rank.pack(pady=10)

# Loop principal
janela.mainloop()
