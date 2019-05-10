#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    if len(lines[i]) <= 1:
        lines[i] = '' # remove all extra \n spaces
    else:
        lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = ' '.join(lines)
pyperclip.copy(text)
