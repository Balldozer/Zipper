import FreeSimpleGUI as sg
from zip_creator import make_archives

label1 = sg.Text("Select files to compress:")
label2 = sg.Text("Select a destination folder:")
input1 = sg.Input(key="input1")
input2 = sg.Input(key="input2")
choose_button1 = sg.FilesBrowse("Choose", key="files")
choose_button2 = sg.FolderBrowse("Choose", key="folder")
zip_button1 = sg.Button("Zip files")
output_label = sg.Text("", key="output")

window = sg.Window("File Zipper",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [zip_button1, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    print(filepaths)
    print(folder)
    make_archives(filepaths, folder)
    window["output"].update(value="Compression completed.")
    window["input1"].update(value="")
    window["input2"].update(value="")

    if sg.WINDOW_CLOSED:
        break

window.close()