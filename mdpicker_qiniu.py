# -*- coding: utf-8 -*-
# Author： firejq
# Created on 2017-09-17

import datetime
import hashlib
import os
import pyperclip
import qiniu

from configparser import ConfigParser
from mimetypes import MimeTypes
from PIL import ImageGrab


class ClipToQiniu(object):
    def __init__(self):
        """
        初始化操作类，获取配置文件信息
        """
        config = ConfigParser()
        config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'qiniu.ini'))
        self.__bucket_name = config.get('config', 'bucket')
        self.__access_key = config.get('config', 'accessKey')
        self.__secret_key = config.get('config', 'secretKey')
        self.__default_domain = 'http://' + \
            config.get('config', 'defaultDomain') + '/'

    def operate(self, file_path):
        """
        将临时图片文件上传到qiniu，并将外链复制到剪贴板
        :param file_path:
        :return:
        """
        # 生成远端存储别名
        remote_name = self.generate_remote_name(file_path)
        # 上传图片到 qiniu
        auth = qiniu.Auth(access_key=self.__access_key,
                          secret_key=self.__secret_key)
        token = auth.upload_token(bucket=self.__bucket_name, key=None)
        qiniu.put_file(up_token=token,
                       key=remote_name,
                       file_path=file_path,
                       mime_type=MimeTypes().guess_type(file_path)[0])

        # 整理 md 图片链接格式到剪贴板
        md_img_string = '![image](' + self.__default_domain + remote_name + ')'
        pyperclip.copy(md_img_string)
        pyperclip.paste()
        # print(md_img_string)

    @staticmethod
    def generate_remote_name(file_path):
        # 获取文件扩展名
        img_ext = file_path.split('.')[-1]
        # 计算文件 md5 值
        with open(file_path, 'rb') as fh:
            md5 = hashlib.md5(fh.read()).hexdigest()

        # remote name: filetype/year/month/day/md5.filetype
        now = datetime.datetime.now()
        remote_name = img_ext + '/' + str(now.year) + '/' + str(
            now.month) + '/' + str(now.day) + '/' + md5 + '.' + img_ext
        return remote_name

    @staticmethod
    def save_from_screen():
        """
        将剪贴板的图片保存到本地为临时图片文件
        :return:
        """
        pic = ImageGrab.grabclipboard()
        pic.save("tmp.jpg")

    @staticmethod
    def close():
        """
        删除保存在本地的临时图片文件
        :return:
        """
        os.remove("tmp.jpg")


if __name__ == '__main__':
    clip_to_qiniu = ClipToQiniu()
    clip_to_qiniu.save_from_screen()
    clip_to_qiniu.operate('tmp.jpg')
    clip_to_qiniu.close()
