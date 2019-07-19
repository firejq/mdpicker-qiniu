# Markdown Picker To Qiniu

## Feature

- 使用 python + ahk 简化使用 markdown 写作时插入图片的繁琐流程

    - python 完成自动化：截图后将剪贴板中的图片上传至个人七牛云空间，并获取图片外链，输出到剪贴板中

    - AutoHotKey 快捷键部署：使用 ctrl+shift+v 执行 python 程序并输出剪贴板中的外链到屏幕

- 效果演示

    ![img](https://github.com/firejq/mdpicker-qiniu/blob/master/static/mdpicker-qiniu-presentation.gif)

- 自动为截图添加阴影

    在 qiniu.ini 中，保持默认配置 `shadow = 1` 即可自动对截图进行阴影处理，显示时效果更加友好。若不需要进行阴影处理，更改默认配置 `shadow = 0` 即可。
    

## Requirement

```powershell
pip install -r requirement.txt
```

## Usage

- Windows 10 (64 bit)

    1. 在 qiniu.ini 中，填写你的七牛账号信息：bucket、accessKey、secretKey、defaultDomain；

    1. 若未安装 AutoHotKey，则安装 [AutoHotKey](https://www.autohotkey.com/download/ahk-install.exe)；

    1. 将 mdpicker_qiniu.ahk 中的 mdpicker_qiniu.py 路径更改为你本地 mdpicker_qiniu.py 的绝对路径后保存；

    1. 运行 mdpicker_qiniu.ahk；

        若已有 .ahk 脚本在运行，则将 mdpicker_qiniu.ahk 中的内容添加到你的 .ahk 脚本中，reload 即可；

    1. 使用任意截图工具截图后，按下 Ctrl + shift + v，程序将剪贴板中的截图上传至七牛图床并将所得外链以 markdown 图片格式重组后输出到屏幕。

- MacOS Mojave 10.14

    1. 在 qiniu.ini 中，填写你的七牛账号信息：bucket、accessKey、secretKey、defaultDomain；
    
    1. 通过 Automator 新建 service，在左侧资源库中选择 run AppleScript，再将 ImgUploadToQiniu.wflow 中的 AppleScript （需要更改项目路径为你自己的路径）添加到代码框中后保存。最后，在系统设置-键盘-快捷键-服务-通用中找到刚刚保存的 service 设置快捷键（此处设置为 command + alt + v）即可。
    
    1. 使用任意截图工具截图后，按下 command + alt + v，程序将剪贴板中的截图上传至七牛图床并将所得外链以 markdown 图片格式重组后输出到剪贴板，得到操作完成的提示后 command + v 输出剪贴板内容即可。

## Similar Project
- https://github.com/ferstar/qiniu4blog
- https://github.com/jiwenxing/qiniu-image-tool-win

## License
The Markdown Picker To Qiniu is under the MIT License.
