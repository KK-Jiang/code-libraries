# -*- encoding: utf-8 -*-
import imageio
import cv2
import numpy as np
import os


def create_gif(source, name, duration):
    """
     生成gif的函数，原始图片仅支持png
     source: 为png图片列表（排好序）
     name ：生成的文件名称
     duration: 每张图片之间的时间间隔
    """
    frames = []  # 读入缓冲区
    for img in source:
        im = imageio.imread('/Users/kk_j/Desktop/plt/' + img + '.png')
        frames.append(im)
    imageio.mimsave(name, frames, 'GIF', duration=duration)
    print("处理完成")


def save_png():
    image_source = cv2.imdecode(np.fromfile('/Users/kk_j/Desktop/plt/90.png', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    image = cv2.resize(image_source, (503, 345))
    cv2.imencode('.png', image)[1].tofile('/Users/kk_j/Desktop/90.png')


if __name__ == '__main__':
    or_path = '/Users/kk_j/Desktop/plt/'
    # pic_list = os.listdir(or_path)
    pic_list = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    # pic_list = [4, 5, 6, 7, 8, 9, 90, 91, 91, 91, 92, 93, 94, 95, 96]
    pic_list = list(map(str, pic_list))
    gif_name = "result.gif"  # 生成gif文件的名称
    duration_time = 0.5
    # 生成gif
    create_gif(pic_list, gif_name, duration_time)
