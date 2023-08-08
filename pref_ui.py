from tkinter import *
from tkinter import font
from tkinter.ttk import Style
import preference
import logging

HEIGHT = 500
WIDTH = 400

class PrefFrame(Frame):
    def __init__(self):
        super().__init__()
        self.final_score_w = StringVar(value="0.00")
        self.final_score_e = StringVar(value="0.00")
        self.final_score_s = StringVar(value="0.00")
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

        Label(frame_west_gora, text='Gora W:').pack(side=TOP)
        # an attribute, as we are to access it
        self.txt_gora_w = Entry(frame_west_gora, width=4)
        self.txt_gora_w.pack(side=TOP)
        bold_font = font.Font(weight='bold', size=24)
        Label(frame_west_gora, text='W', pady=20, font=bold_font).pack(side=TOP)
        # an attribute, as we are to access it
        self.lbl_final_score_W = Label(frame_west_gora, textvariable=self.final_score_w, fg='red', pady=20)
        self.lbl_final_score_W.pack(side=BOTTOM)

        Label(frame_east_gora, text='Gora E:').pack(side=TOP)
        # an attribute, as we are to access it
        self.txt_gora_e = Entry(frame_east_gora, width=4)
        self.txt_gora_e.pack(side=TOP)
        Label(frame_east_gora, text='E', pady=20, font=bold_font).pack(side=TOP)
        # an attribute, as we are to access it
        self.lbl_final_score_E = Label(frame_east_gora, textvariable=self.final_score_e, fg='red', pady=20)
        self.lbl_final_score_E.pack(side=BOTTOM)

        Label(frame_vists_WE, text="W -> E:").pack()
        self.txt_vists_WE = Entry(frame_vists_WE, width=4)
        self.txt_vists_WE.pack()

        Label(frame_vists_WS, text="W -> S:").pack()
        self.txt_vists_WS = Entry(frame_vists_WS, width=4)
        self.txt_vists_WS.pack()

        Label(frame_vists_ES, text="E -> S:").pack()
        self.txt_vists_ES = Entry(frame_vists_ES, width=4)
        self.txt_vists_ES.pack()

        Label(frame_vists_EW, text="E -> W:").pack()
        self.txt_vists_EW = Entry(frame_vists_EW, width=4)
        self.txt_vists_EW.pack()

        self.btn_calculate = Button(frame_south_gora, text="Calculate", command=self.calculate)
        self.btn_calculate.pack(side=LEFT)
        # Put label to add 80 pts space
        Label(frame_south_gora, text="", padx=40).pack(side=LEFT)
        self.lbl_final_score_S = Label(frame_south_gora, textvariable=self.final_score_s, fg='red')
        self.lbl_final_score_S.pack(side=LEFT)
        # an attribute, as we are to access it
        self.txt_gora_s = Entry(frame_south_gora, width=4)
        self.txt_gora_s.pack(side=RIGHT)
        Label(frame_south_gora, text='Gora S:').pack(side=RIGHT)
        Label(frame_south_gora, text='S', font=bold_font).pack(side=RIGHT, padx=20)

        Label(frame_vists_SW, text="S -> W:").pack()
        self.txt_vists_SW = Entry(frame_vists_SW, width=4)
        self.txt_vists_SW.pack()

        Label(frame_vists_SE, text="S -> E:").pack()
        self.txt_vists_SE = Entry(frame_vists_SE, width=4)
        self.txt_vists_SE.pack()

        self.pack(fill=BOTH, expand=True)

        widgets_order = [self.txt_gora_w, self.txt_vists_WE, self.txt_vists_WS,
                         self.txt_gora_e, self.txt_vists_EW, self.txt_vists_ES,
                         self.txt_gora_s, self.txt_vists_SW, self.txt_vists_SE]
        for w in widgets_order:
            w.lift()
        self.txt_gora_w.focus()


    def calculate(self):
        ctrls = [self.txt_gora_w, self.txt_gora_e, self.txt_gora_s,
                    self.txt_vists_WE, self.txt_vists_WS, 
                    self.txt_vists_EW, self.txt_vists_ES,
                    self.txt_vists_SW, self.txt_vists_SE]
        vals = []
        for ct in ctrls:
            val = get_int_or_set_error(ct)
            if val < 0:
                ct.focus()
                return
            else:
                vals.append(val)

        f_w, f_e, f_s = preference.calculate_score(*vals)
        self.final_score_w.set(f"{f_w:.2f}")
        self.final_score_e.set(f"{f_e:.2f}")
        self.final_score_s.set(f"{f_s:.2f}")

def get_int_or_set_error(ctrl):
    val = -1
    try:
        val = int(ctrl.get())
    except ValueError:
        ctrl.focus()
    
    return val


def main():
    root = Tk()
    root.geometry("400x500")
    app = PrefFrame()
    root.mainloop()


if __name__ == "__main__":
    main()