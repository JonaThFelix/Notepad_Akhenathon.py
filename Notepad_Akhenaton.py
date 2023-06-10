import customtkinter
import tkinter as tk
from tkinter import * 
from tkinter.filedialog import asksaveasfilename,askopenfilename

    
class Notepad_Akhenaton:
    
        def __init__(self):

            # -------------------------------------------------------- ORGANIZANDO INTERFACE PRINCIPAL ------------------------------------------------------------ #
            self.root = customtkinter.CTk()

            altura = 500
            largura = 800

            largura_tela = self.root.winfo_screenwidth()
            altura_tela = self.root.winfo_screenheight()

            posX = largura_tela / 2 - largura / 2
            posY = altura_tela / 2 - altura  / 2

            self.root.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))

            self.root.wm_title("Notepad | Akhenaton")

             # --------------------------------------------------------------------- SCROLL BAR  ---------------------------------------------------------------------- #
            scrollbar = Scrollbar(self.root)
            scrollbar.pack(side=RIGHT, fill=Y)


             # ----------------------------------------------------------------------- MENU DE NAVEGAÇÃO ------------------------------------------------------------ #
            menubar = Menu(self.root)

            menubar.add_command(label="Abrir", command=self.abrir)
            menubar.add_command(label="Salvar", command=self.salvar)
            menubar.add_command(label="Github", command=self.github)
            menubar.add_command(label="Como Funciona", command=self.ajuda)
            


            self.root.config(menu=menubar)
            self.root.resizable(False,False)

             # -------------------------------------------------------------------- PARTE PRINCIPAL DO TEXTO ------------------------------------------------------------ #
            self.text = Text(self.root)
            self.text.pack(expand=YES, fill=BOTH)
            self.text.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=self.text.yview)

            #COR DE FUNDO E CONFIGURAÇÃO DA FONTE
            self.text.configure(background="#F5F5F5")
            self.text.configure(font=("Calibri",16))

            self.root.mainloop()

        # ------------------------------------------------------------------------------------------ FUNÇÕES ------------------------------------------------------------ #
        def salvar(self): 

            
            fileName = asksaveasfilename()

            
            try:
                file = open(fileName, 'w')
                textoutput = self.text.get(0.0, END)
                file.write(textoutput)
            except:
                pass
            finally:
                file.close()


        def abrir(self):

            
            fileName = askopenfilename()

           
            try:
                file = open(fileName, 'r')
                contents = file.read()

                self.text.delete(0.0, END)
                self.text.insert(0.0, contents)
            except:
                pass

       
        def github(self):

            tk.messagebox.showinfo("Notepad | Akhenaton","Projeto desenvolvido por: Jonathan Felix\n\nGitHub: https://github.com/JonaThFelix\n\nLinkedin: https://www.linkedin.com/in/jonathan-felix-a7439119b/\n\nApoie a comunidade, ame sua vida e cuide dos animais ❤.")
            


        def ajuda(self):

            tk.messagebox.showinfo("Notepad | Akhenaton","Ainda estamos realizando alguns ajustes, esta é apenas a versão beta para fins de estudos.\n\n\nPara salvar um arquivo digitado você deverá incluir o '.txt' no final do documento, se quiser salva-lo e abri-lo.")
            


    
Notepad_Akhenaton()
