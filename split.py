import os, random, shutil



def moveFile(Dir, train_ratio = 0.8, val_ratio = 0.2, new_dir = r'G:\DLDate\Enhancementdatas\41Dataset'):




    filenames = []

    for root, dirs, files in os.walk(Dir):      # os.walk(): 返回值：函数返回一个元组，含有三个元素。这三个元素分别是：每次遍历的路径名、路径下子目录列表、目录下文件列表。
        for name in files:
            filenames.append(name)
        break

    filenum = len(filenames)

    num_train = int(filenum * train_ratio)
    sample_train = random.sample(filenames, num_train)      # random.sample()：从list样本或集合中随机抽取K个不重复的元素形成新的序列

    Dirlist = Dir.split("\\")
    Houzhui = Dirlist[3] + "/" + Dirlist[4]



    for name in sample_train:
        if not os.path.exists(os.path.join(new_dir, Houzhui)):
            os.makedirs(os.path.join(new_dir, Houzhui))
        shutil.move(os.path.join(Dir, name), os.path.join(new_dir, Houzhui))        # shutil.move 将从一个文件夹里筛选出来的文件信息，移动到新的文件夹中

    sample_val = list(set(filenames).difference(set(sample_train)))

    for name in sample_val:
        if not os.path.exists(os.path.join(new_dir, 'val/'+Dirlist[4])):
            os.makedirs(os.path.join(new_dir, 'val/'+Dirlist[4]))
        shutil.move(os.path.join(Dir, name), os.path.join(new_dir, 'val/'+Dirlist[4]))

if __name__ == '__main__':
    dir = r'G:\DLDate\Enhancementdatas\train'


    for root, dirs, files in os.walk(dir):
        for name in dirs:
            folder = os.path.join(root, name)
            print(folder)
            moveFile(folder)
