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


welcomeString = '''Bienvenido a BlindTeX.\nPuede convertir fórmulas con las teclas Alt+L.\nPuede convertir documentos con las teclas Alt+D.\n '''
class mainGUI(wx.Frame):

    sLector = 0

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(wx.DisplaySize()[0]/3,2*wx.DisplaySize()[1]/5),
                          style= wx.RESIZE_BORDER | wx.SYSTEM_MENU |
                                wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL)

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

	self.mainBox = wx.BoxSizer(wx.VERTICAL)

        self.summaryText  = wx.StaticText(panel, label = welcomeString)#Change label in the definition!!
        self.summaryText.SetFocus()
        self.textsBox = wx.StaticBoxSizer(wx.HORIZONTAL, panel, "Fórmulas")
                                                    

        self.inputBox = wx.BoxSizer(wx.VERTICAL)
        self.inputLabel = wx.StaticText(panel, label = "Fórmulas a convertir")
        self.inputTextbox = wx.TextCtrl(panel, style = wx.TE_MULTILINE)
        self.inputBox.Add(self.inputLabel, flag = wx.BOTTOM, border = 2)
        self.inputBox.Add(self.inputTextbox, flag =wx.CENTER|wx.EXPAND , proportion = 1)
                                    
        self.outputBox = wx.BoxSizer(wx.VERTICAL)
        self.outputLabel = wx.StaticText(panel,label = "Fórmulas convertidas")
        self.outputText = wx.TextCtrl(panel, style = wx.TE_MULTILINE|wx.TE_READONLY)
        self.outputBox.Add(self.outputLabel)
        self.outputBox.Add(self.outputText, flag = wx.CENTER|wx.EXPAND, proportion = 1)
                                    
        self.textsBox.Add(self.inputBox, flag = wx.ALL, border= 8, proportion = 1)
        self.textsBox.Add(self.outputBox, flag= wx.ALL,  border = 8, proportion = 1)

        self.mainBox.Add(self.summaryText, flag = wx.ALL|wx.CENTER, border = 0, proportion = 1)
        self.mainBox.Add(self.textsBox, flag = wx.EXPAND, border = 0, proportion = 1)

        panel.SetSizerAndFit(self.mainBox)


        self.Centre()
        self.Show()
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
            self.outputText.SetValue(convert(self.inputTextbox.GetValue()))
            self.outputText.SetFocus()

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
                wx.MessageBox('Documento convertido exitosamente.', 'Documento completado.', wx.OK)
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
