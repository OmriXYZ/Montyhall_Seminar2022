import matplotlib
import mplcursors
import sys
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



class plotStat:
    def __init__(self, root):
        """
        Initialize the plot object, handles the plot and statistics.
        :param root: window's root.
        """
        self.f = None
        self.a = None
        self.canvas = None
        self.stats = {'wins': [0],
                      'loses': [0]}
        self.winrate = None


    def update(self, wins, losses):
        """
        updates the plot.

        :param wins: wins
        :param losses: losses
        :return: None
        """
        self.stats.update({'wins': wins})
        self.stats.update({'loses': losses})
        sums = wins + losses
        self.winrate = (wins / sums) * 100 if sums != 0 else 0

    def showPlot(self, root):
        """
        function for showing the plot.

        :param root: window's root.
        :return: None
        """
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        self.canvas = None

        self.f = Figure(figsize=(5, 5), dpi=100)
        self.a = self.f.add_subplot(111)
        self.a.set_ylabel('Amount')
        self.a.bar(self.stats.keys(), self.stats.values())
        self.a.set_title('winrate: {winrate}%'.format(winrate=round(self.winrate, 2)))
        self.canvas = FigureCanvasTkAgg(self.f, master=root)
        self.canvas.get_tk_widget().place(x=700, y=0)
        self.canvas.draw()




