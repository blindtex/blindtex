#!/usr/bin/python
#-*-:coding:utf-8-*-
import wx
import os
import blindtex.converter.parser as parser


class mainGUI(wx.Frame):



    def __init__(self, parent, title):
        super(mainGUI, self).__init__(parent, title=title,
                                      size=(1200, 600))

        # Barra de menú
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()

        qim = wx.MenuItem(fileMenu, 1, '&Salir\tCtrl+S')
        oim = wx.MenuItem(fileMenu, 2, '&Abrir\tCtrl+A')
        sim = wx.MenuItem(fileMenu, 3, '&Guardar\tCtrl+G')
        fileMenu.AppendItem(oim)
        fileMenu.AppendItem(sim)
        fileMenu.AppendItem(qim)

        menuBar.Append(fileMenu, '&Archivo')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnQuit, id = 1)
        self.Bind(wx.EVT_MENU, self.onOpen, id = 2)
        self.Bind(wx.EVT_MENU, self.onSave, id = 3)


        #Panel principal
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        grid = wx.GridSizer(2, 3, 1, 2)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # Textbox
        self.t1 = wx.TextCtrl(panel, size=(400, 500), style = wx.TE_MULTILINE)
        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.RIGHT, border = 20)

        #Botón
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.button = wx.Button(panel, label="Convertir", pos=(550,200))
        self.Bind(wx.EVT_BUTTON, self.onClick)

        #Textbox de resultado
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.tf = wx.TextCtrl(panel, size=(400, 500), style = wx.TE_MULTILINE)
        hbox3.Add(self.tf, 1, wx.EXPAND | wx.ALIGN_CENTER | wx.LEFT, 20)

        grid.AddMany([hbox1, (wx.StaticText(panel, size=(1,1)), wx.EXPAND) ,hbox3])
        vbox.Add(grid,proportion=0, flag=wx.EXPAND | wx.ALL,  border=20)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()
        self.Fit()

    def onClick(self, event):
        convertedFormula = u''
        parser.OPTION = 1
        input = self.t1.GetValue()
        inputSplit = input.split("\n")
        for line in inputSplit:
            convertedFormula = convertedFormula + parser.convert(line) + "\n"
        print(convertedFormula)
        self.tf.SetValue(convertedFormula)

    def OnQuit(self, event):
        self.Close()

    def onSave(self, event):
        with wx.FileDialog(self, "Abrir archivos txt file", wildcard="XYZ files (*.txt)|*.txt",
                           style=wx.FD_SAVE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                f = open(pathname, 'w')
                f.write(self.t1.GetValue())
                f.close()
            except IOError:
                wx.LogError('Cannot open file')


    def onOpen(self, event):
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Abrir archivos txt file", wildcard="XYZ files (*.txt)|*.txt",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    self.t1.SetValue(file.read())
                    file.close()
            except IOError:
                wx.LogError('Cannot open file')

if __name__ == '__main__':
    app = wx.App()
    mainGUI(None, title='BlindText')
    app.MainLoop()