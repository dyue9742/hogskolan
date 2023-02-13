import os
import multiprocessing as mp
from scipy.io import loadmat
from lib import DefaultSetup


train_dir = DefaultSetup.DIR.TRAIN_IMG
train_vox = DefaultSetup.DIR.TRAIN_VOX
test_dir  = DefaultSetup.DIR.TEST_IMG
val_dir   = DefaultSetup.DIR.VAL_IMG
dirs = [train_dir, test_dir, val_dir]


def walk_through(target: str):
    categories = []
    for (path, _, _) in os.walk(target, topdown=True):
        categories.append(path)
    print(f"{os.path.realpath(target)}\tcontains {len(categories)-1}\tcategories.")
    return categories[1:]


if __name__ == '__main__':
    mp.freeze_support()
    p = mp.Pool(mp.cpu_count())
    results = [p.map(walk_through, [_ for _ in dirs])]
    p.close()

    vox_files = []
    for (path, _, _) in os.walk(train_vox, topdown=True):
        vox_files.append(path)
    target = vox_files[1:][0]
    print(target)
    mat_content = loadmat(f"{os.path.realpath(target)}/model.mat", squeeze_me=True)
    print(mat_content['input'], mat_content['input'].shape)