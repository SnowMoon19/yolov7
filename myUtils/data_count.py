# 获取文件夹中的文件列表
import json
import os
file = r'D:\fxj\data\yolo\train\train.json'


with open(file, "r", encoding="utf-8") as f:
    content = json.load(f)
    annotations = content['annotations']
    dict = {}
    for i in range(0, 12):
        dict[str(i)] = 0
    for j in annotations:
        id = str(j['category_id'])

        dict[str(id)] += 1

    for c in dict:
        print(c, dict[c])


# 统计标签大小和宽高比
with open(file, "r", encoding="utf-8") as f:
    content = json.load(f)
    annotations = content['annotations']
    dict = {}
    areas = {}


    for j in annotations:
        id = str(j['category_id'])
        # bbox = j['bbox']
        # if len(bbox) != 4: print(j['image_id'])
        # print(dict)
        dict[str(id)] += 1

    for c in dict:
        print(c, dict[c])