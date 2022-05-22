import re
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
class FormularioRegistro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializar_gui()
        self.definir_patrones_validaciones()



    def ventana2(self):
        os.system('mediaModaMediana.py')

    def inicializar_gui(self):
        self.title('Validación Datos')
        self.minsize(400, 350)
        lbl_titulo = tk.Label(self, text='FORMULARIO DE REGISTRO')
        lbl_titulo.grid(row=0, column=1, pady=10)
        frm_principal = tk.Frame(self, bd=7, relief='groove')
        frm_principal.grid(row=1, column=1, padx=10, pady=10)
        lbl_nombre = tk.Label(frm_principal, text='Nombre', justify=tk.LEFT)
        lbl_nombre.grid(row=0, column=0, sticky=tk.W)
        self.txt_nombre = tk.Entry(frm_principal, width=20)
        self.txt_nombre.grid(row=0, column=1)
        
        lbl_edad = tk.Label(frm_principal, text='Edad')
        lbl_edad.grid(row=1, column=0, sticky=tk.W)
        self.txt_edad = tk.Entry(frm_principal, width=20)
        self.txt_edad.grid(row=1, column=1)
        
        # lbl_contrasegnia_repetir = tk.Label(frm_principal, text='Contraseña repetir:')
        # lbl_contrasegnia_repetir.grid(row=2, column=0, sticky=tk.W)
        # self.txt_contrasegnia_repetir = tk.Entry(frm_principal, width=20)
        # self.txt_contrasegnia_repetir.grid(row=2, column=1)
        lbl_mes = tk.Label(frm_principal, text='Mes de su vista (1-12)')
        lbl_mes.grid(row=2, column=0, sticky=tk.W)
        self.txt_mes = tk.Entry(frm_principal, width=20)
        self.txt_mes.grid(row=2, column=1)

        lbl_email = tk.Label(frm_principal, text='Email:')
        lbl_email.grid(row=3, column=0, sticky=tk.W)
        self.txt_email = tk.Entry(frm_principal, width=20)
        self.txt_email.grid(row=3, column=1)
        
        lbl_residencia = tk.Label(frm_principal, text='Estado de residencia')
        lbl_residencia.grid(row=4, column=0, sticky=tk.W)
        self.txt_residencia = tk.Entry(frm_principal, width=20)
        self.txt_residencia.grid(row=4, column=1)
        
        lbl_pais = tk.Label(frm_principal, text='Metodo de pago')
        lbl_pais.grid(row=5, column=0, sticky=tk.W)
        self.cbx_pais = ttk.Combobox(frm_principal, width=20)
        paises = ('Efectivo', 'Tarjeta de credito', 'Tarjeta de debito', 'Cupon')
        self.cbx_pais['values'] = paises
        self.cbx_pais.current(0)
        self.cbx_pais.grid(row=5, column=1)

        lbl_experiencia = tk.Label(frm_principal, text='Experiencia en su visits')
        lbl_experiencia.grid(row=6, column=0, sticky=tk.W)
        self.txt_experiencia = tk.Entry(frm_principal, width=20)
        self.txt_experiencia.grid(row=6, column=1)
        
        lbl_compra = tk.Label(frm_principal, text='Ultima producto que compro:')
        lbl_compra.grid(row=7, column=0, sticky=tk.W)
        self.txt_compra = tk.Entry(frm_principal, width=20)
        self.txt_compra.grid(row=7, column=1)


        
        lbl_sabor = tk.Label(frm_principal, text='Metodo de pago')
        lbl_sabor.grid(row=8, column=0, sticky=tk.W)
        self.cbx_sabor = ttk.Combobox(frm_principal, width=20)
        sabores = ('Cheddar', 'spicy', 'Dulce de leche', 'Sin sabor')
        self.cbx_sabor['values'] = sabores
        self.cbx_sabor.current(0)
        self.cbx_sabor.grid(row=8, column=1)

        lbl_escala = tk.Label(frm_principal, text='Regresaria en escala 1-10:')
        lbl_escala.grid(row=9, column=0, sticky=tk.W)
        self.txt_escala = tk.Entry(frm_principal, width=20)
        self.txt_escala.grid(row=9, column=1)

        lbl_comentario = tk.Label(frm_principal, text='Comentarios para mejorar:')
        lbl_comentario.grid(row=10, column=0, sticky=tk.W)
        self.txt_comentario = tk.Entry(frm_principal, width=20)
        self.txt_comentario.grid(row=10, column=1)



        btn_guardar = tk.Button(frm_principal, text='Guardar', command=self.guardar)
        btn_guardar.grid(row=11, column=2)
        
        btn_limpiar = tk.Button(frm_principal, text='Limpiar', command=self.limpiar)
        btn_limpiar.grid(row=11, column=3)
        
        btn_salir = tk.Button(frm_principal, text='Salir', command=self.salir)
        btn_salir.grid(row=11, column=4)

        btn_media = tk.Button(frm_principal, text='Media',command=self.ventana2)
        btn_media.grid(row=11, column=5)

        # btn_ventana=tk.Button(frm_principal, text='Ventana', command=self.segundaVentana)
        # btn_ventana.grid(row=11, column=5)


    # def segundaVentana():
     
    #     ventana2 = tk.Toplevel()
    #     ventana2.title('Ventana 2')
    #     ventana2.geometry('400x400')
    #     ventana2.configure(background='#F0F0F0')
    #     hello=tk.Label(ventana2, text='Ventana 2', font=('Arial', 20))
    #     hello.pack()
    #     ventana2.mainloop()


    #     app.mainloop()

    def definir_patrones_validaciones(self):
        patron_nombre = r'^[^\s]+( [^\s]+)+$'
        self.regex_nombre = re.compile(patron_nombre)

        patron_edad = r'^(\d{1,99})'
        self.regex_edad = re.compile(patron_edad)

        patron_mes = r'^(\d{1,12})'
        self.regex_mes = re.compile(patron_mes)


        patron_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        self.regex_email = re.compile(patron_email)

        patron_residencia = r'^[^\s]'
        self.regex_residencia = re.compile(patron_residencia)

        patron_compra = r'^[^\s]'
        self.regex_compra = re.compile(patron_compra)

        patron_experiencia = r'^[^\s]'
        self.regex_experiencia = re.compile(patron_experiencia)



        

        patron_escala = r'^(\d{1,10})'
        self.regex_escala = re.compile(patron_escala)

        patron_comentario = r'^[^\s]+( [^\s]+)+$'
        self.regex_comentario = re.compile(patron_comentario)




    def guardar(self):
        
        nombre = self.txt_nombre.get().strip()

        if re.match(self.regex_nombre, nombre) is None:
            messagebox.showwarning('Mensaje', 'El campo Nombre debe incluir Nombre y Apellido')
            return

        edad = self.txt_edad.get().strip()
        if re.match(self.regex_edad, edad) is None:
            messagebox.showwarning('Mensaje', 'Su edad debe ser numerica del 1-99')
            return

    

        email = self.txt_email.get().strip()
        if re.match(self.regex_email, email) is None:
            messagebox.showwarning('Mensaje', 'El campo Email no es válido.')
            return


        mes=self.txt_mes.get().strip()
        if re.match(self.regex_mes, mes) is None:
            messagebox.showwarning('Mensaje', 'El campo Mes debe ser numerico del 1-12')
            return

        residencia = self.txt_residencia.get().strip()
        if re.match(self.regex_residencia, residencia) is None:
            messagebox.showwarning('Mensaje', 'El campo Residencia debe ser texto')
            return

        experiencia = self.txt_experiencia.get().strip()
        if re.match(self.regex_experiencia, experiencia) is None:
            messagebox.showwarning('Mensaje', 'El campo Experiencia debe ser texto')
            return

        compra = self.txt_compra.get().strip()
        if re.match(self.regex_compra, compra) is None:
            messagebox.showwarning('Mensaje', 'El campo Compra debe ser texto')
            return

        





        # documento = self.txt_documento.get().strip()
        # if re.match(self.regex_documento, documento) is None:
        #     messagebox.showwarning('Mensaje', 'El campo Documento debe ser un número con mínimo 7 dígitos, máximo 10.')
        #     return

        # ahorros = self.txt_ahorros.get().strip()
        # if re.match(self.regex_ahorros, ahorros) is None:
        #     messagebox.showwarning('Mensaje', 'El campo Ahorros debe ser un número real (e.g., 1000.53).')
        #     return

        file = open('datos.txt', 'a')
        file.write(nombre + '\n')
        file.write(edad + '\n')
        file.write(email + '\n')
        file.write(residencia + '\n')
        file.write(experiencia + '\n')
        file.write(compra + '\n')
        file.write(self.txt_escala.get().strip() + '\n')
        file.write(self.txt_comentario.get().strip() + '\n')
        file.close()

        file=open('numbers.txt', 'a')
        file.write(self.txt_escala.get().strip() + '\n')
        file.write(edad + '\n')
        file.write(mes + '\n')

        file.close()

        messagebox.showinfo('Mensaje', 'Los datos se guardaron de forma satisfactoria.')

        self.limpiar()

    def limpiar(self):
        self.txt_nombre.delete(0, 'end')
        self.txt_edad.delete(0, 'end')
        self.txt_mes.delete(0, 'end')
        self.txt_email.delete(0, 'end')
        self.txt_residencia.delete(0, 'end')
        self.cbx_pais.current(0)
        self.txt_compra.delete(0, 'end')
        self.txt_experiencia.delete(0, 'end')
        self.txt_escala.delete(0, 'end')
        self.txt_comentario.delete(0, 'end')
    
    def salir(self):
        self.destroy()

    def main():
        app = FormularioRegistro()
        app.mainloop()


if __name__ == '__main__':
    FormularioRegistro.main()

