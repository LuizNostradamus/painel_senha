from tkinter import *
from tkinter import messagebox

#Janela cliente

cliente=Tk()
cliente.title("Solicitar Senha")
cliente.geometry("300x250")
cliente.configure(bg="lightgreen")

#Variaveis 

contador = 1
fila=[]
senha_atual = StringVar()
senha_atual.set("---")

#Janela do administrador 

admin = Toplevel(cliente)
admin.title("Administrador")
admin.geometry("300x350")
admin.configure(bg="lightgreen")

Label(admin, text="Fila de senhas", font=("Arial", 20)).pack(pady=10)
lista_admin = Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

#Janela do painel

painel = Toplevel(cliente)
painel.title("Painel de Senhas")
painel.geometry("400x300")
painel.configure(bg="lightgreen")

Label(painel, text="Senha Atual", font=("Arial", 20)).pack(pady=20)

Label(
    painel,
    textvariable=senha_atual,
    font=("Arial", 40),
    fg="red"
).pack(pady=20)

#Função da senha 

def solicitar_senha():
    global contador
    senha = f"A{contador:03}"
    fila.append(senha)
    lista_admin.insert(END, senha)
    messagebox.showinfo("Senha Gerada", f"Sua senha é {senha}")
    contador += 1

def chamar_senha():
    if len(fila) == 0:
        messagebox.showinfo("Aviso!", "Fila vazia")
    else:
        senha = fila.pop(0)
        lista_admin.delete(0)
        senha_atual.set(senha)

#Butões 

Label(cliente, text="Retirar senha", font=("Arial", 16)).pack(pady=20)

Button(
    cliente,
    text="Gerar senha",
    width=20,
    command=solicitar_senha
).pack(pady=10)

Button(
    admin,
    text="Chamar Proxima",
    width=20,
    command=chamar_senha
).pack(pady=10)
    


cliente.mainloop()
