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


if __name__ == "__main__":
    from PIL import Image

    # import numpy as np
    #
    # w, h = 512, 512
    # data = np.zeros((h, w, 3), dtype=np.uint8)
    # data[0:256, 0:256] = [255, 0, 0]  # red patch in upper left

    data = base64_to_np(
        "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")
    # img = Image.fromarray(cv2.cvtColor(data,cv2.COLOR_BGR2RGB))
    # img.save('my.png')

    img = Image.fromarray(cv2.cvtColor(data,cv2.COLOR_BGR2RGB)).convert("L")
    base64_str = img_to_base64(img)
    print(base64_str)
    img.show()
