import os
import multiprocessing
os.chdir("D://python学习")


def copy_file(file_name,folder_name, q):
    # print("%s %s %s" % (file_name, folder_name, folder_name+"复件"))
    file = open(folder_name+"/"+file_name, "rb")
    content = file.read()
    file.close()
    new_file = open(folder_name+"复件/"+file_name, "wb")
    new_file.write(content)
    new_file.close()
    q.put(file_name)


def main():
    q = multiprocessing.Manager().Queue()
    # 获取文件夹名字
    folder_name = input("输入文件名")
    # 创建一个文件夹
    try:
        os.mkdir(folder_name+"复件")
    except:
        pass
    # 读取文件夹下文件
    po = multiprocessing.Pool(5)
    file_names = os.listdir(folder_name)
    for file_name in file_names:
        po.apply_async(copy_file, (file_name, folder_name, q))
    po.close()
    # po.join()
    file_num = len(file_names)
    num1 = 0
    while True:
        file_name = q.get()
        print("\r已经完成%.8f %%" % ((num1+1)*100/file_num), end="")
        num1 += 1
        if num1 >= file_num:
            break

if __name__ == '__main__':
    main()
