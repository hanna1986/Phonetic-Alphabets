import tkinter as tk
import yaml
import os
from alphabet import Alphabet
#from alphabet_dict import Alphabet_dict

root = tk.Tk()

root.geometry("500x500")
root.title("Phonetic Alphabets")

# Creating empty rows and columns on the form
space_label1 = tk.Label(root, text="       ").grid(row=0, column=0)
space_label2 = tk.Label(root, text="       ").grid(row=11, column=10)
space_label3 = tk.Label(root, text="       ").grid(row=6, column=1)
space_label4 = tk.Label(root, text="                 ").grid(row=1, column=5)
space_label5 = tk.Label(root, text="                 ").grid(row=1, column=6)
space_label6 = tk.Label(root, text="                 ").grid(row=1, column=7)


# Creating input label and textbox. This texbox is used to input a name, flight number, etc to be converted
label_input = tk.Label(root, text="Input text here")
label_input.grid(row=1, column=1, columnspan=4)

textbox_input = tk.Text(root, height=10, width=20)
textbox_input.grid(row=2, column=1, rowspan=3, columnspan=4)

# Creating output label and textbox
label_output = tk.Label(root, text="Output")
label_output.grid(row=7, column=1, columnspan=4)

textbox_output = tk.Text(root, height=10, width=20)
textbox_output.grid(row=8, column=1, columnspan=4)

# Creating "Spell" button
button_spell = tk.Button(root, text = "Spell", command=lambda:spell())
button_spell.grid(row=5, column=4)

# Creating "American" button
button_american = tk.Button(root, text = "American")
button_american.grid(row=3, column=8, columnspan=2)

# Creating the dropdown (Option Menu) menu
directory_path = './Alphabet Dictionaries'
alphabets = Alphabet.get_yaml_files(directory_path)
selected_alphabet = tk.StringVar(value=alphabets[0])
drop = tk.OptionMenu(root, selected_alphabet,  *alphabets).grid(row=2, column=8, columnspan=2)

 
def spell():

    #try:
        name = textbox_input.get("1.0", "end-1c")
        with open("Alphabet Dictionaries/" + selected_alphabet.get() + ".yaml", "r") as f:dictionary = yaml.safe_load(f)
        f.close()
        output = Alphabet.convert(name, dictionary['mydict'])
        textbox_output.delete("1.0", "end")
        textbox_output.insert("1.0", output)
    #except TypeError:
     #   print("Enter only alpha-numeric english characters, please!")

root.mainloop()



