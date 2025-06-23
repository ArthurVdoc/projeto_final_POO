import subprocess
import sys


def main():

    print("Executando Login.py...")
    
    # Executa o arquivo como se fosse no terminal
    resultado = subprocess.run([sys.executable, "Login.py"])
    
    print("Login.py terminou de executar")
    print("Código de saída:", resultado.returncode)

if __name__ == "__main__":
    main()
