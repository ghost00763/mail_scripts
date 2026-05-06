from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()

left_crop = 50
image = red
coordinates = (left_crop,0, image.width, image.height)
red1 = image.crop(coordinates)

left_crop = 25
ride_crop = 25
image = red
coordinates = (left_crop, 0,image.width-ride_crop, image.height)
red2 = image.crop(coordinates)

image1 = red1
image2 = red2
red3 = Image.blend(image1, image2, 0.5)

ride_crop = 50
image = blue
coordinates = (0,0, image.width-ride_crop, image.height)
blue1 = image.crop(coordinates)

left_crop = 25
ride_crop = 25
image = blue
coordinates = (left_crop, 0,image.width-ride_crop, image.height)
blue2 = image.crop(coordinates)

image1 = blue1
image2 = blue2
blue3 = Image.blend(image1, image2,0.5)

image = green
coordinates = (25,0, image.width-25,image.height)
green3 = image.crop(coordinates)

r = red3
b= blue3
g= green3
new_image = Image.merge("RGB",(r,g,b))
new_image.save("Monro_merge.jpg")

image = Image.open("Monro_merge.jpg")
image.thumbnail((80,80))
image.save("avatar.jpg")