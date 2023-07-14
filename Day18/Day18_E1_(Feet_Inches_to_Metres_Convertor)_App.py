import PySimpleGUI as sg
import Feet_Inches_to_Metres_Function
sg.theme("Black")

label1 = sg.Text("Enter Feet: ")
input_box1 = sg.InputText(tooltip="Type Feet to convert", key="feet")

label2 = sg.Text("Enter Inches: ")
input_box2 = sg.InputText(tooltip="Type Inches to convert", key="inches")

convert_button = sg.Button("Convert to Meters")
exit_button = sg.Button("Exit")
message = sg.Text(key="output")

window = sg.Window("Convertor", layout=[[label1, input_box1],
                                        [label2, input_box2],
                                        [convert_button, exit_button, message]])
while True:
    events, values = window.read()
    match events:
        case "Convert to Meters":
            try:
                feet = float(values["feet"])
                inches = float(values["inches"])
                output = Feet_Inches_to_Metres_Function.convert(feet, inches)
                window["output"].update(output)
            except ValueError:
                sg.popup("Type inches.")

        case "Exit":
            break

window.close()

