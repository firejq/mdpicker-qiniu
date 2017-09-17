# Markdown Picker To Qiniu #

## Feature ##

- 使用 python + ahk 简化使用 markdown 写作时插入图片的繁琐流程

    - python 完成自动化：截图后将剪贴板中的图片上传至个人七牛云空间，并获取图片外链，输出到剪贴板中

    - AutoHotKey 快捷键部署：使用 ctrl+shift+v 执行 python 程序并输出剪贴板中的外链到屏幕

- 效果演示

![img](https://github.com/firejq/mdpicker-qiniu/blob/master/static/mdpicker-qiniu-presentation.gif)

## Requirement ##
- Python 3.6
```powershell
pip install -r requirement.txt
```
- Windows 10 (64 bit)

其它环境未测试

## Usage ##

1. 在 qiniu.ini 中，填写你的七牛账号信息：bucket、accessKey、secretKey、defaultDomain；

1. 若未安装 AutoHotKey，则安装 [AutoHotKey](https://www.autohotkey.com/download/ahk-install.exe)；

2. 将 mdpicker_qiniu.ahk 中的 mdpicker_qiniu.py 路径更改为你本地 mdpicker_qiniu.py 的绝对路径后保存；

2. 运行 mdpicker_qiniu.ahk；
   
    若已有 .ahk 脚本在运行，则将 mdpicker_qiniu.ahk 中的内容添加到你的 .ahk 脚本中，reload 即可；

3. 使用任意截图工具截图后，按下 Ctrl + shift + v，程序将剪贴板中的截图上传至七牛图床并将所得外链以 markdown 图片格式重组后输出到屏幕。


## Similar Project ##
https://github.com/ferstar/qiniu4blog
https://github.com/jiwenxing/qiniu-image-tool-win


## License ##
The Markdown Picker To Qiniu is under the MIT License.