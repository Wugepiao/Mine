import os
from PIL import Image
import shutil

# 设置源文件夹和目标文件夹路径
source_folder = 'C:\debug_image'
destination_folder = r'C:\Users\JM\Desktop\Test\Test_1\rgb'

# 创建目标文件夹（如果不存在）
os.makedirs(destination_folder, exist_ok=True)
def extract_and_copy_tif_files(source_folder, destination_folder):
    # 确保目标文件夹存在
    os.makedirs(destination_folder, exist_ok=True)

    i = 0
    #循环查看文件夹中每个文件
    for file_name in os.listdir(source_folder):
        #判断文件的名字是否以_7.tif结尾
        if file_name.endswith('_7.tif'):
            #将以_7.tif结尾的文件加入到tif_files中
            #tif_files.append(file_name)
            # 打开.tif文件并转换为.png格式
            # 构造完整的源文件路径
            i = i+1
            source_file = os.path.join(source_folder, file_name)

            with Image.open(source_file) as img:
                # 构造目标文件路径
                destination_file = os.path.join(destination_folder, file_name.replace('.tif', '.png'))
                # 将转换后的png文件存入目标文件夹
                img.save(destination_file, 'PNG')

    return i

def rename(timestamps, num, destination_folder):
    n=0
    for j in os.listdir(destination_folder):
        timestamp = timestamps[n]
        aa = os.path.join(destination_folder, str(j))
        bb = os.path.join(destination_folder, str(timestamp)+ ".png")
        print(aa, "/n", bb)

        os.rename(aa,bb)
        n += 1
                  # os.path.join(destination_folder, timestamp))


    # for i in range(num):
    #     timestamp = timestamps[i]
    #     print(os.path.join(destination_folder, os.listdir(source_folder)[i])) # 替换
    #     print(os.path.join(destination_folder, timestamp))
    #     # 重命名函数
    #     os.rename(os.path.join(destination_folder, os.listdir(source_folder)[i]), os.path.join(destination_folder, timestamp))
    #     print("重命名后的名字", os.path.join(destination_folder, timestamp))

if __name__ == '__main__':
    num = extract_and_copy_tif_files(source_folder, destination_folder)
    # 初始时间戳
    start_time = 1403636579763555584
    # 帧间隔时间（秒）
    interval = 50000000

    # 生成时间戳
    timestamps = [start_time + i * interval for i in range(num)]  # 生成425个时间戳

    rename(timestamps, num, destination_folder)
    # 将时间戳写入txt文件
    with open(r"C:\Users\JM\Desktop\Test\Test_1\timestamps.txt","w") as file:
        for ts in timestamps:
            file.write(f"{ts}\n")  # 每个时间戳写入一行

    print("时间戳已成功写入到 timestamps.txt 文件中。")
