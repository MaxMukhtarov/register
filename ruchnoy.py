from tkinter import *
from datetime import date
import os
from datetime import *
root = Tk()
root.minsize(500, 600)
root.maxsize(500, 600)
root.configure(bg="cyan")
#========Variable===============================================================
v1 = StringVar()
#========Widgets================================================================

name_label = Label(root, text="Введите имю", bg="olive")
name_label.place(x=60, y=40)
kolobok_label = Label(root, text="Колобок", bg='cyan')
kolobok_label.place(x=60, y=70)
solnoshko_label = Label(root, text="Солнышко", bg='cyan')
solnoshko_label.place(x=60, y=90)
buratino_label = Label(root, text="Буратино", bg='cyan')
buratino_label.place(x=60, y=110)
cheburashka_label = Label(root, text="Чебурашка", bg='cyan')
cheburashka_label.place(x=60, y=130)
znayka_label = Label(root, text="Знайка", bg='cyan')
znayka_label.place(x=60, y=150)
malvina_label = Label(root, text="Мальвина", bg='cyan')
malvina_label.place(x=60, y=170)
chepolino_label = Label(root, text="Чеполино", bg='cyan')
chepolino_label.place(x=60, y=190)
name_entry = Entry(root, width=36)
name_entry.place(x=150, y=40)


#=========Groups================================================================
kolobok_rb = Radiobutton(root, variable=v1, value="kolobok", bg='cyan')
kolobok_rb.place(x=160, y=70)
solnoshko_rb = Radiobutton(root, variable=v1, value="solnoshko", bg='cyan')
solnoshko_rb.place(x=160, y=90)
buratino_rb = Radiobutton(root, variable=v1, value="buratino", bg='cyan')
buratino_rb.place(x=160, y=110)
cheburashka_rb = Radiobutton(root, variable=v1, value="cheburashka", bg='cyan')
cheburashka_rb.place(x=160, y=130)
znayka_rb = Radiobutton(root, variable=v1, value="znayka", bg='cyan')
znayka_rb.place(x=160, y=150)
malvina_rb = Radiobutton(root, variable=v1, value="malvina", bg='cyan')
malvina_rb.place(x=160, y=170)
chepolino_rb = Radiobutton(root, variable=v1, value="chepolino", bg='cyan')
chepolino_rb.place(x=160, y=190)

#========Functions==============================================================
def ok():
    grupa = v1.get()
    ism = name_entry.get()
    name = f'{ism.upper()}_{grupa.upper()}'
    
    folderName = str(date.today()).split('-')
    folderName = f'{folderName[0]}-{folderName[1]}'
    os.chdir(r'C:\Users\Sehrli orolcha\Desktop\gister\kelgan')
        
        
    
    try:
            with open(f'{folderName}/{date.today()}_bolalar.csv', 'r+') as f:
                myDataList = f.readlines()
                nameList = []

                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[1])
                if name in nameList:
                    pass
                elif len((name.split('_'))[0])<1:
                    pass
                    
                elif name not in nameList:
                    now = datetime.now()
                    datestring = now.strftime('%H:%M:%S')
                    f.writelines(f'{len(myDataList)+1},{name},{datestring}\n')
                

    except FileNotFoundError:
            with open(f'{folderName}/{date.today()}_bolalar.csv', "w") as f:


                now = datetime.now()
                datestring = now.strftime('%H:%M:%S')
                f.writelines(f'1,{name},{datestring}\n')
    name_entry.delete(0, END)
#========Buttons================================================================
name_button = Button(root, text="Ок", width=10, command=ok)
name_button.place(x=380, y=40)
root.mainloop()
