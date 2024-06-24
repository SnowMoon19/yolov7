import os
import shutil

path = r'D:\fxj\data\yolo3\train\images'
label_path = r'D:\fxj\data\yolo3\train\labels'

new_path = r'D:/fxj/data/yolo3/test/images/'
new_label_path = r'D:/fxj/data/yolo3/test/labels/'

def mymovefile(srcfile,dstpath):                       # 移动函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.move(srcfile, dstpath + fname)          # 移动文件
        print ("move %s -> %s"%(srcfile, dstpath + fname))

def mycopyfile(srcfile,dstpath):                       # 复制函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        print ("copy %s -> %s"%(srcfile, dstpath + fname))

my = r'D:\fxj\data\test.txt'
li = []
with open(my, 'r') as file:
    lines = file.readlines()
    for line in lines:
        li.append(line[:-1])
cnt = 0
for file in os.listdir(label_path):
    tmp = file[:-4]
    if tmp in li:
    # if cnt % 3 == 0:
        cnt += 1
        name = file[:-4]
        origin_label = label_path + "\\" + name + ".txt"
        aim_label_directory = new_label_path
        mymovefile(origin_label, aim_label_directory)
        origin_pic = path + "\\" + name + ".bmp"
        aim_pic_directory = new_path
        mymovefile(origin_pic, aim_pic_directory)

print(cnt)
# my = r'D:\fxj\data\test.txt'
# li = []
# with open(my, 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         li.append(line[:-1])
#
# print(len(li))
# pth = r'D:/fxj/data/yolo/yolov7-c3hb-4-cot-multi1/val/'
# cnt = 0
# tt = 0
# sd = 0
# total = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}
# for file in os.listdir(pth):
#     tmp = file[:-4]
#     # print(tmp)
#     if tmp in li:
#         print(tmp)
#     # if cnt % 8 == 0:
#         sd += 1
#         filename = pth + file
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#         for line in lines:
#             line = line.strip()
#             idx = line[0]
#             if line[0] == '1':
#                 if line[1] == '0':
#                     idx = '10'
#             total[idx] += 1
#         num_of_lines = len(lines)
#         tt += num_of_lines
#     # if cnt == 741 * 8: break
# print(sd)
# print(tt)
# print(total)

