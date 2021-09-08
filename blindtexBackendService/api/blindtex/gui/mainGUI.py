#!/usr/bin/env python
# -*-:coding:utf-8-*-

import wx
import threading
import webbrowser
import os
import dictionariesGUI
import converter.parser as parser
import mainGUIController

welcomeString = '''Bienvenido a BlindTeX.\nPuede convertir fórmulas con las teclas Alt+L.\nPuede convertir documentos con las teclas Alt+D.\n '''

def convertProcess(path):
    global presult
    presult = mainGUIController.onClickConvertFileController(path)
def convertProcessPdf(path):
    global presult
    presult = mainGUIController.onClickConvertToPdfController(path)

class mainGUI(wx.Frame):
    sLector = 0
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(wx.DisplaySize()[0] / 3, 2 * wx.DisplaySize()[1] / 5),
                          style=wx.DEFAULT_FRAME_STYLE | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL)

        # Barra de menú
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        editionMenu = wx.Menu()
        actionMenu = wx.Menu()
        lectorMenu = wx.Menu()

        qim = wx.MenuItem(fileMenu, 1, '&Salir\tCtrl+S')
        oim = wx.MenuItem(fileMenu, 2, '&Abrir\tCtrl+A')
        sim = wx.MenuItem(fileMenu, 3, '&Guardar\tCtrl+G')
        fileMenu.Append(oim)
        fileMenu.Append(sim)
        fileMenu.Append(qim)

        # Menú de Archivo
        menuBar.Append(fileMenu, '&Archivo')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=1)
        self.Bind(wx.EVT_MENU, self.onOpen, id=2)
        self.Bind(wx.EVT_MENU, self.onSave, id=3)

        # Menú de Edición
        copy = wx.MenuItem(editionMenu, -1, "&Copiar\tCtrl+C")
        paste = wx.MenuItem(editionMenu, -1, "&Pegar\tCtrl+V")
        cut = wx.MenuItem(editionMenu, -1, "&Cortar\tCtrl+X")
        selectAll = wx.MenuItem(editionMenu, -1, "&Seleccionar todo\tCtrl+E")
        editionMenu.Append(copy)
        editionMenu.Append(paste)
        editionMenu.Append(cut)
        editionMenu.Append(selectAll)

        self.Bind(wx.EVT_MENU, self.onCopy, copy)
        self.Bind(wx.EVT_MENU, self.onPaste, paste)
        self.Bind(wx.EVT_MENU, self.onCut, cut)
        self.Bind(wx.EVT_MENU, self.onSelectAll, selectAll)

        menuBar.Append(editionMenu, "&Edición")

        # Menú de acciones
        cLiteral = wx.MenuItem(actionMenu, 4, "Conversión literal\tALT+L")
        cHTML = wx.MenuItem(actionMenu, 5, "Convertir a HTML\tALT+H")
        cDocument = wx.MenuItem(actionMenu, 6, "Convertir documento\tALT+D")
        cDict = wx.MenuItem(actionMenu,7, "Diccionarios\tALT+F")
        cConvertToPdf = wx.MenuItem(actionMenu, 8, "Convertir a Pdf\tALT+P")#These controls will have to be modified.
        actionMenu.Append(cDocument)
        actionMenu.Append(cLiteral)
        actionMenu.Append(cHTML)
        actionMenu.Append(cDict)
        actionMenu.Append(cConvertToPdf)

        self.Bind(wx.EVT_MENU, self.onClickConvertLiteral, cLiteral, 4)
        self.Bind(wx.EVT_MENU, self.onClickConvertHTML, cHTML, 5)
        self.Bind(wx.EVT_MENU, self.onClickConvertFile, cDocument, 6)
        self.Bind(wx.EVT_MENU, self.onClickOpenDictionary, cDict, 7)
        self.Bind(wx.EVT_MENU, self.onClickConvertToPdf, cConvertToPdf, 8)

        menuBar.Append(actionMenu, '&Acciones')

        # Menú de configuraciones
        VoiceOverItem = lectorMenu.Append(wx.NewId(), "VoiceOver/Jaws\tALT+V", "HTML para VoiceOver", wx.ITEM_RADIO)
        nvdaItem = lectorMenu.Append(wx.NewId(), 'NVDA\tALT+N', 'HTML para NVDA', wx.ITEM_RADIO)
        literalItem = lectorMenu.Append(wx.NewId(), 'Literal\tALT+M', 'HTML Literal', wx.ITEM_RADIO)

        self.Bind(wx.EVT_MENU, self.voiceOverChek, VoiceOverItem)
        self.Bind(wx.EVT_MENU, self.nvdaChek, nvdaItem)
        self.Bind(wx.EVT_MENU, self.literalCheck, literalItem)

        menuBar.Append(lectorMenu, '&Configuración')

        # Panel principal
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#4f5049')

        self.mainBox = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.summaryText = wx.StaticText(panel, label=welcomeString)  # Change label in the definition!!
        self.summaryText.SetFocus()
        self.summaryText.SetFont(font)
        self.summaryText.SetForegroundColour('#FFFFFF')

        self.box = wx.StaticBox(panel, -1, "Fórmulas")
        self.box.SetFont(font)
        self.box.SetForegroundColour("#FFFFFF")
        self.textsBox = wx.StaticBoxSizer(self.box, wx.HORIZONTAL)

        self.inputBox = wx.BoxSizer(wx.VERTICAL)
        self.inputLabel = wx.StaticText(panel, label="Fórmulas a convertir")
        self.inputLabel.SetFont(font)
        self.inputLabel.SetForegroundColour('#FFFFFF')
        self.inputTextbox = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.inputBox.Add(self.inputLabel, flag=wx.BOTTOM, border=2)
        self.inputBox.Add(self.inputTextbox, flag=wx.CENTER | wx.EXPAND, proportion=1)

        self.outputBox = wx.BoxSizer(wx.VERTICAL)
        self.outputLabel = wx.StaticText(panel, label="Fórmulas convertidas")
        self.outputLabel.SetFont(font)
        self.outputLabel.SetForegroundColour('#FFFFFF')
        self.outputText = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.outputBox.Add(self.outputLabel)
        self.outputBox.Add(self.outputText, flag=wx.CENTER | wx.EXPAND, proportion=1)

        self.textsBox.Add(self.inputBox, flag=wx.ALL | wx.EXPAND, border=8, proportion=1)
        self.textsBox.Add(self.outputBox, flag=wx.ALL | wx.EXPAND, border=8, proportion=1)

        self.mainBox.Add(self.summaryText, flag=wx.ALL | wx.CENTER, border=0, proportion=1)
        self.mainBox.Add(self.textsBox, flag=wx.EXPAND, border=0, proportion=1)

        panel.SetSizerAndFit(self.mainBox)

        self.Centre()
        self.Show()
        self.Fit()

    def onCut(self, event):
        self.inputTextbox.Cut()

    def onCopy(self, event):
        self.inputTextbox.Copy()

    def onPaste(self, event):
        self.inputTextbox.Paste()

    def onDelete(self, event):
        frm, to = self.inputTextbox.GetSelection()
        self.inputTextbox.Remove(frm, to)

    def onSelectAll(self, event):
        self.inputTextbox.SelectAll()

    def nvdaChek(self, event):
        parser.setOption(2)
        self.sLector = 2


    def voiceOverChek(self, event):
        parser.setOption(0)
        self.sLector = 0


    def literalCheck(self, event):
        parser.setOption(1)
        self.sLector = 1


    def onClickConvertLiteral(self, event):
        if self.inputTextbox.GetValue() == "":
            print("No hay valores que mostrar")
        else:
            parser.setOption(1)
            self.outputText.SetValue(mainGUIController.convert(self.inputTextbox.GetValue()))
            self.outputText.SetFocus()

    def onClickConvertHTML(self, event):
        if self.inputTextbox.GetValue() == "":
            print("No hay valores que mostrar")
        else:
            temPath = os.getcwd()
            ecuation = self.inputTextbox.GetValue()
            try:
                f = open(temPath + "temp.html", 'w')
                f.write(mainGUIController.convert(ecuation))
                f.close()
                webbrowser.open(temPath + "temp.html")
                message = wx.MessageDialog(self, "¿Desea guardar el archivo generado?", "Guardar HTML",
                                           wx.YES_NO | wx.ICON_QUESTION)
                answer = message.ShowModal()
                if answer == wx.ID_YES:
                    message.Destroy()
                    os.remove(temPath + "temp.html")
                    with wx.FileDialog(self, "Abrir archivos HTML", wildcard="(*.html)|*.html",
                                       style=wx.FD_SAVE) as fileDialog:
                        if fileDialog.ShowModal() == wx.ID_CANCEL:
                            return

                        if parser.getOption() == 1:
                            parser.setOption(self.sLector)
                        # Proceed loading the file chosen by the user
                        pathname = fileDialog.GetPath()
                        try:
                            f = open(pathname, 'w')
                            f.write(mainGUIController.convert(ecuation))
                            f.close()
                            webbrowser.open(pathname)
                        except IOError:
                            wx.LogError('Cannot open file')
                else:
                    message.Destroy()
                    os.remove(temPath + "temp.html")
            except IOError:
                wx.LogError('Cannot open file')



    def onClickConvertFile(self, event):

        with wx.FileDialog(self, "Convertir Documento", wildcard="Archivo (La)TeX (.tex) |*.tex") as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            pathName = fileDialog.GetPath()



            wait = wx.BusyInfo("El archivo está siendo convertido, porfavor espere...")
            threatProcess = threading.Thread(target=convertProcess(pathName))
            threatProcess.start()

            if (presult):
                del wait
                successm = wx.MessageDialog(self, 'Documento convertido exitosamente.', 'Documento completado.', wx.OK)
                successm.ShowModal()
                successm.Destroy()
                webbrowser.open(pathName.replace('.tex', '.xhtml'))
            else:
                del wait
                errorm = wx.MessageDialog(self, 'Ha habido un error', "Error", wx.OK | wx.ICON_WARNING)
                errorm.ShowModal()
                errorm.Destroy()

    # EndOfFunction


    def onClickOpenDictionary(self, event):
        dictionariesGUI.openWindow()

    def onClickConvertToPdf(self,event):
        with wx.FileDialog(self, "Convertir Documento", wildcard="Archivo (La)TeX (.tex) |*.tex") as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            pathName = fileDialog.GetPath()



            wait = wx.BusyInfo("El archivo está siendo convertido, porfavor espere...")
            threatProcess = threading.Thread(target=convertProcessPdf(pathName))
            threatProcess.start()

            if (presult):
                del wait
                successm = wx.MessageDialog(self, 'Documento convertido exitosamente.', 'Documento completado.', wx.OK)
                successm.ShowModal()
                successm.Destroy()
                #webbrowser.open(pathName.replace('.tex', '.xhtml'))
            else:
                del wait
                errorm = wx.MessageDialog(self, 'Ha habido un error', "Error", wx.OK | wx.ICON_WARNING)
                errorm.ShowModal()
                errorm.Destroy()

        #EndOfFunction

    def OnQuit(self, event):
        self.Close()

    def onSave(self, event):
        with wx.FileDialog(self, "Guardar", wildcard="(*.txt)|*.txt",
                           style=wx.FD_SAVE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            text = self.inputTextbox.GetValue()
            if (mainGUIController.onSaveController(pathname, text) == False):
                wx.LogError('No se pudo abrir el archivo')

    def onOpen(self, event):
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Abrir", wildcard="(*.txt)|*.txt",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    self.inputTextbox.SetValue(file.read())
                    file.close()
            except IOError:
                wx.LogError('No se pudo abrir el archivo')


def run():
    app = wx.App()
    mainGUI(None, title='BlindTex')
    app.MainLoop()
