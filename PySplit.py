import os
import math
import shutil
from tkinter import *


class Aplicacao:
    def __init__(self):
        # Interface Gráfica
        self.root = Tk()
        self.root.title('PySplit')
        self.root.geometry('400x200')
        self.root.configure(background='#3CB371')

        self.titulo = Label(self.root, text='Informe o número de divisões da pasta')
        self.titulo.configure(background='red')
        self.titulo.place(x=10, y=10)

        self.entrada = Entry(self.root, width=5)
        self.entrada.place(x=10, y=50)

        self.botao = Button(self.root, text='OK', command=self.on_click)
        self.botao.configure(width=5)
        self.botao.place(x=10, y=80)

        self.resultado = Label(self.root)
        self.resultado.configure(background='#3CB371', font=('Arial Black', 26))
        self.resultado.place(x=110, y=50)

        self.aviso = Label(self.root, text='Obs.: Certifique-se de ter criado a pasta "Arquivos",\ne colocado os itens '
                                           'dentro da mesma.\nO programa deve ser executado no mesmo nível da pasta '
                                           'Arquivos.')

        self.aviso.configure(background='red')
        self.aviso.place(x=10, y=120)

        self.info = Label(self.root, text='Desenvolvedor: Walacy S.')
        self.info.configure(background='#3CB371', font=('Arial Black', 8))
        self.info.place(x=100, y=180)

        self.root.resizable(False, False)
        self.root.mainloop()

    def on_click(self):
        # Contador
        count = 0

        # Define diretórios de origem e destino
        cur_path = os.getcwd()
        src_path = cur_path + '\\Arquivos\\'
        dest_path = cur_path + '\\Saida\\'
        # Cria lista com dos arquivos
        files = os.listdir(src_path)

        # Numero de arquivos
        file_num = len(files)
        # Número de divisões da pasta
        cuts = int(self.entrada.get())
        cuts2 = math.floor(file_num / cuts)
        # Divide lista
        file_split = [files[i:i + cuts2] for i in range(0, len(files), cuts2)]

        # Cria diretórios
        os.mkdir('Saida')
        for pasta in range(cuts):
            os.mkdir('Saida\\' + str(pasta))

        # Move arquivos
        for x in file_split:
            print('Sequência: ', count + 1)
            for y in file_split[count]:
                shutil.move(src_path + y, dest_path + str(count) + '\\' + y)
            if count == cuts - 1:
                break
            else:
                count += 1
                continue

        # Move o resto
        resto = os.listdir(src_path)
        if len(resto) == 0:
            self.resultado['text'] = f'Concluído'
        else:
            for w in resto:
                shutil.move(src_path + w, dest_path + str(count) + '\\' + w)
                self.resultado['text'] = f'Concluído'


Aplicacao()
