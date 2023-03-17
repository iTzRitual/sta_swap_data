import os
import tkinter as tk
from tkinter import messagebox

def main():

    root = tk.Tk()
    root.withdraw()

    root.silence_deprecation = True

    if not os.path.exists('changed'):
        os.makedirs('changed')

    if not os.path.exists('to_change'):
        os.makedirs('to_change')

    to_change = os.listdir('to_change')
    changed = os.listdir('changed')

    isDoneAnything = False

    for file in to_change:
        if file.endswith('.STA'):
            with open(os.path.join('to_change', file), 'r', encoding='Windows-1250') as f:
                arrayForPeople = []
                personData = []

                for index, line in enumerate(f):
                    if line.startswith(':61'):
                        arrayForPeople.append(personData)
                        personData = []
                    personData.append(line)

            for person in arrayForPeople:
                data38 = ''
                data24 = ''
                for line in person:
                    if line.startswith('<38'):
                        data38 = line[3:]
                    elif line.startswith('<24'):
                        data24 = line[3:]

                if data38 != '' and data24 != '':
                    temp = data38
                    data38 = data24
                    data24 = temp

                    for index, line in enumerate(person):
                        if line.startswith('<38'):
                            person[index] = '<38' + data38
                        elif line.startswith('<24'):
                            person[index] = '<24' + data24

            if os.path.isfile(os.path.join('changed', file)):
                i = 1
                while os.path.isfile(os.path.join('changed', f"{i}_{file}")):
                    i += 1
                file = f"{i}_{file}"

            with open(os.path.join('changed', file), 'w', encoding='Windows-1250') as f:
                for person in arrayForPeople:
                    for line in person:
                        f.write(line)

        isDoneAnything = True

    if isDoneAnything:
        messagebox.showinfo("Success", "Done")
    else:
        messagebox.showinfo("Error", "Put .STA files in to_change folder")

if __name__ == "__main__":
    main()