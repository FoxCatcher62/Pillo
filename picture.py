from PIL import Image

# img = Image.open("red_channel.jpg")
# left = 70
# top = 0
# right = 600
# bottom = 522
# cropped = img.crop((left, top, right, bottom))
# cropped.save('left1.jpg')
# img_left = Image.open("left1.jpg")

# left = 35
# top = 0
# right = 565
# bottom = 522
# cropped = img.crop((left, top, right, bottom))
# cropped.save('mid.jpg')
# img_mid = Image.open("mid.jpg")
# r = Image.open('mid.jpg')
# r.show()

# img = Image.blend(img_left, img_mid, 0.5)
# img.save("monro1.jpg")
# img = Image.open("monro1.jpg")
# img.show()



img = Image.open("blue_channel.jpg")
left = 0
top = 0
right = 670
bottom = 522
cropped = img.crop((left, top, right, bottom))
cropped.save('right1.jpg')
img_right = Image.open("right1.jpg")
img_right.show()



left = 35
top = 0
right = 635
bottom = 522
cropped = img.crop((left, top, right, bottom))
cropped.save('mid2.jpg')
img_mid = Image.open("mid2.jpg")
img_mid.show()

img = Image.blend(img_right, img_mid, 0.5)
img.save("monro2.jpg")
img = Image.open("monro2.jpg")
img.show()