import PySimpleGUI as sg
window = sg.Window(title="Profile", 
                   layout=[[sg.Text("NPM    : 2210010020")],
                           [sg.Text("Nama   : ISMI ZAKIA")],
                           [sg.Text("Kelas  : 5B Non Reguler Banjarmasin")],
                           [sg.Text("Matkul : Pemrograman Visual 3")],
                           ],
                           size=(400,200))
window()
window.close()