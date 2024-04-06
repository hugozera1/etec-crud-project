
from tkinter import *
import requests
import json
import mysql.connector
from PIL import Image, ImageTk
from urllib.request import urlopen

class pokezinho:
    def __init__(self):
      self.dbconexao = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "tbalunos")
      self.conexao = self.dbconexao.cursor()
      self.lista = []
           
      self.janela = Tk()
      self.janela.title("api Pokemon")
      self.janela.geometry("317x685")
      self.janela.configure(bg="red")
      self.janela.resizable(0,0)
      self.dictizin = {}
      self.idzinho = {}
      
      
      self.frambotao = Frame()
      self.frambotao.pack(fill="both", expand=True)
     
      self.bgimg = PhotoImage (file= "bonitinho.png")
      self.bgimgtxt = Label(self.janela, image=self.bgimg).place(relheight=1, relwidth=1)

      self.button = Button(self.janela,bg="white", font="Arial 9 bold", text="Iniciar",height=2, width=39, command=self.telainicial)
      self.button.place(x=20, y=520)
      
      self.janela.mainloop()

    def telainicial(self):
      
      self.frambotao.destroy()
      self.bgimg = PhotoImage (file= "beitt.png")
      self.bgimgtxt = Label(self.janela, image=self.bgimg).place(relheight=1, relwidth=1)

      

      

      

        #frame 
      self.frameNumeros = Frame(self.janela, height=183, width=265, bg="green")
      self.frameNumeros.place(x= 24, y= 248)
      self.bgimgg = PhotoImage (file= "texturinha.png")
      self.bgimgtxtt = Label(self.frameNumeros, image=self.bgimgg).place(relheight=1, relwidth=1)
      
      
        #labels
      self.addlabel = Label(self.frameNumeros, text="  Insira o Pokemon: ", font = 'arial 15',bg="dark grey",fg="black")
      self.addlabel.pack()
      self.addlabel.place(x=0,y=420)
      self.labelapelido = Label(self.frameNumeros, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")
      self.labelapelido.pack()
      self.labelapelido.place(x=0,y=520)
        #entry
      self.addentry = Entry(self.janela,font="Arial 14 bold",bg="white",bd=0,fg="black",width=22)
      
      self.apelidoentry = Entry(self.janela,font="Arial 14 bold",bg="white",bd=0,fg="black",width=22)
      


      self.botao3 = Button(self.janela,bg="white",bd=0,font="Arial 9 bold",text="Pesquisar",fg="black",width=30,height=2,command=self.procurarPokemon)
      self.botao4 = Button(self.janela,bg="white",bd=0,font="Arial 9 bold",text="Salvar",fg="black",width=30,height=2,command=self.SalvarBd)
      self.botao5 = Button(self.janela,bg="white",bd=0,font="Arial 9 bold",text="Deletar",fg="black",width=30,height=2,command=self.DeletarPokemon)
      self.botao6 = Button(self.janela,bg="white",bd=0,font="Arial 9 bold",text="Update",fg="black",width=30,height=2,command=self.UpdatePokemon)
      
      self.botaoteste2 = Button(self.janela,bg="#d01212",bd=0, text="🏡",font="Arial 20", command=None)
      self.botaoteste2.place(x=255, y=74)

      self.lb_listinha = Listbox(self.janela,font="Arial 10 bold",height=11,width=37)
      self.lb_listinha.place(x=25,y=245)
      self.addlabelteste = Label(self.janela, text="", font = 'arial 7',bg="white",fg="black")
      self.addlabelteste.place(x=150,y=400)
      self.id = 0
      
      
      
      

        #position
      self.addentry.place(x=33,y=156)
      self.apelidoentry.place(x=33,y=196)

      self.botao3.place(x=52,y=456)
      self.botao4.place(x=52,y=512)
      self.botao5.place(x=52,y=568)
      self.botao6.place(x=52,y=621)
      
      
    def tela2(self):
 
      

      self.bgimg = PhotoImage (file= "amem.png")
      self.bgimgtxt = Label(self.janela, image=self.bgimg).place(relheight=1, relwidth=1)


        #frame 
      self.pinkframe = Frame(self.janela, height=380, width=240, bg="green")
      self.pinkframe.place(x= 20, y= 160)
      self.bgimgg = PhotoImage (file= "foi.png")
      self.bgimgtxtt = Label(self.pinkframe, image=self.bgimgg).place(relheight=1, relwidth=1)

        #labels
      
      self.lista = [1, 2, 23, 134]
      
      ImageUrl1= f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.lista[0]}.png'
      u1 = urlopen(ImageUrl1)
      raw_data = u1.read()
      u1.close()
      photo1 = ImageTk.PhotoImage(data=raw_data)
      self.pok1 = Label(self.pinkframe, image=photo1)
      self.pok1.image = photo1
      
      ImageUrl2= f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.lista[1]}.png'
      u2 = urlopen(ImageUrl2)
      raw_data = u2.read()
      u2.close()
      photo2 = ImageTk.PhotoImage(data=raw_data)
      self.pok2 = Label(self.pinkframe, image=photo2)
      self.pok2.image = photo2

      ImageUrl3= f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.lista[2]}.png'
      u3 = urlopen(ImageUrl3)
      raw_data = u3.read()
      u3.close()
      photo3 = ImageTk.PhotoImage(data=raw_data)
      self.pok3 = Label(self.pinkframe, image=photo3)
      self.pok3.image = photo3

      ImageUrl4= f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.lista[3]}.png'
      u4 = urlopen(ImageUrl4)
      raw_data = u4.read()
      u4.close()
      photo4 = ImageTk.PhotoImage(data=raw_data)
      self.pok4 = Label(self.pinkframe, image=photo4)
      self.pok4.image = photo4
      self.pok5 = Label(self.pinkframe, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")
      self.pok6 = Label(self.pinkframe, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")
      self.pok7 = Label(self.pinkframe, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")
      self.pok8 = Label(self.pinkframe, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")
      self.pok9 = Label(self.pinkframe, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")
      self.pok10 = Label(self.pinkframe, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")
      self.pok11 = Label(self.pinkframe, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")
      self.pok12 = Label(self.pinkframe, text="Apelido: ", font = 'arial 15',bg="dark grey",fg="black")

      self.pok1.grid(column=1, row=1)
      self.pok2.grid(column=2, row=1)
      self.pok3.grid(column=1, row=2)
      self.pok4.grid(column=2, row=2)
      self.pok5.grid(column=1, row=3)
      self.pok6.grid(column=2, row=3)
      self.pok7.grid(column=1, row=4)
      self.pok8.grid(column=2, row=4)
      self.pok9.grid(column=1, row=5)
      self.pok10.grid(column=2, row=5)
      self.pok11.grid(column=1, row=6)
      self.pok12.grid(column=2, row=6)



      


        #entry
      
      
      self.botaoteste5 = Button(self.janela,font="Arial 20",bd=0, bg="#d01212", text="🏡", command= self.telainicial).place(x=255, y=74)

      

        #position
      self.addentry.place(x=200,y=420)
      self.apelidoentry.place(x=200,y=520)
      #self.botao3.place(x=15,y=600)
      
      self.botao5.place(x=320,y=600)
      self.botao6.place(x=120,y=600)      
    def procurarPokemon(self):
    
      pokemon = self.addentry.get().lower()
      
      try:
          requisicao = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
          requisicao.raise_for_status()  # Raise an error for bad status codes

          pokemon_data = requisicao.json()

          self.lb_listinha.delete(0, END)

          self.apelido = str(self.apelidoentry.get())
          self.nomepokemon = str(self.addentry.get())
          nomezinho = pokemon_data['name']
          self.altura = pokemon_data['height'] / 10
          self.peso = pokemon_data['weight'] / 10
          self.id = pokemon_data['id']

          self.lb_listinha.insert(END, f'Nome: {nomezinho}')
          self.lb_listinha.insert(END, f'Altura: {self.altura}')
          self.lb_listinha.insert(END, f'Peso: {self.peso}')
          self.lb_listinha.insert(END, f'Id: {self.id}')

          if self.nomepokemon in self.dictizin:
              self.lb_listinha.insert(END, self.dictizin[self.nomepokemon])
          else:
              self.lb_listinha.insert(END, "Apelido não encontrado no dicionário")

          ImageUrl = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.id}.png'
          u = urlopen(ImageUrl)
          raw_data = u.read()
          u.close()
          photo = ImageTk.PhotoImage(data=raw_data)
          label = Label(self.janela, image=photo, width=100, height=100, background="white")
          label.image = photo
          label.place(x=180, y=330)

          print(self.id)

      except requests.exceptions.RequestException as e:
          self.lb_listinha.delete(0, END)
          self.lb_listinha.insert(END, f"Erro ao buscar Pokemon: {e}")
      except KeyError as e:
          self.lb_listinha.delete(0, END)
          self.lb_listinha.insert(END, f"Pokemon não encontrado ou dados inválidos.")
      
    def SalvarBd(self):
      
          try:

             
            self.lista.insert(3, self.id)
            self.nomepokemon = str(self.addentry.get())
            self.apelido = str(self.apelidoentry.get())
            altura_str = "{:.1f}".format(self.altura)  # Convertendo e arredondando a altura
            peso_str = "{:.1f}".format(self.peso)  # Convertendo e arredondando o peso
            cmd = f'INSERT INTO tbalunos(nomepokemon, Altura, Peso, Apelido) VALUES("{self.nomepokemon}","{altura_str}","{peso_str}","{self.apelido}")'
            self.dictizin[self.nomepokemon] = self.apelido
            self.lb_listinha.delete(0, END)
            self.conexao.execute(cmd)
            self.dbconexao.commit()
          except Exception as e:
             
             
    
    
            print(f"Erro ao salvar no banco de dados: {e}")
            self.lb_listinha.delete(0, END)
            self.lb_listinha.insert(0, "POKEMON JA INSERIDO")

            self.a = self.id
            self.lista.insert(3, self.id)
            print(self.dictizin)
            print(self.lista)
          
    def DeletarPokemon(self):
        self.nomepokemon = str(self.addentry.get())
        cmd = f'DELETE FROM tbalunos WHERE nomepokemon = "{self.nomepokemon}"'
        self.conexao.execute(cmd)
        self.dbconexao.commit()
    def UpdatePokemon(self):
      nome_pokemon = self.addentry.get()
      novo_apelido = self.apelidoentry.get()
      print(f'Atualizando Pokémon: {nome_pokemon} com Apelido: {novo_apelido}')
      
      cmd = f'UPDATE tbalunos SET Apelido = "{novo_apelido}" WHERE nomepokemon = "{nome_pokemon}"'
      self.conexao.execute(cmd)
      self.dbconexao.commit()
      
     
      self.dictizin[nome_pokemon] = novo_apelido

      
      self.refresh_listbox_item(nome_pokemon)
      
      print('Atualização concluída')

    def refresh_listbox_item(self, pokemon_name):
      
      cmd = f'SELECT * FROM tbalunos WHERE nomepokemon = "{pokemon_name}"'
      self.conexao.execute(cmd)
      updated_data = self.conexao.fetchone()

     
      index = None
      for i in range(self.lb_listinha.size()):
          if self.lb_listinha.get(i).startswith("Nome: " + pokemon_name):
              index = i
              break

      if index is not None:
          
          self.lb_listinha.delete(index, index + 3)  
          self.lb_listinha.insert(index, f'Nome: {updated_data[0]}')
          self.lb_listinha.insert(index + 1, f'Altura: {updated_data[1]}')
          self.lb_listinha.insert(index + 2, f'Peso: {updated_data[2]}')
          self.lb_listinha.insert(index + 3, f'Apelido: {updated_data[3]}') 
      else:
          print("Pokemon not found in Listbox")
    def MostrarCampos(self):
        cmd = f'SHOW tbalunos Apelido'
        self.conexao.execute(cmd)
        self.dbconexao.commit()
    def Dictteste(self):
      self.nomepokemon = str(self.addentry.get())
      self.apelido = str(self.apelidoentry.get())
      self.dictizin[self.nomepokemon] = self.apelido
      self.lb_listinha.insert(END,self.dictizin[self.nomepokemon])
    def TesteImage(self):
      imglogo = PhotoImage(file="" )
      l_logo=Label(self.janela,image=imglogo)
      l_logo.place(x=30,y=50) 
    
    def testemostrar(self):
      self.frameteste = Frame()
      self.frameteste.pack()


      
    

    
pokezinho()