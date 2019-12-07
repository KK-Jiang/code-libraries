# -*- encoding: utf-8 -*-
import imageio
import cv2
import numpy as np
import os


def create_gif(base_path, source, name, duration):
    """
     生成gif的函数
     source: 为png图片列表（排好序）
     name ：生成的文件名称
     duration: 每张图片之间的时间间隔
    """
    pic_frames = []  # 读入缓冲区
    for img_num in source:
        img_array = imageio.imread(base_path + img_num + '.png')
        pic_frames.append(img_array)
    imageio.mimsave(name, pic_frames, 'GIF', duration=duration)
    print("处理完成")


def save_png(pic_path, save_path):
    image_source = cv2.imdecode(np.fromfile(pic_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    image = cv2.resize(image_source, (503, 345))
    cv2.imencode('.png', image)[1].tofile(save_path)


if __name__ == '__main__':
    or_path = '/Users/kk_j/Desktop/plt/'
    picture_path = '/Users/kk_j/Desktop/plt/90.png'
    base_path = '/Users/kk_j/Desktop/plt/'

    # 想在一张上停留久一点，他的序号就多写几个
    pic_num = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    pic_num = list(map(str, pic_num))
    gif_name = "result.gif"  # 生成gif文件的名称

    # 每张图片的时间间隔（s）
    duration_time = 0.5
    # 生成gif
    create_gif(base_path, pic_num, gif_name, duration_time)
