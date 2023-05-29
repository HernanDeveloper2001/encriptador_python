import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st


class Desenciptador():

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Desencriptador")
        self.diseño()
        self.ventana1.mainloop()

    def diseño(self):
        self.titulo=ttk.Label(self.ventana1, text="encriptador de mensajes", font="Arial", foreground="red")
        self.titulo.grid(row=0, column=0,padx=5,pady=5)

        self.labelframe1 = ttk.Labelframe(self.ventana1, text="Encriptar texto")
        self.labelframe1.grid(row=1, column=0, padx=5, pady=5)

        self.escribirTexto = st.ScrolledText(self.labelframe1,width=30,height=10)
        self.escribirTexto.grid(row=0,column=0)

        self.texto = ttk.Label(self.labelframe1, text="Solo minusculas y sin acentos.",font="Arial")
        self.texto.grid(row=1, column=0, padx=5, pady=5)

        self.botonEncriptar = ttk.Button(self.labelframe1, text="Encriptar", command=self.encriptar)
        self.botonEncriptar.grid(row=2,column=0,padx=5,pady=5)


        self.labelframe2 = ttk.Labelframe(self.ventana1, text="Texto encriptado")
        self.labelframe2.grid(row=1, column=1,padx=5, pady=5)

        self.escribirTexto2 = st.ScrolledText(self.labelframe2,width=30,height=10)
        self.escribirTexto2.grid(row=0,column=0)

        self.texto2 = ttk.Label(self.labelframe2, text="Desencriptar texto",font="Arial")
        self.texto2.grid(row=1, column=0, padx=5, pady=5)

        self.botonDesencriptar = ttk.Button(self.labelframe2, text="Desencriptar",command=self.desencriptar)
        self.botonDesencriptar.grid(row=2,column=0,padx=5,pady=5)

        


        
    def encriptar(self):
        texto_original = self.escribirTexto.get(1.0,tk.END)
        texto_encriptado = ""
        for caracter in texto_original:
            if caracter.islower() and caracter.isalpha():
                if caracter == "a":
                   texto_encriptado += "ai"
                
                elif caracter == "e":
                   texto_encriptado += "enter"

                elif caracter == "i":
                   texto_encriptado += "imes"

                elif caracter == "o":
                   texto_encriptado += "ober"

                elif caracter == "u":
                   texto_encriptado += "ufat"
                else:
                   texto_encriptado += caracter

            else:
                texto_encriptado+=caracter

        self.escribirTexto.delete(1.0, tk.END)
        self.escribirTexto2.delete(1.0, tk.END)
        self.escribirTexto2.insert(tk.INSERT, texto_encriptado)

    def desencriptar(self):
        texto_encriptado= self.escribirTexto2.get(1.0, tk.END)
        texto_desencriptado = ""
        
        i = 0

        while i < len(texto_encriptado):
            caracter = texto_encriptado[i]
            if caracter == "a" and i < len(texto_encriptado) - 1 and texto_encriptado[i + 1] == "i":
                texto_desencriptado += "a"
                i += 1
            elif caracter == "e" and i < len(texto_encriptado) - 4 and texto_encriptado[i + 1:i + 5] == "nter":
                texto_desencriptado += "e"
                i += 4
            elif caracter == "i" and i < len(texto_encriptado) - 3 and texto_encriptado[i + 1:i + 4] == "mes":
                texto_desencriptado += "i"
                i += 3
            elif caracter == "o" and i < len(texto_encriptado) - 3 and texto_encriptado[i + 1:i + 4] == "ber":
                texto_desencriptado += "o"
                i += 3
            elif caracter == "u" and i < len(texto_encriptado) - 3 and texto_encriptado[i + 1:i + 4] == "fat":
                texto_desencriptado += "u"
                i += 3
            else:
                texto_desencriptado += caracter

            i += 1

        self.escribirTexto2.delete(1.0, tk.END)
        self.escribirTexto.delete(1.0, tk.END)
        self.escribirTexto.insert(tk.INSERT, texto_desencriptado)

    

    

        



aplicacion = Desenciptador()




