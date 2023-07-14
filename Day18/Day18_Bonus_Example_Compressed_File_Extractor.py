import PySimpleGUI as sg
from zip_extractor import extract_archive


label1 = sg.Text("Select archive: ")
input_box1 = sg.InputText()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination folder: ")
input_box2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")

message = sg.Text(key='output', text_color='green')

window = sg.Window("Archive Extractor", layout=[[label1, input_box1, choose_button1],
                                              [label2, input_box2, choose_button2],
                                              [extract_button, message]])

while True:
    event, values = window.read()
    archive_path = values["archive"]
    dest_folder = values["folder"]
    extract_archive(archive_path, dest_folder)
    window["output"].update(value="Extraction Completed!")


window.close()
