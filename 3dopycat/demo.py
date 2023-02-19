import os
import multiprocessing as mp
from scipy.io import loadmat
from lib import DefaultSetup


train_dir = DefaultSetup.DIR.TRAIN_IMG
train_vox = DefaultSetup.DIR.TRAIN_VOX
test_dir  = DefaultSetup.DIR.TEST_IMG
test_vox  = DefaultSetup.DIR.TEST_VOX
val_dir   = DefaultSetup.DIR.VAL_IMG
val_vox   = DefaultSetup.DIR.VAL_VOX

dirs = [train_dir, test_dir, val_dir]


def walk_through(target: str):
    categories = []
    for (path, _, _) in os.walk(target, topdown=True):
        categories.append(path)
    print(f"{os.path.realpath(target)}\tcontains {len(categories)-1}\tcategories.")
    return categories[1:]

def sampling(target: str, to: str):
    files = walk_through(target)
    if to == 'vox':
        mat_content = loadmat(f"{os.path.realpath(files[0])}/model.mat", squeeze_me=True)
        print(mat_content['input'], mat_content['input'].shape)
    elif to == 'img':
        from PIL import Image
        import numpy as np
        img_content = Image.open(f"{os.path.realpath(files[0])}/000.png")
        img = np.asarray(img_content)
        print(img, img.shape)
    else:
        raise NotImplementedError()

if __name__ == '__main__':
    mp.freeze_support()
    p = mp.Pool(mp.cpu_count())
    results = [p.map(walk_through, [_ for _ in dirs])]
    p.close()

    # sampling(train_vox, 'vox')
    # sampling(train_dir, 'img')
