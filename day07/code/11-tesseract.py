import pytesseract
# 这个库调用tesseract软件

from PIL import Image
import random

from captcha.image import ImageCaptcha

imageCaptcha = ImageCaptcha()

chars = ['a','b','c','d','1','2','3','4','5','6','7','8','9','0','A','B','C','D']
for i in range(65,91):
    chars.append(chr(i))


# 列表['A',1,'a',5]
code = random.choices(chars,k = 4)

str = ''.join(code)


img = imageCaptcha.generate_image(str)

# img = Image.open('./english.png')

img.show()


result = pytesseract.image_to_string(img)


print(result)
