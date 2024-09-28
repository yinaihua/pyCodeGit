from torch.utils.data import Dataset
import os
from PIL import Image

class Mydata(Dataset):     #定义一个数据类
    def __init__(self,root_dir,label_dir):   #文件地址，label地址
        self.root_dir=root_dir
        self.label_dir=label_dir
        self.path=os.path.join(self.root_dir,self.label_dir)   #图片路径
        self.img_path=os.listdir(self.path)              #图片列表化


    def __getitem__(self, idx):       #索引取照片    idx原为item
        img_name=self.img_path[idx]          #从图片列表中获取每一张的名字
        img_item_path=os.path.join(self.root_dir,self.label_dir,img_name) #获取每一张图片的地址
        img=Image.open(img_item_path)    #获取该图片
        label=self.label_dir
        return img,label


    def __len__(self):
        return len(self.img_path)


root_dir="test/train"
ants_label_dir="ants"
bees_label_dir="bees"
ants_dataset=Mydata(root_dir,ants_label_dir)
bees_dataset=Mydata(root_dir,bees_label_dir)

train_dataset=ants_dataset+bees_dataset
img,label=bees_dataset[0]
img.show()
''' 
文件结构
test 
    |_train
            |_ants   ，里面存放很多图片
            |_bees
    |_本文件
'''