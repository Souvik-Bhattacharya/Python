import cv2

from PIL import Image
'''
img=Image.open("./static/image.png")
img.show()
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save("./static/corrected.png")
I=Image.open("./static/corrected.png")
I.show()
print('done')
'''
i=cv2.imread("./static/image.png")
clahe=cv2.createCLAHE()
gray_img=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
enh_img=clahe.apply(gray_img)
cv2.imwrite("./static/enhanced.png",enh_img)
IM=Image.open("./static/enhanced.png")
IM.show()
print('done')
