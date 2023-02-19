import numpy as np
from PIL import Image
from config import DefaultSetup

def crop_center(target: str, dim=DefaultSetup.CONST.IMG_DIM):
    img = Image.open(target)
    _w, _h = img.size
    _l = (_w - dim) // 2
    _t = (_h - dim) // 2
    _r = (_w + dim) // 2
    _b = (_h + dim) // 2
    return img.crop((_l, _t, _r, _b))

def crop_random(target: str, dim=DefaultSetup.CONST.IMG_DIM):
    img = Image.open(target)
    _w, _h = img.size
    crop_loc = [np.random.randint(0, _w - dim), np.random.randint(0, _h - dim)]
    return img.crop((crop_loc[0], crop_loc[1], crop_loc[0] + dim, crop_loc[1] + dim))
