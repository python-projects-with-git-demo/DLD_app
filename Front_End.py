from tkinter import*
import DLD_app as un
import tkinter.font as TkFont
from tkinter import ttk
class front_end:
    def __init__(self,screen):
        self.screen=screen
        self.screen.title("DLD app")
        self.screen.config(bg='#C6D0E0')
        self.screen.geometry('470x300')
        custom_font = TkFont.Font(family="Bahnschrift SemiLight Condensed", size=14)
        self.menubar=Menu(self.screen,background='blue',bg='blue',font=('',20),fg='black')
        self.conversions=Menu(self.menubar,tearoff=0,font=('Agency FB',15))
        self.menubar.add_cascade(label='options',menu=self.conversions)
        self.conversions.add_command(label="conversions",command=self.conversions_button)
        self.conversions.add_command(label="complements",command=self.complements_button)
        self.conversions.add_separator()
        self.conversions.add_command(label='Exit',command=self.screen.quit)
        self.screen.config(menu=self.menubar)
        self.frame1=Frame(self.screen,bg='#C6D0E0',width=430,height=300)
        self.frame1.pack(side='top',fill='x')
    def exit_option(self):
        self.frame1.pack_forget()
        self.frame1=Frame(self.screen,bg='#C6D0E0',width=430,height=300)
        self.frame1.pack(side='top',fill='x') 
    def noconversions(self):
        self.a=self.combo1.get()
        self.b=self.combo2.get()
        if self.a==self.b:#need to reveiw logic for this condition
            self.entry2.delete(1.0,END)
            self.entry2.insert(END,self.entry1.get(1.0,END))
        elif self.a=='decimal' and self.b=='binary':
            self.entry2.delete(1.0,END)
            decbin=un.deci_binary_conversion(self.entry1.get(1.0,END))
            self.entry2.insert(END,decbin.result)
        elif self.a=='decimal' and self.b=='octal':
            self.entry2.delete(1.0,END)
            decioct=un.deci_octal_conversion(self.entry1.get(1.0,END))
            self.entry2.insert(END,decioct.result)
        elif self.a=='decimal' and self.b=='hexadecimal':
            self.entry2.delete(1.0,END)
            decihexa=un.deci_hexa_conversion(self.entry1.get(1.0,END))
            self.entry2.insert(END,decihexa.result)
        elif self.a=='binary' and self.b=='decimal':
            self.entry2.delete(1.0,END)
            bindec=un.binary_to_decimal(self.entry1.get(1.0,END))
            self.entry2.insert(END,bindec.result)
        elif self.a=='octal' and self.b=='decimal':
            self.entry2.delete(1.0,END)
            octdec=un.octal_to_decimal(self.entry1.get(1.0,END))
            self.entry2.insert(END,octdec.result)
        elif self.a=='hexadecimal' and self.b=='decimal':
            self.entry2.delete(1.0,END)
            hexadec=un.hexa_to_decimal(self.entry1.get(1.0,END))
            self.entry2.insert(END,hexadec.result)
        elif self.a=='binary' and self.b=='octal':
            self.entry2.delete(1.0,END)
            binoct=un.binary_to_octal(self.entry1.get(1.0,END))
            self.entry2.insert(END,binoct.result)
        elif self.a=='binary' and self.b=='hexadecimal':
            self.entry2.delete(1.0,END)
            binhex=un.binary_to_hexadecimal(self.entry1.get(1.0,END))
            self.entry2.insert(END,binhex.result)
        elif self.a == 'octal' and self.b=='binary':
            self.entry2.delete(1.0,END)
            octbin=un.octal_to_binary(self.entry1.get(1.0,END))
            self.entry2.insert(END,octbin.result)
        elif self.a=='hexadecimal' and self.b=='binary':
            self.entry2.delete(1.0,END)
            hexbin=un.hexadecimal_to_binary(self.entry1.get(1.0,END))
            self.entry2.insert(END,hexbin.result)
        elif self.a=='octal' and self.b=='hexadecimal':
            self.entry2.delete(1.0,END)
            octhex=un.octal_to_hexadecimal(self.entry1.get(1.0,END))
            self.entry2.insert(END,octhex.result)
        elif self.a=='hexadecimal' and self.b=='octal':
            self.entry2.delete(1.0,END)
            hexoct=un.hexadecimal_to_octal(self.entry1.get(1.0,END))
            self.entry2.insert(END,hexoct.result)
    def conversions_button(self):
        self.screen.geometry('420x300')
        self.data_type1=StringVar()
        self.data_type2=StringVar()
        self.combo1=ttk.Combobox(self.screen,width=20,values=['decimal','binary','octal','hexadecimal'],font=('Bahnschrift SemiLight Condensed',15),textvariable=self.data_type1)
        self.combo1.place(x=10,y=20)
        self.combo1.current(0)
        self.combo2=ttk.Combobox(self.screen,width=20,values=['decimal','binary','octal','hexadecimal'],font=('Bahnschrift SemiLight Condensed',15),textvariable=self.data_type2)
        self.combo2.place(x=220,y=20)
        self.combo2.current(0)
        self.entry1=Text(self.screen,width=16,font=('Consolas',15),height=4,bd=5)
        self.entry1.place(x=10,y=60)
        self.entry2=Text(self.screen,width=16,font=('Consolas',15),height=4,bd=5)
        self.entry2.place(x=220,y=60)
        self.button1=Button(self.screen,width=10,bd=5,text="Convert",relief='raised',font=('Arial Rounded MT Bold',13),bg='blue',fg='white',activebackground='green',activeforeground='white',command=self.noconversions)
        self.button1.place(x=150,y=200)
        self.exit_button=Button(self.screen,width=5,bd=5,text="Exit",relief='raised',font=('Arial Rounded MT Bold',9),bg='red',fg='white',activebackground='white',activeforeground='black',command=self.exit_option)
        self.exit_button.place(x=185,y=260)
    def complements_button(self):
        pass
        