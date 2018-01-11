#!/usr/bin/env python
#-*-:coding:utf-8-*-

import wx
import sys
import webbrowser
from blindTex.GUI.controller import mainController
import os
if os.name == "nt":
    import converter.parser as parser
elif os.name == "posix":
    import parser as parser

class mainGUI(wx.Frame):

    sLector = 0

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=wx.GetDisplaySize(),
                          style= wx.RESIZE_BORDER | wx.SYSTEM_MENU |
                                wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        # Barra de menú
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        lectorMenu = wx.Menu()

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

        VoiceOverItem = lectorMenu.Append(wx.NewId(), "VoiceOver/Jaws\tALT+V","HTML para VoiceOver", wx.ITEM_RADIO)
        nvdaItem = lectorMenu.Append(wx.NewId(),'NVDA\tALT+N', 'HTML para NVDA', wx.ITEM_RADIO)


        self.Bind(wx.EVT_MENU, self.voiceOverChek, VoiceOverItem)
        self.Bind(wx.EVT_MENU, self.nvdaChek, nvdaItem)

        menuBar.Append(lectorMenu, '&Configuración')


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
        self.button2.Bind(wx.EVT_BUTTON, self.onClickConvertHTML)


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
        if self.t1.GetValue() == "":
            print("No hay valores que mostrar")
        else:
            parser.OPTION = 1
            self.tf.SetValue(mainController.convert(self.t1.GetValue()))

    def onClickConvertHTML(self, event):
        if self.t1.GetValue() == "":
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
                    f.write(mainController.convert(self.t1.GetValue()))
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



def run():
    app = wx.App()
    mainGUI(None, title='BlindTex')
    app.MainLoop()
