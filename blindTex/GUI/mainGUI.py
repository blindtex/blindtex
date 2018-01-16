#!/usr/bin/env python
#-*-:coding:utf-8-*-

import wx
import sys
import webbrowser
import os
try:
    sys.path.insert(0, 'blindtex')
    import converter.parser as parser
except ValueError:
    import blindtex.converter.parser as parser

import mainBlindtex

def convert(str):
    convertedFormula = u''
    input = str
    inputSplit = input.split("\n")
    if parser.OPTION != 1:
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
    if parser.OPTION == 1:
        for line in inputSplit:
            convertedFormula = convertedFormula + parser.convert(line) + "\n"
    return convertedFormula

class mainGUI(wx.Frame):

    sLector = 0

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=wx.GetDisplaySize(),
                          style= wx.RESIZE_BORDER | wx.SYSTEM_MENU |
                                wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        # Barra de menú
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        actionMenu = wx.Menu()
        lectorMenu = wx.Menu()

        qim = wx.MenuItem(fileMenu, 1, '&Salir\tCtrl+S')
        oim = wx.MenuItem(fileMenu, 2, '&Abrir\tCtrl+A')
        sim = wx.MenuItem(fileMenu, 3, '&Guardar\tCtrl+G')
        fileMenu.Append(oim)
        fileMenu.Append(sim)
        fileMenu.Append(qim)

        #Menú de Archivo
        menuBar.Append(fileMenu, '&Archivo')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnQuit, id = 1)
        self.Bind(wx.EVT_MENU, self.onOpen, id = 2)
        self.Bind(wx.EVT_MENU, self.onSave, id = 3)

        #Menú de acciones
        cLiteral = wx.MenuItem(actionMenu, 4, "Conversión literal\tALT+L")
        cHTML = wx.MenuItem(actionMenu, 5, "Convertir a HTML\tALT+H")
        cDocument = wx.MenuItem(actionMenu, 6, "Convertir documento\tALT+D")
        actionMenu.Append(cDocument)
        actionMenu.Append(cLiteral)
        actionMenu.Append(cHTML)

        self.Bind(wx.EVT_MENU, self.onClickConvertLiteral, cLiteral, 4)
        self.Bind(wx.EVT_MENU, self.onClickConvertHTML, cHTML, 5)
        self.Bind(wx.EVT_MENU, self.onClickConvertFile, cDocument, 6)

        menuBar.Append(actionMenu, '&Acciones')

        #Menú de configuraciones
        VoiceOverItem = lectorMenu.Append(wx.NewId(), "VoiceOver/Jaws\tALT+V","HTML para VoiceOver", wx.ITEM_RADIO)
        nvdaItem = lectorMenu.Append(wx.NewId(),'NVDA\tALT+N', 'HTML para NVDA', wx.ITEM_RADIO)


        self.Bind(wx.EVT_MENU, self.voiceOverChek, VoiceOverItem)
        self.Bind(wx.EVT_MENU, self.nvdaChek, nvdaItem)

        menuBar.Append(lectorMenu, '&Configuración')


        #Panel principal
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')

        # Textbox
        self.inputTextbox = wx.TextCtrl(panel ,pos = (20,20), size=(9*self.GetSize()[0]/20, 4*self.GetSize()[1]/5), style = wx.TE_MULTILINE)

        #Textbox de resultado
        self.tf = wx.TextCtrl(panel ,pos = (self.GetSize()[0]-(9*self.GetSize()[0]/20+20),20), size = (9*self.GetSize()[0]/20, 4*self.GetSize()[1]/5), style = wx.TE_MULTILINE | wx.TE_READONLY)


        self.Centre()
        self.Show()
        self.Maximize(True)
        self.Fit()

    def nvdaChek(self, event):
        parser.OPTION = 2
        self.sLector = 2

    def voiceOverChek(self, event):
        parser.OPTION = 0
        self.sLector = 0

    def onClickConvertLiteral(self, event):
        if self.inputTextbox.GetValue() == "":
            print("No hay valores que mostrar")
        else:
            
            parser.OPTION = 1
            self.tf.SetValue(convert(self.inputTextbox.GetValue()))

    def onClickConvertHTML(self, event):
        if self.inputTextbox.GetValue() == "":
            print("No hay valores que mostrar")
        else:
            with wx.FileDialog(self, "Abrir archivos txt file", wildcard="(*.html)|*.html",
                               style=wx.FD_SAVE) as fileDialog:
                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return  # the user changed their mind

                if parser.OPTION == 1:
                    parser.OPTION = self.sLector
                # Proceed loading the file chosen by the user
                pathname = fileDialog.GetPath()
                try:
                    f = open(pathname, 'w')
                    f.write(convert(self.inputTextbox.GetValue()))
                    f.close()
                    webbrowser.open(pathname)
                except IOError:
                    wx.LogError('Cannot open file')

    def onClickConvertFile(self, event):
        
        with wx.FileDialog(self, "Convertir Documento", wildcard = "Archivo (La)TeX (.tex) |*.tex") as fileDialog:
                if fileDialog.ShowModal()== wx.ID_CANCEL:
                        return

                pathName = fileDialog.GetPath()
                mainBlindtex.convertDocument(pathName)
                webbrowser.open(pathName.replace('.tex','.xhtml'))

    #EndOfFunction

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
                f.write(self.inputTextbox.GetValue())
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
                    self.inputTextbox.SetValue(file.read())
                    file.close()
            except IOError:
                wx.LogError('Cannot open file')



def run():
    app = wx.App()
    mainGUI(None, title='BlindTex')
    app.MainLoop()
