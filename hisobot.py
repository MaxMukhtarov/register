from tkinter import *
from tkinter import filedialog, messagebox
import os
from datetime import datetime



root = Tk()
root.minsize(300, 400)

lab = Label(root, width=20, text="")
lab.pack()
bugun = datetime.today()
bugun = str(bugun)
bugun = bugun.split()
bugun=bugun[0]

path = ''
def tanla():
    global path
    tanlangan = filedialog.askopenfilename()
    if path == '':
        path += tanlangan
    else:
        path = tanlangan
royxat = []
buratino = []
solnoshko= []
chepolino = []
znayka = []
malvina = []
kolobok = []
cheburashka = []
qogan =[]

def hisob():
    try:
        dir = filedialog.askdirectory()
        os.chdir(dir)
        with open(f'{path}', 'r') as file:
            data = file.readlines()
            data1 = data
            for i in data1:
                i = i.split(",")
                del i[0]
                el = i[0].split("_")
                i = i[0] + i[1]
                i = i.split("_")
                q = i[1].replace('\n', '')
                i.remove(i[1])
                i.append(q)
                ul = f'{i[1]}_{i[0]}\n'
                r1=1
                r2=1
                r3=1
                r4=1
                r5=1
                r6=1
                r7=1
                r8=1
                if 'BURATINO' in el[1]:
                    buratino.append(ul)
                elif 'SOLNOSHKO' in el[1]:
                    solnoshko.append(ul)
                elif 'CHEPOLINO' in el[1]:
                    chepolino.append(ul)
                elif 'ZNAYKA' in el[1]:
                    znayka.append(ul)
                elif 'MALVINA' in el[1]:
                    malvina.append(ul)
                elif 'KOLOBOK' in el[1]:
                    kolobok.append(ul)
                elif 'CHEBURASHKA' in el[1]:
                    cheburashka.append(ul)
                else:
                    qogan.append(ul)
        # print(buratino)
        # print(solnoshko)
        # print(chepolino)
        # print(znayka)
        # print(znayka)
        # print(malvina)
        #
        with open('buratino.csv', 'w') as hisob:
            r1=1
            hisob.writelines(f'Buratino guruhining {bugun} dagi hisoboti\n\n\n')
            for i in buratino:
                hisob.writelines(f'{r1}      ,{i}')
                r1+=1
            hisob.writelines(f'\n\n\nJami {len(buratino)} ta bola keldi,___________Tarbiyachisi')
        with open('solnoshko.csv', 'w') as hisob:   
            r2=1
            hisob.writelines(f'Solnoshko guruhining {bugun} dagi hisoboti\n\n\n')
            for i in solnoshko:
                hisob.writelines(f'{r2}      ,{i}')
                r2+=1
            hisob.writelines(f'\n\n\nJami {len(solnoshko)} ta bola keldi,___________Tarbiyachisi')
        with open('chepolino.csv', 'w') as hisob:
            r3=1
            hisob.writelines(f'Chepolino guruhining {bugun} dagi hisoboti\n\n\n')
            for i in chepolino:
                hisob.writelines(f'{r3}      ,{i}')
                r3+=1
            hisob.writelines(f'\n\n\nJami {len(chepolino)} ta bola keldi,___________Tarbiyachisi')
        with open('znayka.csv', 'w') as hisob:
            r4=1
            hisob.writelines(f'Znayka guruhining {bugun} dagi hisoboti\n\n\n')
            for i in znayka:
                hisob.writelines(f'{r4}      ,{i}')
                r4+=1
            hisob.writelines(f'\n\n\nJami {len(znayka)} ta bola keldi,___________Tarbiyachisi')
        with open('malvina.csv', 'w') as hisob:
            r5=1
            hisob.writelines(f'Malvina guruhining {bugun} dagi hisoboti\n\n\n')
            for i in malvina:
                hisob.writelines(f'{r5}      ,{i}')
                r5+=1
            hisob.writelines(f'\n\n\nJami {len(malvina)} ta bola keldi,___________Tarbiyachisi')
        with open('kolobok.csv', 'w') as hisob:
            r6=1
            hisob.writelines(f'Kolobok guruhining {bugun} dagi hisoboti\n\n\n')
            for i in kolobok:
                hisob.writelines(f'{r6}      ,{i}')
                r6+=1
            hisob.writelines(f'\n\n\nJami {len(kolobok)} ta bola keldi,___________Tarbiyachisi')
        with open('cheburashka.csv', 'w') as hisob:
            r7=1
            hisob.writelines(f'Cheburashka guruhining {bugun} dagi hisoboti\n\n\n')
            for i in cheburashka:
                hisob.writelines(f'{r7}      ,{i}')
                r7+=1
            hisob.writelines(f'\n\n\nJami {len(cheburashka)} ta bola keldi,___________Tarbiyachisi')
        print(qogan)
        messagebox.showinfo(title="", message="Muvaffaqiyatli yakunlandi")
    except:
        messagebox.showerror(title="Hatolik", message="Dasturdan foydalanishda xatolikka yo`l qo`ydingiz\nDasturni qayta ishga tushiring")
b = Button(root, text="Faylni tanlang", command=tanla)
b.pack()
b2 = Button(root, text="Hisobotni olish", command=hisob)
b2.pack()


root.mainloop()
