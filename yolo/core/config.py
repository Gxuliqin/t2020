#! /usr/bin/env python
# coding=utf-8


from easydict import EasyDict as edict

__C = edict()
# Consumers can get config by: from config import cfg

cfg = __C

# YOLO options
__C.YOLO = edict()

# Set the class name
__C.YOLO.CLASSES = "yolo/data/classes/coco.names"
__C.YOLO.ANCHORS = "yolo/data/anchors/basline_anchors.txt"
__C.YOLO.MOVING_AVE_DECAY = 0.9995
__C.YOLO.STRIDES = [8, 16, 32]
__C.YOLO.ANCHOR_PER_SCALE = 3
__C.YOLO.IOU_LOSS_THRESH = 0.5
__C.YOLO.UPSAMPLE_METHOD = "resize"
__C.YOLO.ORIGINAL_WEIGHT = "yolo/checkpoint/yolov3_test_loss=102.3514.ckpt-29"
__C.YOLO.DEMO_WEIGHT = "yolo/checkpoint/yolov3_coco_demo.ckpt"

# Train options
__C.TRAIN = edict()

__C.TRAIN.ANNOT_PATH = "yolo/data/dataset/train.txt"
__C.TRAIN.BATCH_SIZE = 1
__C.TRAIN.INPUT_SIZE = [320, 352, 384, 416, 448, 480, 512, 544, 576, 608]
__C.TRAIN.DATA_AUG = True
__C.TRAIN.LEARN_RATE_INIT = 1e-4
__C.TRAIN.LEARN_RATE_END = 1e-6
__C.TRAIN.WARMUP_EPOCHS = 10
__C.TRAIN.FISRT_STAGE_EPOCHS = 100
__C.TRAIN.SECOND_STAGE_EPOCHS = 100
__C.TRAIN.INITIAL_WEIGHT = "yolo/checkpoint/yolov3_coco_demo.ckpt"

# TEST options
__C.TEST = edict()

__C.TEST.ANNOT_PATH = "yolo/data/dataset/voc_test.txt"
__C.TEST.BATCH_SIZE = 2
__C.TEST.INPUT_SIZE = 544
__C.TEST.DATA_AUG = False
__C.TEST.WRITE_IMAGE = True
__C.TEST.WRITE_IMAGE_PATH = "yolo/data/detection/"
__C.TEST.WRITE_IMAGE_SHOW_LABEL = False
__C.TEST.WEIGHT_FILE = "yolo/checkpoint/yolov3_test_loss=9.2099.ckpt-5"
__C.TEST.SHOW_LABEL = False
__C.TEST.SCORE_THRESHOLD = 0.3
__C.TEST.IOU_THRESHOLD = 0.45
