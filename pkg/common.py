import configparser
from PIL import Image
import base64
import io
import numpy as np
import cv2


def read_conf(path: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(path)
    return config


def save_base64(img_str: str, out_file: str, resize: bool = False) -> None:
    image = base64.b64decode(img_str)
    imagePath = (out_file)

    byteImgIO = io.BytesIO(image)
    byteImgIO.seek(0)
    img = Image.open(byteImgIO)

    if resize:
        (w, h) = img.size
        img = img.resize((int(w / 5), int(h / 5)))
    img.save(imagePath, 'jpeg')


def img_to_base64(img: Image) -> str:
    output_buffer = io.BytesIO()
    img.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_content = base64.b64encode(byte_data)
    return base64_content


def base64_to_np(img: str) -> np.array:
    img_data = base64.b64decode(img)
    np_arr = np.fromstring(img_data, np.uint8)
    img_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    return img_np


