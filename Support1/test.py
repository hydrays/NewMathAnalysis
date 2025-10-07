
#导入抠图依赖库
from PIL import Image
import rembg

if __name__=="__main__":
    #打开待抠图图片
    img = Image.open("in.png")
    #开始AI自动抠图
    img_bg_remove = rembg.remove(img)
    #保存抠图的图片
    img_bg_remove.save('out.png')