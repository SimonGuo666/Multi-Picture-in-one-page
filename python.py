import os

def list_filenames(directory, output_file=None):
    try:
        filenames = os.listdir(directory)
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as file:
                for name in filenames:
                    file.write('\'' +'./output/' + name +'\''+ ',' +'\n')
            print(f"File names have been saved to {output_file}")
        else:
            for name in filenames:
                print(name)
    except Exception as e:
        print(f"An error occurred: {e}")

# 修改为你的图片目录路径
directory = "./"  
output_file = "filenames.txt"  # 设置为 None 则只打印

list_filenames(directory, output_file)
