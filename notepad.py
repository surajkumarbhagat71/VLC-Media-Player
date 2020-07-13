from wx import *
a = App()
f = Frame(None,title="suraj notpad",size=(500,600))
f.Center()
p = Panel(f)
mbar = MenuBar()

file = Menu()
edit = Menu()
format = Menu()
view = Menu()
help = Menu()

mbar.Append(file,"File")
mbar.Append(edit,"Edit")
mbar.Append(format,"Format")
mbar.Append(view,"View")
mbar.Append(help,"Help")

#forfile**********************************************************
new = MenuItem(file,ID_NEW,text="New \tCtrl+n")

opens = MenuItem(file,ID_OPEN,text="Open \tCtrl+O")
save = MenuItem(file,ID_SAVE,text="Save \tCtrl+S")
save_as = MenuItem(file,ID_ANY,text="Save As")
page_s = MenuItem(file,ID_ANY,text="Page Satup")
prints = MenuItem(file,ID_ANY,text="Print \tCtrl+P")
exit = MenuItem(file,ID_ANY,text="Exit")

file.Append(new)
file.Append(opens)
file.Append(save)
file.Append(save_as)
file.Append(page_s)
file.Append(prints)
file.Append(exit)

#foredit*****************************************************************

undo = MenuItem(edit,ID_ANY,text="Undo \tCtrl+z")
cut = MenuItem(edit,ID_CUT,text="Cut \tCtrl+x")
copy = MenuItem(edit,ID_COPY,text="Copy \tCtrl+c")
paste = MenuItem(edit,ID_PASTE,text="Paste \tCtrl+v")
delete = MenuItem(edit,ID_DELETE,text="Delete \tCtrl+D")
find = MenuItem(edit,ID_FIND,text="Find \tCtrl+v")
f_next = MenuItem(edit,ID_ANY,text="Find Next \tF3")
replace = MenuItem(edit,ID_ANY,text="Replace \tCtrl+H")
go_to = MenuItem(edit,ID_ANY,text="Go To")
selete_all = MenuItem(edit,ID_ANY,text="Select All\tCtrl+a")
time = MenuItem(edit,ID_ANY,text="Time/Delete \tF5")


edit.Append(undo)
edit.Append(cut)
edit.Append(copy)
edit.Append(paste)
edit.Append(delete)
edit.Append(find)
edit.Append(f_next)
edit.Append(replace)
edit.Append(go_to)
edit.Append(selete_all)
edit.Append(time)

#FORformat
word = MenuItem(format,ID_ANY,text="Word Wrap")
font = MenuItem(format,ID_SELECT_FONT,text="Font..")
zoom_in = MenuItem(format,ID_ZOOM_IN,text="Zoom in \tCtrl+z")
zoom_out = MenuItem(format,ID_ZOOM_OUT,text="Zoom out \tCtrl+k")


format.Append(word)
format.Append(font)
format.Append(zoom_in)
format.Append(zoom_out)

#forview
stetus = MenuItem(view,ID_ANY,text="Stetus Bar")

view.Append(stetus)

#forhelp
v_help = MenuItem(help,ID_ANY,text="View Help")
about = MenuItem(help,ID_ANY,text="About Notepad")

help.Append(v_help)
help.Append(about)

#BOX*******************************************
box = BoxSizer()
text = TextCtrl(p,style=TE_MULTILINE)
box.Add(text,1,ALL|EXPAND)

def font_change(event):
    foo = FontDialog(None)
    if foo.ShowModal()==ID_OK:
        font = foo.GetFontData()
        new_font = font.GetChoienFont()
        colour = fnot.GetColour()
        text.SetFont(new_font)
        text.SetForegroundColour(colour)

format.Bind(EVT_MENU,font_change,font)


def open_file(event):
    wild = "text and doc (*.txt;*.doc)|*.txt;*.docx|all file|*.*"
    w = FileDialog(None,"open karo","e://",wildcard=wild,style=FD_OPEN)
    if w.ShowModal()==ID_OK:
        files = open(w.GetPath(),r)
        text.SetValue(files.read())
        files.close()

file.Bind(EVT_MENU,open_file,opens)

def newfile(event):
    d = MessageDialog(None,"new file chahiye to yes kijiye")
    if d.ShowModal()==ID_OK:
        text.Clear()
    else:
        MessageBox("aapki marji")

file.Bind(EVT_MENU,newfile,new)

def save_dialog(event):
    wild = "text and doc file(*.txt;*.doc)|*.txt;*.docx|all files|*.*"
    win = FileDialog(None, "save kar dalo bhai g", "e://", "data.txt", wildcard=wild, style=FD_SAVE)
    if win.ShowModal() == ID_OK:
        data = text.GetValue()
        files = open(win.GetPath(),'w')
        files.write(data)
        files.close()
    else:
        MessageBox("Koi bat nhi")

file.Bind(EVT_MENU, save_dialog, save)



def close(envent):
    a = MessageDialog(None,"Kya band karna hai",style=YES_NO)
    if a.ShowModal()==ID_YES:
        f.Close()
    else:
        MessageBox("Thik hai")
f.Bind(EVT_MENU,close,exit)

def cont_word(event):
    foo = len( text.GetValue())
    status.SetStatusText("length="+str(foo))

text.Bind(EVT_TEXT,cont_word,text)


def zoomin(event):
    font = text.GetFont()
    font = font.GetPointSize()+1
    foo = Font(font,FONTFAMILY_DECORATIVE,FONTSTYLE_ITALIC,FONTWEIGHT_BOLD)
    text.SetFont(foo)

format.Bind(EVT_MENU,zoomin,zoom_in)


def zoomout(event):
    font = text.GetFont()
    fonts = font.GetPointSize()-1
    fo = Font(fonts,FONTFAMILY_DECORATIVE,FONTSTYLE_ITALIC,FONTWEIGHT_BOLD)
    text.SetFont(fo)

format.Bind(EVT_MENU,zoomout,zoom_out)


status = f.CreateStatusBar(3)

status.SetStatusText("niche wala dibba",1)




p.SetSizer(box)
f.SetMenuBar(mbar)
f.Show()
a.MainLoop()