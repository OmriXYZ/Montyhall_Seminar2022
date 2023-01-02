import matplotlib

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

    def update(self, wins, losses):
        """
        update plot.
        :param wins: wins
        :param losses: losses
        :return: None
        """
        self.stats.update({'wins': wins})
        self.stats.update({'loses': losses})

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
        self.a.bar(self.stats.keys(), self.stats.values())
        self.canvas = FigureCanvasTkAgg(self.f, master=root)
        self.canvas.get_tk_widget().place(x=700, y=0)
        self.canvas.draw()
