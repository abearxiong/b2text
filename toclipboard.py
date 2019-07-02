# coding:utf-8
import win32clipboard as w
import win32con
import time


def get_file():
    try:
        w.OpenClipboard()
        _file_name = w.GetClipboardData(win32con.CF_HDROP)  # CF_HDROP
        w.CloseClipboard()
    except:
        return None
    return _file_name[0]


def set_text(v):
    # print("内容", v)
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(v)
    w.CloseClipboard()


filename = get_file()  # 获取文件的路径
if filename is None:
    print("复制错误,必须复制文件类型的")
    time.sleep(2)
else:
    print("文件名", filename)
    name = filename.split("\\")[-1]  # 得到文件的名字
    # name = name.encode(encoding="utf-8")
    fen_ge_fu = "<fen_ge_fu>"
    # print(name)
    with open(filename, "rb") as r:
        bytes_content = r.read()
        con = bytes_content.hex()
        r.close()
        value = name+fen_ge_fu+con  # 得到输出的内容
        # print(value)
        set_text(value)
    # a,b= value.split(fen_ge_fu)
    # print(a,b)
    # f = open(a, "wb")
    # f.write(bytes.fromhex(b))
    # f.close()
