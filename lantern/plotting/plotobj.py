from abc import abstractmethod, ABCMeta
from future.utils import with_metaclass
from .plotutils import get_color
from .plotobjs import AreaPlot, BarPlot, HistPlot, LinePlot, ScatterPlot, StepPlot, VLine, HLine, VSpan, HSpan


class BasePlotter(with_metaclass(ABCMeta)):
    def __init__(self, size=None, theme=None):
        self.size = size
        self.theme = theme

        self.line = []
        self.bar = []
        self.hist = []
        self.scatter = []
        self.step = []

        self.hline = []
        self.vline = []
        self.hspan = []
        self.vspan = []

        self.left = []
        self.right = []

        self.subplots = []
        self.subplot_dir = 'horizontal'

        self.legend = []

    @abstractmethod
    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        pass

    def area(self, data, color=None, y_axis='left', stacked=False, subplot='', **kwargs):
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            self.area.append(AreaPlot(data.index, data[col], _color, y_axis, stacked, subplot, **kwargs))
            self.legend.append((col, _color, y_axis))

    def bar(self, data, color=None, y_axis='left', stacked=False,  subplot='', **kwargs):
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            self.bar.append(BarPlot(data.index, data[col], _color, y_axis, stacked, subplot, **kwargs))
            self.legend.append((col, _color, y_axis))

    def hist(self, data, color=None, y_axis='left', stacked=False,  subplot='', **kwargs):
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            self.hist.append(HistPlot(data.index, data[col], _color, y_axis, stacked, subplot, **kwargs))
            self.legend.append((col, _color, y_axis))

    def hline(self, y, color=None, **kwargs):
        self.hline.append(HLine(y, color))

    def hspan(self, ylow, yhigh, color=None, **kwargs):
        self.hspan.append(HSpan(ylow, yhigh, color))

    def line(self, data, color=None, y_axis='left',  subplot='', **kwargs):
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            self.line.append(LinePlot(data.index, data[col], _color, y_axis, False, subplot, **kwargs))
            self.legend.append((col, _color, y_axis))

    def scatter(self, data, color=None, x=None, y=None,  y_axis='left',  subplot='', **kwargs):
        for i, col in enumerate(data):
            if i == 0:
                continue  # don't scatter against self
            _color = get_color(i, col, color)
            self.scatter.append(ScatterPlot(data.index, data[col], _color, y_axis, False, subplot, **kwargs))
            self.legend.append((col, _color, y_axis))

    def step(self, data, color=None, y_axis='left',  subplot='', **kwargs):
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            self.step.append(StepPlot(data.index, data[col], _color, y_axis, False, subplot, **kwargs))
            self.legend.append((col, _color, y_axis))

    def vline(self, x, color=None, **kwargs):
        self.vline.append(VLine(x, color))

    def vspan(self, xlow, xhigh, color=None, **kwargs):
        self.vspan.append(VSpan(xlow, xhigh, color))
