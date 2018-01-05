#!/usr/bin/python
#-*-:coding:utf-8-*-
import wx
import sys
import webbrowser
import os
import blindtex.converter.parser as parser

def convert(self, option, str):
    convertedFormula = u''
    parser.OPTION = option
    input = str
    inputSplit = input.split("\n")
    if option == 0:
        reload(sys)
        sys.setdefaultencoding('utf8')
        convertedFormula = '''<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title> Pruebas</title>
        </head>
        <body>
        <p>Fórmula generada:</p>'''
        for line in inputSplit:
            convertedFormula = convertedFormula + "<div>" + parser.convert(line) + "</div>" + "\n"
        convertedFormula = convertedFormula + '''</body>
        </html>'''
    if option == 1:
        for line in inputSplit:
            convertedFormula = convertedFormula + parser.convert(line) + "\n"
    return convertedFormula



class mainGUI(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=wx.GetDisplaySize(),
                          style= wx.RESIZE_BORDER | wx.SYSTEM_MENU |
                                wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

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

        # Textbox
        self.t1 = wx.TextCtrl(panel ,pos = (20,20), size=(2*self.GetSize()[0]/5, 4*self.GetSize()[1]/5), style = wx.TE_MULTILINE)

        #Botón
        self.button1 = wx.Button(panel, label="Conversión &literal", pos=(self.GetSize()[0]/2-57, self.GetSize()[1]/4))
        self.button1.Bind(wx.EVT_BUTTON, self.onClickConvertLiteral)



        #Textbox de resultado
        self.tf = wx.TextCtrl(panel ,pos = (self.GetSize()[0]-(2*self.GetSize()[0]/5+20),20), size = (2*self.GetSize()[0]/5, 4*self.GetSize()[1]/5), style = wx.TE_MULTILINE)

        self.button2 = wx.Button(panel, label="Convertir a &HTML", pos=(self.GetSize()[0] / 2 - 58, 3 * self.GetSize()[1] / 10))
        self.Bind(wx.EVT_BUTTON, self.onClickConvertHTML)


        self.Centre()
        self.Show()
        self.Maximize(True)
        self.Fit()



    def onClickConvertLiteral(self, event):
        if self.t1.GetValue() == "":
            print("No hay valores que mostrar")
        else:
            self.tf.SetValue(convert(self, 1, self.t1.GetValue()))

    def onClickConvertHTML(self, event):
        if self.t1.GetValue() == "":
            print("No hay valores que mostrar")
        else:
            with wx.FileDialog(self, "Abrir archivos txt file", wildcard="XYZ files (*.html)|*.html",
                               style=wx.FD_SAVE) as fileDialog:
                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return  # the user changed their mind

                # Proceed loading the file chosen by the user
                pathname = fileDialog.GetPath()
                try:
                    f = open(pathname, 'w')
                    f.write(convert(self, 0, self.t1.GetValue()))
                    f.close()
                    webbrowser.open(pathname)
                except IOError:
                    wx.LogError('Cannot open file')

    def OnQuit(self, event):
        self.Close()

    def onSave(self, event):
        with wx.FileDialog(self, "Guardar", wildcard="XYZ files (*.txt)|*.txt",
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
        with wx.FileDialog(self, "Abrir", wildcard="XYZ files (*.txt)|*.txt",
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
    mainGUI(None, title='BlindTex')
    app.MainLoop()

