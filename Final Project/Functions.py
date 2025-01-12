#Import Liabriries
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile,askopenfiles
import customtkinter
import os
import string

#Variable For Two Files Text
global FileText
FileText=["",""]
#Variable for Multiple FILES
global Files
Files =[]
#Variable to Store Multiple File Text
global FilesText
FilesText=[]
#Variable to Store Duplicate Sentences
global Duplicates
Duplicates=[]

#Appearance Modes (Light Dark System)
def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

#Scaling Menu(80% 90% 100% 110% 120%)
def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)

#Function To Return Plagarism Percentage
def PlagarismPercentage(FileText_1,FileText_2):
    Sentences1=FileText_1.split("\n")
    Sentences2=FileText_2.split("\n")
    Count=0
    for x in Sentences1:
        for y in Sentences2:
            if x==y:
                Count=Count+len(x)
                break
    Similarity=Count*100/(len(FileText_1)-len(Sentences1))
    return int(Similarity)

#Function to Store Duplicate Sentences in Global Duplicates Array
def DuplicateSentences(FileText_1,FileText_2):
    Sentences1=FileText_1.split("\n")
    Sentences2=FileText_2.split("\n")
    global Duplicates
    Duplicates.clear()
    for x in Sentences1:
        x=x.strip()
    for x in Sentences2:
        x=x.strip()
    for x in Sentences1:
        for y in Sentences2:
            if x==y:
                Duplicates.append(x)
                break

#Function To Open File 1
def OpenFile1(ButtonText):
    ButtonText.set("Loading..")
    File1 = askopenfile(mode = 'r', title="Choose a File", filetypes=[("All files","*"),("text file","*.txt"),("java File","*.java"),("python file","*.py")])
    if File1 :
        ButtonText.set(os.path.basename(File1.name))
        global FileText
        FileText[0]=File1.read()
    else:
        ButtonText.set("Choose File 1")

#Function To Open File 2
def OpenFile2(ButtonText):
    ButtonText.set("Loading..")
    File2 = askopenfile(mode = 'r', title="Choose a File", filetypes=[("All files","*"),("text file","*.txt"),("java File","*.java"),("python file","*.py")])
    if File2 :
        ButtonText.set(os.path.basename(File2.name))
        global FileText
        FileText[1]=File2.read()
    else:
        ButtonText.set("Choose File 2")

#Function To Open Multiple Files
def OpenFiles(ButtonText):
    ButtonText.set("Loading..")
    global Files
    global FilesText
    Files.clear()
    Files = askopenfiles(mode ='r', title="Choose Multiple Files", filetypes=[("All files","*"),("text file","*.txt"),("java File","*.java"),("python file","*.py")])
    if Files:
        ButtonText.set((str(len(Files))+" Files Selected"))
        FilesText.clear()
        for x in Files:
            FilesText.append(x.read())
    else:
        ButtonText.set("CHOOSE FILES")

#Function to print result into textbox for two files
def TwoFileCompareResult(TextBox):
    TextBox.delete("1.0","end")
    global FileText
    global Duplicates
    Similarity = PlagarismPercentage(FileText[0],FileText[1])
    DuplicateSentences(FileText[0],FileText[1])
    for x in range(len(Duplicates)-1,0,-1):
        if Duplicates[x]!="":
            TextBox.insert("1.0",Duplicates[x])
            TextBox.insert("1.0","\n")
    TextBox.insert("1.0","\n\nDuplicate Sentences Are:\n")
    TextBox.insert("1.0",("Similarity Percentage is : "+str(Similarity)))

def MultipleCompareResult(TextBox):
    TextBox.delete("1.0","end")
    global Files
    global FilesText
    for x in FilesText:
        a=FilesText.index(x)
        for y in FilesText:
            b=FilesText.index(y)
            Similarity = PlagarismPercentage(x,y)
            FileName1=os.path.basename(Files[a].name)
            FileName2=os.path.basename(Files[b].name)
            TextBox.insert("1.0",(FileName1+"\t and \t"+FileName2+"\t  -  \t"+str(Similarity)))
            TextBox.insert("1.0","\n")
