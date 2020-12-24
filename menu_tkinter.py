import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        self.Frame1, self.label, self.button_action, self.message_fin = None, None, None, None
        # init var:
        # self.difficulty_v, self.language_v, self.action_button_v = tk.IntVar(), tk.StringVar(), tk.IntVar()
        super().__init__(master)
        self.master = master
        self.master.wm_state(newstate="zoomed")
        self.master.resizable(width=False, height=False)
        self.master.title("Auto pilote")
        self.menubar = tk.Menu(self.master)
        self.menu1 = tk.Menu(self.menubar, tearoff=0)
        self.menu2 = tk.Menu(self.menubar, tearoff=0)
        self.barre_outil()
        self.buttons, self.cases_vues, self.map_nombre, self.cases_marquee= [], [], [], []
        self.coups, self.cases = 0, 0


    def barre_outil(self):
        # menu "action"
        self.menu1.add_radiobutton(label="Calcul de position", command=self.calcul_position)
        self.menu1.add_radiobutton(label="Calcul de cap", command=self.calcul_cap)
        self.menu1.add_radiobutton(label="Calcul de maree", command=self.calcul_maree)
        self.menubar.add_cascade(label="action", menu=self.menu1)
        # menu "données"
        self.menu2.add_radiobutton(label="heure actuelle", command=self.heure)
        self.menu2.add_radiobutton(label="heure maree", command=self.heure)
        self.menu2.add_radiobutton(label="position", command=self.heure)
        self.menu2.add_radiobutton(label="cadre de la carte", command=self.heure)
        self.menubar.add_cascade(label="données", menu=self.menu2)
        # bouton de sortie
        self.menubar.add_radiobutton(label="quitter", command=self.master.destroy)
        self.master.config(menu=self.menubar)
    
    def calcul_position():
        pass
    
    def calcul_cap():
        pass
    
    def calcul_maree():
        pass
    
    def heure():
        pass

root = tk.Tk()
app = Application(master=root)
root.iconbitmap('Tkinter\\icones\\bateau.ico')

background_image=tk.PhotoImage(file='Tkinter\\images\\carte_9999.png', master=root)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

"""w, h = 460, 330
image = tk.PhotoImage(file='Tkinter\\images\\carte_9999.png', master=root)
canvas = tk.Canvas(root, width=w, height=h)
canvas.pack()
 
canvas.create_image((w//2, h//2), image=image)"""

app.mainloop()