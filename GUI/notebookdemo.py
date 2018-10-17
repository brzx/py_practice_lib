#!/usr/bin/python

import wx
class cjsave(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self,label='Page Three3')
        pass

if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, title="dd")
    nb = wx.Notebook(frame)
    n = cjsave(nb)
    b = cjsave(nb)
    nb.AddPage(n, "fiss")
    nb.AddPage(b, "fiss")
    frame.Show()
    app.MainLoop()