import os


number = 300
target_list = [str(x) + ".txt" for x in range(1, number + 1)]

all_txt_path = "/home/ghy/GHY/CenterNet-1-bs/output_txt (另一个复件)"
input_list = os.listdir(all_txt_path)

for txt_name in target_list:
    if txt_name not in input_list:
        file_name = os.path.join(all_txt_path, txt_name)
        with open(file_name, 'w') as tmp_file:
            # tmp_file.write()
            pass
