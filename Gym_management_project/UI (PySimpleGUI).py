import PySimpleGUI as pui


layout=[
    [sg.Text("Fitness Centre Management System")]
    [sg.Text("Enter Credential")]
    [sg.Input]
    [sg.Button("Login")]
]
sq.Window('converter',layout).read()
