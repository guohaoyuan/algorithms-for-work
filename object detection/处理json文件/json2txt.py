"""
json文件处理
https://www.cnblogs.com/bigberg/p/6430095.html

"""
import json

images_path = []
with open("/home/ghy/GHY/CenterNet-1-bs/data/coco/annotations/instances_test2017.json", 'r') as file:
    load_dict = json.load(file)
    # print(load_dict)
    images = load_dict["images"]
    # print(images)
    for i in range(len(images)):
        image = images[i]['file_name']
        images_path.append(image)

new_test_path = "/home/ghy/GHY/CenterNet-1-bs/data/coco/images/testimages"
old_test_path = "/home/ghy/GHY/CenterNet-1-bs/data/coco/images/test2017"

import shutil
import os

for path in images_path:
    new_test_image_path = os.path.join(new_test_path, path)
    old_test_image_path = os.path.join(old_test_path, path)
    shutil.move(old_test_image_path, new_test_image_path)
print("finished!")