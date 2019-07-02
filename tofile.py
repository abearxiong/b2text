# coding:utf-8
import win32clipboard as w
import win32con
import time


def get_file():
    w.OpenClipboard()
    _content = w.GetClipboardData(win32con.CF_TEXT)  # 获取剪贴板的文本内容
    w.CloseClipboard()
    return _content


value = get_file().decode("utf-8")
# print(type(value))
# print(value)
fen_ge_fu = "<fen_ge_fu>"
a,b= value.split(fen_ge_fu)
if a is None or b is None:
    pass
else:
    f = open(a, "wb")
    f.write(bytes.fromhex(b))
    f.close()
