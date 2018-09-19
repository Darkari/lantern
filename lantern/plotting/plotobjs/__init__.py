class BasePlot(object):
    def __init__(self, x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs):
        self.x = x
        self.y = y
        self.color = color
        self.y_axis = y_axis
        self.stacked = stacked
        self.subplot = subplot
        self.kwargs = kwargs


class AreaPlot(BasePlot):
    def __init__(self, x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs):
        super(AreaPlot, self).__init__(x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs)


class BarPlot(BasePlot):
    def __init__(self, x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs):
        super(BarPlot, self).__init__(x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs)


class HistPlot(BasePlot):
    def __init__(self, x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs):
        super(HistPlot, self).__init__(x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs)


class LinePlot(BasePlot):
    def __init__(self, x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs):
        super(LinePlot, self).__init__(x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs)


class ScatterPlot(BasePlot):
    def __init__(self, x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs):
        super(ScatterPlot, self).__init__(x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs)


class StepPlot(BasePlot):
    def __init__(self, x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs):
        super(StepPlot, self).__init__(x, y, color=None, y_axis='left', stacked=False, subplot='', **kwargs)


class RangeObject(object):
    def __init__(self, x_min, y_min, x_max, y_max, color):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.color = color


class VLine(RangeObject):
    def __init__(self, x, color):
        super(VLine, self).__init__(self, x, None, x, None, color)


class HLine(RangeObject):
    def __init__(self, y, color):
        super(HLine, self).__init__(self, None, y, None, y, color)


class VSpan(RangeObject):
    def __init__(self, x_low, x_high, color):
        super(VSpan, self).__init__(self, x_low, None, x_high, None, color)


class HSpan(RangeObject):
    def __init__(self, y_low, y_high, color):
        super(HSpan, self).__init__(self, None, y_low, None, y_high, color)
