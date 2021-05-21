import win32clipboard as w
import win32con
import re


def get_text():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d.decode('GBK')


text = get_text().strip()
if text != '':
    pass
else:
    print("Error:no input")
    exit(0)
text2 = re.findall("\d{2,}", text)

for i in text2:
    print(chr(int(i)), end="")
