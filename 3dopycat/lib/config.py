from easydict import EasyDict

__C = EasyDict()
DefaultSetup = __C

__C.DIR = EasyDict()
__C.DIR.TRAIN_IMG = "/Users/george/Data/train_images"
__C.DIR.TRAIN_VOX = "/Users/george/Data/train_voxels"
__C.DIR.TEST_IMG  = "/Users/george/Data/test_images"
__C.DIR.TEST_VOX  = "/Users/george/Data/test_voxels"
__C.DIR.VAL_IMG   = "/Users/george/Data/val_images"
__C.DIR.VAL_VOX   = "/Users/george/Data/val_voxels"

__C.CONST = EasyDict()
__C.CONST.IMG_W = 150
__C.CONST.IMG_H = 150
__C.CONST.IMG_DIM = 150
__C.CONST.BATCH_SIZE = 32

__C.TRAIN = EasyDict()
__C.TRAIN.LEARNING_RATES = {'0': 1e-4, '1': 1e-5, '2': 1e-6}
__C.TRAIN.CONV2D_FILTERS = [96, 128, 256, 256, 256]
__C.TRAIN.LIMIT_ITERATIONS = 50000
__C.TRAIN.WEIGHT_DECAY = 0.00005
__C.TRAIN.MOMENTUM = 0.90
__C.TRAIN.RANDOM_CROP = True
