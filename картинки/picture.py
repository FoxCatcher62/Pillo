from PIL import Image

img = Image.open("new.jpg")
red_channel,green_channel, blue_channel = img.split()
red_channel.save("red_channel.jpg")
green_channel.save("green_channel.jpg") 
blue_channel.save("blue_channel.jpg")

img = Image.open("red_channel.jpg")
left = 50
top = 0
right = 600
bottom = 522
img1 = img.crop((left, top, right, bottom))

left = 25
top = 0
right = 575
bottom = 522
img2 = img.crop((left, top, right, bottom))

img_red = Image.blend(img1, img2, 0.5)





img = Image.open("blue_channel.jpg")
left = 0
top = 0
right = 550
bottom = 522
img1 = img.crop((left, top, right, bottom))

left = 25
top = 0
right = 575
bottom = 522
img2 = img.crop((left, top, right, bottom))

img_blue = Image.blend(img1, img2, 0.5)



img = Image.open("green_channel.jpg")
left =25
top = 0
right = 575
bottom = 522
img_green = img.crop((left, top, right, bottom))

new_image = Image.merge("RGB", (img_red, img_green, img_blue))
new_image.show()