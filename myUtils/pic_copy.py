import os
from random import sample

# 定义源文件夹路径和目标文件夹路径
source_folder = r'D:\buyongxi\ComparisonDetectorDataset\train\images'
target_folder = r'D:\fxj\projects\yolov7\yolov7\yolov7\inference\images'

# 获取源文件夹中所有图片文件名列表
image_files = [f for f in os.listdir(source_folder) if f.endswith('.bmp') or f.endswith('.png')]

# 如果没有符合条件的图片文件则提前结束程序
if len(image_files) == 0:
    print('未找到任何图片文件！')
else:
    # 随机选择100张图片并复制到目标文件夹
    selected_images = sample(image_files, k=100)

    for image in selected_images:
        source_path = os.path.join(source_folder, image)
        target_path = os.path.join(target_folder, image)

        try:
            # 创建目标文件夹（如果不存在）
            os.makedirs(target_folder, exist_ok=True)

            # 复制图片文件到目标文件夹
            with open(source_path, 'rb') as src, \
                    open(target_path, 'wb') as dest:
                dest.write(src.read())

            print(f"已将 {image} 复制至目标文件夹")
        except Exception as e:
            print(f"无法处理 {image}: {str(e)}")