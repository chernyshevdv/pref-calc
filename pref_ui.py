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
        frame_top.pack(side=TOP)

        frame_south = Frame(self, width=WIDTH, height=1/3*HEIGHT, borderwidth=1)
        frame_south.pack(side=BOTTOM)

        frame_west = Frame(frame_top, width=WIDTH/2, height=2/3*HEIGHT, borderwidth=1)
        frame_west.pack(side=LEFT)

        frame_west_gora = Frame(frame_west, width=WIDTH/4, height=2/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_west_gora.pack(side=RIGHT)

        frame_west_vists = Frame(frame_west, width=WIDTH/4, height=2/3*HEIGHT, borderwidth=1)
        frame_west_vists.pack(side=LEFT)

        frame_east = Frame(frame_top, width=WIDTH/2, height=2/3*HEIGHT, borderwidth=1)
        frame_east.pack(side=RIGHT)

        frame_east_gora = Frame(frame_east, width=WIDTH/4, height=2/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_east_gora.pack(side=LEFT)

        frame_east_vists = Frame(frame_east, width=WIDTH/4, height=2/3*HEIGHT, borderwidth=1)
        frame_east_vists.pack(side=RIGHT)

        frame_south_gora = Frame(frame_south, width=WIDTH, height=HEIGHT/6, borderwidth=1, relief=RAISED)
        frame_south_gora.pack(side=TOP)

        frame_south_vists = Frame(frame_south, width=WIDTH, height=HEIGHT/6, borderwidth=1)
        frame_south_vists.pack(side=BOTTOM)

        frame_vists_WE = Frame(frame_west_vists, width=WIDTH/4, height=1/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_vists_WE.pack(side=TOP)

        frame_vists_WS = Frame(frame_west_vists, width=WIDTH/4, height=1/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_vists_WS.pack(side=BOTTOM)

        frame_vists_EW = Frame(frame_east_vists, width=WIDTH/4, height=1/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_vists_EW.pack(side=TOP)

        frame_vists_ES = Frame(frame_east_vists, width=WIDTH/4, height=1/3*HEIGHT, borderwidth=1, relief=RAISED)
        frame_vists_ES.pack(side=BOTTOM)

        frame_vists_SW = Frame(frame_south_vists, width=WIDTH/2, height=HEIGHT/6, borderwidth=1, relief=RAISED)
        frame_vists_SW.pack(side=LEFT)

        frame_vists_SE = Frame(frame_south_vists, width=WIDTH/2, height=HEIGHT/6, borderwidth=1, relief=RAISED)
        frame_vists_SE.pack(side=RIGHT)

        self.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    root.geometry("400x500")
    app = PrefFrame()
    root.mainloop()


if __name__ == "__main__":
    main()