import PySimpleGUI as sg

layout = [[sg.Text("Hola")], [], []]

window = sg.Window("Demo", layout, margins=(100, 100)).read()