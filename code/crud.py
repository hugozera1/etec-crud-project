from tkinter import *
import requests
import json
import mysql.connector
from PIL import Image, ImageTk
from urllib.request import urlopen

class Calculadora:
    def __init__(self):

        self.janela = Tk()
        self.janela.title("api Pokemon")
        self.janela.geometry("400x750")
        self.janela.configure(bg="white")
        self.janela.resizable(0,0)

        self.frame = Frame()
        self.frame.pack(fill="both", expand=True)
        self.button = Button(self.janela,bg="white", font="Arial 9 bold", text="Iniciar",height=2, width=39, command=self.telainicial)
        self.button.place(x=20, y=520)
      

        self.janela.mainloop()

Calculadora()            