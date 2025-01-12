from tkinter import *
from tkinter .messagebox import showinfo
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfilename
import os
'''root=Tk()
root.title("Untitled - Notepad")
root.geometry('644x788')'''
file=None

def newFile(root,TextArea):
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile(root,TextArea):
    global file
    file=askopenfile(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    print(file)
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        root.title('Notepad')
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())

def saveFile(root,TextArea):
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            print('File Saved')

    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def saveAsFile(root,TextArea):
    global file
    file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+" - Notepad")
        print('File Saved')

def quitApp(root):
    root.destroy()

def cut(TextArea):
    TextArea.event_generate(("<<Cut>>"))

def copy(TextArea):
    TextArea.event_generate(("<<Copy>>"))

def paste(TextArea):
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Developed by Krishna")

def undo(TextArea):
    TextArea.event_generate(("<<Undo>>"))

def delete(TextArea):
    TextArea.delete(1.0,END)

def wrapText(TextArea,wrapVal):
    if wrapVal.get()==1:
        TextArea.config(wrap=None)
    else:
        TextArea.config(wrap="none")

def newWindow(root,TextArea):
    global file
    root=Tk()
    root.title("Untitled - Notepad")
    root.geometry('644x788')    
    TextArea=Text(root,font="lucida 13",undo=True,wrap="none")
    TextArea.pack(expand=True,fill=BOTH)
    file=None
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    HorizontalScroll=Scrollbar(root,orient=HORIZONTAL)
    HorizontalScroll.pack(side=BOTTOM,fill=X)
    HorizontalScroll.config(command=TextArea.xview)
    TextArea.config(yscrollcommand=Scroll.set,xscrollcommand=HorizontalScroll.set)
    Menubar=Menu(root)
    FileMenu=Menu(Menubar,tearoff=0)
    FileMenu.add_command(label="New                          Ctrl+N",command=lambda:newFile(root,TextArea))
    FileMenu.add_command(label="New Window          Ctrl+Shift+N",command=lambda:newWindow(root,TextArea))
    FileMenu.add_command(label="Open                        Ctrl+O",command=lambda:openFile(root,TextArea))
    FileMenu.add_command(label="Save                          Ctrl+S",command=lambda:saveFile(root,TextArea))
    FileMenu.add_command(label="Save As                     Ctrl+Shift+S",command=lambda:saveAsFile(root))
    FileMenu.add_separator()
    FileMenu.add_command(label="Page Setup")
    FileMenu.add_command(label="Print                          Ctrl+P")
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=FileMenu)
    root.config(menu=Menubar)

    EditMenu=Menu(Menubar,tearoff=0)
    EditMenu.add_command(label="Undo                                  Ctrl+Z",command=lambda:undo(TextArea))
    EditMenu.add_separator()
    EditMenu.add_command(label="Cut                                     Ctrl+X",command=lambda:cut(TextArea))
    EditMenu.add_command(label="Copy                                  Ctrl+C",command=lambda:copy(TextArea))
    EditMenu.add_command(label="Paste                                  Ctrl+V",command=lambda:paste(TextArea))
    EditMenu.add_command(label="Delete                                 Del",command=lambda:delete(TextArea))
    EditMenu.add_separator()
    EditMenu.add_command(label="Search with Bing...           Ctrl+E")
    EditMenu.add_command(label="Find                                    Ctrl+F")
    EditMenu.add_command(label="Find Next                           F3")
    EditMenu.add_command(label="Find Previous                    Shift+F3")
    EditMenu.add_command(label="Replace...                           Ctrl+H")
    EditMenu.add_command(label="Go To...                              Ctrl+G")
    EditMenu.add_separator()
    EditMenu.add_command(label="Select All                           Ctrl+A")
    EditMenu.add_command(label="Time/Date                         F5")
    Menubar.add_cascade(label="Edit",menu=EditMenu)

    FormatMenu=Menu(Menubar,tearoff=0)
    wrapVal=IntVar()
    FormatMenu.add_checkbutton(label="Word Wrap",variable=wrapVal,onvalue=1,offvalue=0,command=lambda:wrapText(TextArea,wrapVal))
    FormatMenu.add_command(label="Font...")
    Menubar.add_cascade(label="Format",menu=FormatMenu)

    ViewMenu=Menu(Menubar,tearoff=0)
    Zoom=Menu(ViewMenu,tearoff=0)
    ViewMenu.add_cascade(label='Zoom',menu=Zoom)
    Zoom.add_command(label="Zoom In                                      Ctrl+Plus")
    Zoom.add_command(label="Zoom Out                                   Ctrl+Minus")
    Zoom.add_command(label="Restore Default Zoom               Ctrl+O")
    checkval=IntVar()
    ViewMenu.add_checkbutton(label="Status Bar",variable=checkval,onvalue=1,offvalue=0)
    checkval.set(1)
    Menubar.add_cascade(label="View",menu=ViewMenu)

    HelpMenu=Menu(Menubar,tearoff=0)
    HelpMenu.add_command(label="View Help")
    HelpMenu.add_command(label="Send Feedback")
    HelpMenu.add_separator()
    HelpMenu.add_command(label='About Notepad',command=about)
    Menubar.add_cascade(label="Help",menu=HelpMenu)

    root.mainloop()

root=""
TextArea=""
newWindow(root,TextArea)
