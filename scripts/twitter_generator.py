'''
Use this file to grab twitter '@' handles off a page and turn them into links
'''

import pyperclip

text = pyperclip.paste()
lines = text.split('\r\n')
twitter_handles = []

for i in range(len(lines)):
    line_length = len(lines[i])
    if line_length < 1:
        lines[i] = ''
    else:
        lines[i] = str(lines[i]).strip()
        handle = lines[i].split("@")
        if len(handle) > 1:
            twitter_handles.append("https://twitter.com/" + handle[1])

msg = "\r\n".join(twitter_handles)
print(msg)
pyperclip.copy(msg)
