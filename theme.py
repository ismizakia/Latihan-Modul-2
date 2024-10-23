import PySimpleGUI as sg
sg.theme("DarkPurple")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile", 
                   layout=[[sg.Text("SELAMAT DATANG DIKELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                           [sg.Text("NPM   : 2210010020 ")],
                           [sg.Text("Nama  : ISMI ZAKIA ")],
                           [sg.Text("Kelas : 5B Non Reguler Banjarmaasin ")]
                           ],
                    size=(510,200),
                    font=("Times", 18))
window()
window.close()