#!/usr/bin/env python
# -*-:coding:utf-8-*-

import wx
import os
import json
import sys
import converter.dictionary as dictionary
import converter.formulate as formulate

class mainWindow(wx.Frame):

    def __init__(self, parent, title):

        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size = (wx.DisplaySize()[0]/3, wx.DisplaySize()[1]/3),
                          style = wx.DEFAULT_FRAME_STYLE|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL)


        self.principalPanel = wx.Panel(self)
        self.principalPanel.SetBackgroundColour('#4f5049')

        #Main sizer.
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        #Dictionary selection Sizer.
        self.chooseDictBox = wx.BoxSizer(wx.HORIZONTAL)
        #Dictionary text
        self.dictTitle = wx.StaticText(self.principalPanel, label = 'Diccionarios')
        self.chooseDictBox.Add(self.dictTitle, border = 3, flag = wx.CENTER)
        #Dictionaries ComboBox
        self.dictComboBox = wx.ComboBox(self.principalPanel, choices = getDictsNames(), style = wx.TE_PROCESS_ENTER)
        self.chooseDictBox.Add(self.dictComboBox, border = 3, flag = wx.CENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.selectDictionary, source = self.dictComboBox)

        #Selected Dictionary Box Sizer
        self.selectedDictBoxSizer = wx.BoxSizer(wx.VERTICAL)
        #Create a StaticBox
        self.slctdDictStaticBox = wx.StaticBox(self.principalPanel, label = "Diccionario")
        self.slctdDictSizer = wx.StaticBoxSizer(self.slctdDictStaticBox, wx.VERTICAL)
        #The list with the commands
        self.commandsBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        #The Commands ComboBox
        self.slctdDictStaticText = wx.StaticText(self.principalPanel, label = 'Commandos:')
        self.slctdDictCommands = wx.ComboBox(self.principalPanel, choices = [], style = wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.selectCommand, source = self.slctdDictCommands)

        self.commandsBoxSizer.Add(self.slctdDictStaticText, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 3, proportion = 1)
        self.commandsBoxSizer.Add(self.slctdDictCommands, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 3, proportion = 1)
        #Selected CommandBox Sizer
        self.slctdCommandBoxSizer = wx.BoxSizer(wx.VERTICAL)
        #Current Reading
        self.currentReadingBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.currReadingStaticText = wx.StaticText(self.principalPanel, label= "Lectura actual:")
        self.currReading = wx.TextCtrl(self.principalPanel, value = "", style= wx.TE_READONLY)
        self.currentReadingBoxSizer.Add(self.currReadingStaticText, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        self.currentReadingBoxSizer.Add(self.currReading, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        #Command Possible Readings
        self.possibleReadingsBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.possibleReadingsStaticText = wx.StaticText(self.principalPanel, label = "Lecturas del Comando:")
        self.possibleReadingsComboBox = wx.ComboBox(self.principalPanel, choices = [], style = wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.chooseReading, source = self.possibleReadingsComboBox)
        self.possibleReadingsBoxSizer.Add(self.possibleReadingsStaticText,flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.possibleReadingsBoxSizer.Add(self.possibleReadingsComboBox ,flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        #Add Reading
        self.addReadingBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.addReadingTexts = wx.BoxSizer(wx.HORIZONTAL)
        self.addReadingStaticText = wx.StaticText(self.principalPanel, label = 'Añadir Lectura:')
        self.addReadingTextCtrl = wx.TextCtrl(self.principalPanel, value='')
        self.addReadingTexts.Add(self.addReadingStaticText, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.addReadingTexts.Add(self.addReadingTextCtrl, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.addReadingButton = wx.Button(self.principalPanel, label= "Añadir Lectura")
        self.Bind(wx.EVT_BUTTON, self.readingAdded, source = self.addReadingButton)
        self.addReadingBoxSizer.Add(self.addReadingTexts, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.addReadingBoxSizer.Add(self.addReadingButton,flag = wx.ALL | wx.CENTER, border= 8, proportion = 1)

        self.slctdCommandBoxSizer.Add(self.currentReadingBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.slctdCommandBoxSizer.Add(self.possibleReadingsBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.slctdCommandBoxSizer.Add(self.addReadingBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)

        #Add Command
        self.addCommandBoxSizer = wx.BoxSizer(wx.VERTICAL)
        #Add command Button
        self.addCommandButton = wx.Button(self.principalPanel, label = "Añadir Comando")
        self.Bind(wx.EVT_BUTTON, self.addCommandShow, source= self.addCommandButton)
        #New Command Space
        self.newCommandBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.newCommandStaticText = wx.StaticText(self.principalPanel, label = "Nuevo Comando:")
        self.newCommandTextCtrl = wx.TextCtrl(self.principalPanel, value = '' )
        self.newCommandBoxSizer.Add(self.newCommandStaticText, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.newCommandBoxSizer.Add(self.newCommandTextCtrl, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        #New Reading Space
        self.newReadingBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.newReadingStaticText = wx.StaticText(self.principalPanel, label = "Lectura:")
        self.newReadingTextCtrl = wx.TextCtrl(self.principalPanel, value = '', style = wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.addCommand, source = self.newReadingTextCtrl)
        self.newReadingBoxSizer.Add(self.newReadingStaticText, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.newReadingBoxSizer.Add(self.newReadingTextCtrl, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        #Confirm add Button
        self.confirmButton = wx.Button(self.principalPanel, label = "Confirmar")
        self.Bind(wx.EVT_BUTTON, self.addCommand, source= self.confirmButton)
        #The  Add Command Addings
        self.addCommandBoxSizer.Add(self.newCommandBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.addCommandBoxSizer.Add(self.newReadingBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.addCommandBoxSizer.Add(self.confirmButton, flag = wx.ALL | wx.CENTER, border= 8, proportion = 1)

        #The slctdDictSizer Addings
        self.slctdDictSizer.Add(self.commandsBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 3, proportion = 1)
        self.slctdDictSizer.Add(self.slctdCommandBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 3, proportion = 1)
        self.slctdDictSizer.Add(self.addCommandButton, flag = wx.ALL | wx.CENTER, border= 8, proportion = 1 )
        self.slctdDictSizer.Add(self.addCommandBoxSizer,flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 3, proportion = 1)
        self.slctdDictSizer.Show(self.commandsBoxSizer, show = False)
        self.slctdDictSizer.Show(self.slctdCommandBoxSizer, show = False)
        self.slctdDictSizer.Show(self.addCommandBoxSizer, show = False)

        self.selectedDictBoxSizer.Add(self.slctdDictSizer,flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1 )
        self.selectedDictBoxSizer.Show(self.slctdDictSizer, show = False)


        self.mainSizer.Add(self.chooseDictBox, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        self.mainSizer.Add(self.selectedDictBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        self.mainSizer.Show(self.selectedDictBoxSizer, show = False)
        self.principalPanel.SetSizer(self.mainSizer)

        self.Centre()
        self.Show()
        self.Fit()

    def selectDictionary(self, event):
        dictName = self.dictComboBox.GetStringSelection()
        #Open The dictionary
        self.selectedDictionary = dictionary.dictionary(os.path.join('converter','dicts', dictName+'.json'))

        self.slctdDictStaticBox.SetLabel(dictName)
        self.slctdDictCommands.Set(getCommandNames(dictName))
        self.selectedDictBoxSizer.Show(self.slctdDictSizer, show = True)
        self.slctdDictSizer.Show(self.commandsBoxSizer, show = True)
        self.slctdDictSizer.Show(self.addCommandButton, show = True)
        self.slctdDictSizer.Show(self.addCommandBoxSizer, show = False)
        self.principalPanel.Layout()
        #EndOfFunction


    def selectCommand(self, event):
        self.commandName = self.slctdDictCommands.GetStringSelection()
        #Shows Current Reading.
        self.currReading.SetValue(formulate.replaceHtml(self.selectedDictionary.showReading(self.commandName)))
        self.currReading.SetFocus()
        #Set the other possible readings.
        nonHtmlReadings = []
        for reading in self.selectedDictionary.showReadings(self.commandName):
            nonHtmlReadings.append(formulate.replaceHtml(reading))
        self.possibleReadingsComboBox.Set(nonHtmlReadings)

        #EndOfFunction
    def chooseReading(self, event):
        self.newPossibleReading = self.possibleReadingsComboBox.GetStringSelection()
        #Open Dialog (Idea From wx.Dialog documentation)
        self.changeReadingDialog =wx.MessageDialog(parent = None, message = "¿Quiere cambiar lectura a "+ self.newPossibleReading+"?", caption = "Cambio de Lectura",
                                                   style = wx.CLOSE_BOX|wx.YES_NO)
        if self.changeReadingDialog.ShowModal() == wx.ID_YES:
            self.selectedDictionary.changeReading(self.commandName, formulate.backHtml(self.newPossibleReading))
       #EndOfFunction

    def readingAdded(self, event):
        self.newReading = self.addReadingTextCtrl.GetValue()
        self.addReadingDialog = wx.MessageDialog(parent = None, message = "¿Quiere añadir la lectura %s?"%(self.newReading), style= wx.CLOSE_BOX| wx.YES_NO)
        if self.addReadingDialog.ShowModal() == wx.ID_YES:
            self.selectedDictionary.addReading(self.commandName, self.newReading)
            self.selectedDictionary.save()
        elif self.addReadingDialog.ShowModal() == wx.ID_NO:
            pass

        #EndOfFunction
    def addCommandShow(self, event):
        self.slctdDictSizer.Show(self.addCommandBoxSizer, show = True)
        self.principalPanel.Layout()
        #EndOfFunction
    def addCommand(self, event):
        self.newCommand = self.newCommandTextCtrl.GetValue()
        self.newCommandReading = self.newReadingTextCtrl.GetValue()
        self.addCommandDialog = wx.MessageDialog(parent = None, message = "¿Quiere añadir el comando %s, con la lectura %s ?"%(self.newCommand, self.newCommandReading),
                                                 style = wx.CLOSE_BOX|wx.YES_NO)
        if self.addCommandDialog.ShowModal() == wx.ID_YES:
            success =self.selectedDictionary.addCommand(self.newCommand, self.newCommandReading)
            self.selectedDictionary.save()
            if success:
                self.successDialog = wx.MessageDialog(parent = None, message = "Comando añadido Existosamente.", style = wx.OK)
                self.successDialog.ShowModal()
            else:
                self.failureDialog=wx.MessageDialog(parent = None, message = "Falla al añadir comando.", style = wx.OK)
                self.failureDialog.ShowModal()
        elif self.addReadingDialog.ShowModal == wx.ID_NO:
            pass
        #EndOfFunction



def openWindow():
    app = wx.App()
    mainWindow(None, title= 'Diccionarios')
    app.MainLoop()

def getDictsNames():
    try:
        myFile = open(os.path.join('converter','dicts','regexes.json'), 'r')
        dictOfDicts = json.load(myFile)
        myFile.close()
    except IOError:
        print('File could not be oppened.')

    return dictOfDicts.keys()

def getCommandNames(strDictName):
    try:
        myFile = open(os.path.join('converter','dicts', strDictName +'.json'), 'r')
        dictOfDicts = json.load(myFile)
        myFile.close()
    except IOError:
        print('File could not be oppened.')

    return dictOfDicts.keys()

if __name__ == "__main__":
    openWindow()
