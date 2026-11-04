from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk


class Graphique:
    def __init__(self, master):
        super().__init__(master)
        self.fig = Figure(figsize=(6, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.barre = None
        if avec_barre:                     
            cadre_barre = ctk.CTkFrame(self)
            cadre_barre.pack(side="bottom", fill="x")
            self.barre = NavigationToolbar2Tk(self.canvas, cadre_barre, pack_toolbar=False)
            self.barre.grid(row=0, column=0, sticky="w")
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self.fenetre = (-10, 10, -10, 10)
        self._axes()

    def axes(self):
        xmin, xmax, ymin, ymax = self.fenetre
        self.ax.set_xlim(xmin, xmax)
        self.ax.set_ylim(ymin, ymax)
        self.ax.grid(True, alpha=0.3)
        self.canvas.draw()
        if self.barre:
            self.barre.update()   

    def tracer(self, xs, ys, couleur="tab:blue"):
        self.ax.plot(xs, ys, color=couleur)
        self.canvas.draw()

    def effacer(self):
        self.ax.clear()
        self._axes()

    #méthode à créer = axes, tracer, effacer, peut-être zoom, exporter le graphique/ enregistrer