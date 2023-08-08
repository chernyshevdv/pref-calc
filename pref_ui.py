from tkinter import *
from tkinter.ttk import Style

HEIGHT = 500
WIDTH = 400

class PrefFrame(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.master.title("Pref Counter")
        self.style = Style()
        self.style.theme_use("default")
        frame_top = Frame(self, width=WIDTH, height=2/3*HEIGHT)
        frame_top.pack(side=TOP, fill=BOTH, expand=True)

        frame_south = Frame(self, width=WIDTH, height=1/3*HEIGHT, borderwidth=1)
        frame_south.pack(side=BOTTOM, fill=BOTH, expand=True)

        frame_west = Frame(frame_top, width=WIDTH/2, height=2/3*HEIGHT, borderwidth=1)
        frame_west.pack(side=LEFT, expand=True, fill=BOTH)

        frame_west_gora = Frame(frame_west, width=WIDTH/4, height=2/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_west_gora.pack(side=RIGHT, fill=BOTH, expand=True)

        frame_west_vists = Frame(frame_west, width=WIDTH/4, height=2/3*HEIGHT, borderwidth=1)
        frame_west_vists.pack(side=LEFT, fill=BOTH, expand=True)

        frame_east = Frame(frame_top, width=WIDTH/2, height=2/3*HEIGHT, borderwidth=1)
        frame_east.pack(side=RIGHT, fill=BOTH, expand=True)

        frame_east_gora = Frame(frame_east, width=WIDTH/4, height=2/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_east_gora.pack(side=LEFT, expand=True, fill=BOTH)

        frame_east_vists = Frame(frame_east, width=WIDTH/4, height=2/3*HEIGHT, borderwidth=1)
        frame_east_vists.pack(side=RIGHT, fill=BOTH, expand=True)

        frame_south_gora = Frame(frame_south, width=WIDTH, height=HEIGHT/6, borderwidth=1, relief=RAISED)
        frame_south_gora.pack(side=TOP, fill=BOTH, expand=True)

        frame_south_vists = Frame(frame_south, width=WIDTH, height=HEIGHT/6, borderwidth=1)
        frame_south_vists.pack(side=BOTTOM, fill=BOTH, expand=True)

        frame_vists_WE = Frame(frame_west_vists, width=WIDTH/4, height=1/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_vists_WE.pack(side=TOP, fill=BOTH, expand=True)

        frame_vists_WS = Frame(frame_west_vists, width=WIDTH/4, height=1/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_vists_WS.pack(side=BOTTOM, fill=BOTH, expand=True)

        frame_vists_EW = Frame(frame_east_vists, width=WIDTH/4, height=1/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_vists_EW.pack(side=TOP, fill=BOTH, expand=True)

        frame_vists_ES = Frame(frame_east_vists, width=WIDTH/4, height=1/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_vists_ES.pack(side=BOTTOM, fill=BOTH, expand=True)

        frame_vists_SW = Frame(frame_south_vists, width=WIDTH/2, height=HEIGHT/6, borderwidth=1, relief=RAISED)
        frame_vists_SW.pack(side=LEFT, fill=BOTH, expand=True)

        frame_vists_SE = Frame(frame_south_vists, width=WIDTH/2, height=HEIGHT/6, borderwidth=1, relief=RAISED)
        frame_vists_SE.pack(side=RIGHT, fill=BOTH, expand=True)

        lbl_gora_w = Label(frame_west_gora, text='Gora W:')
        lbl_gora_w.pack(side=TOP)
        # an attribute, as we are to access it
        self.txt_gora_w = Entry(frame_west_gora, width=4)
        self.txt_gora_w.pack(side=TOP)
        lbl_W = Label(frame_west_gora, text='W', pady=20)
        lbl_W.pack(side=TOP)
        # an attribute, as we are to access it
        self.lbl_final_score_W = Label(frame_west_gora, text="-000.0", fg='red', pady=20)
        self.lbl_final_score_W.pack(side=BOTTOM)

        lbl_gora_e = Label(frame_east_gora, text='Gora E:')
        lbl_gora_e.pack(side=TOP)
        # an attribute, as we are to access it
        self.txt_gora_e = Entry(frame_east_gora, width=4)
        self.txt_gora_e.pack(side=TOP)
        lbl_E = Label(frame_east_gora, text='E', pady=20)
        lbl_E.pack(side=TOP)
        # an attribute, as we are to access it
        self.lbl_final_score_E = Label(frame_east_gora, text="-000.0", fg='red', pady=20)
        self.lbl_final_score_E.pack(side=BOTTOM)

        lbl_vists_we = Label(frame_vists_WE, text="W -> E:")
        lbl_vists_we.pack()
        self.txt_vists_WE = Entry(frame_vists_WE, width=4)
        self.txt_vists_WE.pack()

        lbl_vists_ws = Label(frame_vists_WS, text="W -> S:")
        lbl_vists_ws.pack()
        self.txt_vists_WS = Entry(frame_vists_WS, width=4)
        self.txt_vists_WS.pack()

        lbl_vists_es = Label(frame_vists_ES, text="E -> S:")
        lbl_vists_es.pack()
        self.txt_vists_ES = Entry(frame_vists_ES, width=4)
        self.txt_vists_ES.pack()

        lbl_vists_ew = Label(frame_vists_EW, text="E -> W:")
        lbl_vists_ew.pack()
        self.txt_vists_EW = Entry(frame_vists_EW, width=4)
        self.txt_vists_EW.pack()

        self.btn_calculate = Button(frame_south_gora, text="Calculate")
        self.btn_calculate.pack(side=LEFT)
        self.lbl_final_score_S = Label(frame_south_gora, text="-000.0", fg='red', padx=80)
        self.lbl_final_score_S.pack(side=LEFT)
        # an attribute, as we are to access it
        self.txt_gora_s = Entry(frame_south_gora, width=4)
        self.txt_gora_s.pack(side=RIGHT)
        lbl_gora_s = Label(frame_south_gora, text='Gora S:')
        lbl_gora_s.pack(side=RIGHT)
        lbl_S = Label(frame_south_gora, text='S')
        lbl_S.pack(side=RIGHT, padx=20)

        lbl_vists_sw = Label(frame_vists_SW, text="S -> W:")
        lbl_vists_sw.pack()
        self.txt_vists_SW = Entry(frame_vists_SW, width=4)
        self.txt_vists_SW.pack()

        lbl_vists_se = Label(frame_vists_SE, text="S -> E:")
        lbl_vists_se.pack()
        self.txt_vists_SE = Entry(frame_vists_SE, width=4)
        self.txt_vists_SE.pack()
        
        self.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    root.geometry("400x500")
    app = PrefFrame()
    root.mainloop()


if __name__ == "__main__":
    main()