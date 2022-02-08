from tkinter import *
import requests
import json


def cep():
    while True:
        cep = entrada.get()
        tamanho = len(str(cep))

        if (tamanho == 8):
            resultado = requests.get("https://cep.awesomeapi.com.br/json/{}".format(cep))
            resultado = resultado.json()
            texto_cep = (resultado)
            texto = """
            CEP: {}
            RUA: {}
            ESTADO: {}
            BAIRRO: {}
            CIDADE: {}
            DDD: {}
            """.format(resultado["cep"], resultado["address_name"], resultado["state"], resultado["district"],
                       resultado["city"], resultado["ddd"])
            resultado_cep["text"] = texto
            break


        else:
            texto = 'Cep digitado é invalido'
            resultado_cep["text"] = texto
            break


janela = Tk()
janela.configure(background="#dde")
janela.title("Buscador de cep")

texto = Label(janela, text="Digite o cep")
texto.grid(column=1, row=0, pady=10, padx=10)

entrada = Entry(janela)
entrada.grid(column=1, row=1, padx=10, pady=10)

botao = Button(janela, text="Buscar Cep", command=cep)
botao.grid(column=1, row=2, padx=10, pady=10)

resultado_cep = Label(janela, text="")
resultado_cep.grid(column=1, row=3)

janela.mainloop()

