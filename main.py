from tkinter import *


janela = Tk()

janela.title('Gerador de Senhas')
janela.configure(background='#1e3743')
janela.geometry('500x200')
janela.resizable(False, False)


def gerar():
    contrato = entrada_contrato.get()

    nao_digitou = contrato == ''
    digitou_so_numeros = contrato.isdigit() is True

    if nao_digitou or digitou_so_numeros:
        lb_erro.configure(text='Insira um contrato válido')
    else:
        lista_contrato = contrato.split(' ')
        lb_erro.configure(text='')
        try:
            for contador in range(len(lista_contrato)):
                if lista_contrato[contador].isalpha() and len(lista_contrato[contador]) >= 4:
                    copiar_senha = Entry(janela, bg='#1e3743', highlightcolor='#1e3743', fg='white', justify='center')
                    copiar_senha.place(relx=0.41, rely=0.7)
                    copiar_senha.insert(0, f'{lista_contrato[contador].capitalize()}@123')
                    break

        except IndexError:
            lb_erro.configure(text='Insira um contrato válido')


def limpa_cliente():
    entrada_contrato.delete(0, END)


def on_enter(e):
    e.widget['background'] = '#1e3743'


def on_leave(e):
    e.widget['background'] = '#38B6FF'


lb_contrato = Label(janela, text='Cliente:', bg='#1e3743', fg='white')
lb_contrato.place(relx=0.02, rely=0.1)

entrada_contrato = Entry(janela, bg='#38B6FF')
entrada_contrato.place(relx=0.15, rely=0.1, relwidth=0.8)

btn_limpar = Button(janela, text='Limpar', bg='#38B6FF', border=2, fg='white', command=limpa_cliente)
btn_limpar.place(relx=0.4, rely=0.3, relwidth=0.12, relheight=0.15)

btn_limpar.bind("<Enter>", on_enter)
btn_limpar.bind("<Leave>", on_leave)

btn_gerar = Button(janela, text='Gerar', bg='#38B6FF', border=2, fg='white', command=gerar)
btn_gerar.place(relx=0.55, rely=0.3, relwidth=0.12, relheight=0.15)

btn_gerar.bind("<Enter>", on_enter)
btn_gerar.bind("<Leave>", on_leave)

lb_erro = Label(janela, text='', bg='#1e3743', fg='white')
lb_erro.place(relx=0.4, rely=0.6)

janela.mainloop()
