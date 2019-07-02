## 使用方式

源码是toclipboard.py和tofile.py

使用pyinstaller -Fw toclipboard.py 和pyinstall -Fw tofile.py打包成了单个应用程序。打包在dist中

点击toclipboard.exe之前ctrl+c文件，得到文件的路径。然后复制了内容到粘贴板。可以把内容保存为文档形式在网页中。

复制保存在网页上的内容，运行tofile.exe 执行把剪贴板的内容，粘贴在tofile.exe同文件夹下的新的文件
 
## 发现问题

当复制的内容超过某一个限度，剪贴板的内容会卡住。就像复制一个东西一样，会卡住。
等于当复制的东西过大，有一个处理的时间，对于浏览器处理会出现崩溃。


