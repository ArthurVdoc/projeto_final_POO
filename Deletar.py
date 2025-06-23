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
def deletar():
    usuarios = carregar_usuarios()
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        Login.deletar(usuario)
        messagebox.showinfo("Deletar", f"{usuario} deletado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")


#Oculta e mostra a senha
senha_visivel = False
def alternar_senha():
    global senha_visivel
    senha_visivel = not senha_visivel
    entrada_senha.configure(show="" if senha_visivel else "*")


def voltar():
    janela.quit()
    subprocess.Popen(["python", "Login.py"])


# Configuração de tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Excluir usuário")
janela.geometry("400x400")

# Título
titulo = ctk.CTkLabel(janela, text="Excluir usuário", font=ctk.CTkFont(size=20, weight="bold"))
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

# Botão de cadastro
btn_deletar = ctk.CTkButton(janela, text="Excluir", command=deletar)
btn_deletar.pack()

#Botão voltar
btn_voltar = ctk.CTkButton(janela, text="Menu Principal", command=voltar)
btn_voltar.pack(pady=20)


# Loop principal
janela.mainloop()