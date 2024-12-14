from PIL import Image

img = Image.open("new.jpg")
red_channel,green_channel, blue_channel = img.split()



left = 50
top = 0
right = 600
bottom = 522
img1 = red_channel.crop((left, top, right, bottom))

left = 25
top = 0
right = 575
bottom = 522
img2 = red_channel.crop((left, top, right, bottom))
img_red = Image.blend(img1, img2, 0.5)



left = 0
top = 0
right = 550
bottom = 522
img1 = blue_channel.crop((left, top, right, bottom))

left = 25
top = 0
right = 575
bottom = 522
img2 = blue_channel.crop((left, top, right, bottom))
img_blue = Image.blend(img1, img2, 0.5)



left =25
top = 0
right = 575
bottom = 522
img_green = green_channel.crop((left, top, right, bottom))

new_image = Image.merge("RGB", (img_red, img_green, img_blue))
new_image.show()