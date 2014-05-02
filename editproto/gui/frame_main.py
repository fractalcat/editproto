import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, id, opts):
        wx.Frame.__init__(self, parent)
        self.Show(True)
        self.Maximize(True)
