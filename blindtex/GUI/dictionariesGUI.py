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
        
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size = (wx.DisplaySize()[0]/3, wx.DisplaySize()[1]/5),
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
        
        
        self.mainSizer.Add(self.chooseDictBox, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        self.mainSizer.Add(self.selectedDictBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        self.principalPanel.SetSizer(self.mainSizer)
        
        self.Centre()
        self.Show()
        self.Fit()

    def selectDictionary(self, event):
        #Erase all the previous widgets.
        if self.selectedDictBoxSizer.GetChildren():
            for child in range(len(self.selectedDictBoxSizer.GetChildren())):
                self.selectedDictBoxSizer.Hide(child)
                self.selectedDictBoxSizer.Remove(child)

        dictName = self.dictComboBox.GetStringSelection()
        #Open the Dictionary.
        self.selectedDictionary = dictionary.dictionary(os.path.join('converter','dicts', dictName+'.json'))
        #Create a StaticBox
        self.slctdDictStaticBox = wx.StaticBox(self.principalPanel, label = dictName)
        self.slctdDictSizer = wx.StaticBoxSizer(self.slctdDictStaticBox, wx.VERTICAL)

        #The list with the commands
        self.commandsBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.slctdDictStaticText = wx.StaticText(self.principalPanel, label = dictName)
        self.slctdDictCommands = wx.ComboBox(self.principalPanel, choices = getCommandNames(dictName), style = wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.selectCommand, source = self.slctdDictCommands)
        self.commandsBoxSizer.Add(self.slctdDictStaticText, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        self.commandsBoxSizer.Add(self.slctdDictCommands, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        
        self.slctdDictSizer.Add(self.commandsBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border= 8, proportion = 1)
        #self.commandsBoxSizer.SetFocus()
        #BoxSizer with the command options
        self.commandOptionsBoxSizer = wx.BoxSizer(wx.VERTICAL)
        #Add Everything
        self.selectedDictBoxSizer.Add(self.slctdDictSizer,flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1 )
        self.principalPanel.Refresh()
        self.principalPanel.Layout()
        #EndOfFunction


    def selectCommand(self, event):
        
        #Erase all the previous widgets (there was a command change)
        if self.commandOptionsBoxSizer.GetChildren():
            for child in range(len(self.commandOptionsBoxSizer.GetChildren())):
                self.commandOptionsBoxSizer.Hide(child)
                self.commandOptionsBoxSizer.Remove(child)

        #Current Reading Box
        self.currentReadingBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.currReadingStaticText = wx.StaticText(self.principalPanel, label= "Lectura actual:")
        self.currReading = wx.TextCtrl(self.principalPanel,
                                       value = formulate.replaceHtml(self.selectedDictionary.showReading(self.slctdDictCommands.GetStringSelection()))
                                       , style= wx.TE_READONLY)
        print(formulate.replaceHtml(self.selectedDictionary.showReading(self.slctdDictCommands.GetStringSelection())))
        self.currentReadingBoxSizer.Add(self.currReadingStaticText, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        self.currentReadingBoxSizer.Add(self.currReading, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        
        self.commandOptionsBoxSizer.Add(self.currentReadingBoxSizer,flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        self.slctdDictSizer.Add(self.commandOptionsBoxSizer, flag = wx.ALL | wx.EXPAND | wx.CENTER, border = 8, proportion = 1)
        self.principalPanel.Refresh()
        self.principalPanel.Layout()
        #EndOfFunction
        




def openWindow():
    app = wx.App()
    mainWindow(None, title= 'Diccionarios')
    app.MainLoop()

def getDictsNames():
    try:
        myFile = open(os.path.join('converter','dicts','regexes.json'), 'r')
        #myFile = open('regexes.json')
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
