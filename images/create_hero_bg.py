from PIL import Image, ImageDraw

# Hero 1 - Green field gradient
img = Image.new('RGB', (1600, 900))
draw = ImageDraw.Draw(img)
for y in range(900):
    t = y / 900
    r = int(27 + (100 - 27) * t)
    g = int(77 + (180 - 77) * t)
    b = int(50 + (120 - 50) * t)
    draw.line([(0, y), (1600, y)], fill=(r, g, b))
img.save("C:/Users/kingo/trimurti-redesign/images/hero/hero-1.jpg", quality=85)
print("Hero 1 created")

# Hero 2 - Warm gold
img2 = Image.new('RGB', (1600, 900))
draw2 = ImageDraw.Draw(img2)
for y in range(900):
    t = y / 900
    r = int(139 + (210 - 139) * t)
    g = int(105 + (170 - 105) * t)
    b = int(20 + (80 - 20) * t)
    draw2.line([(0, y), (1600, y)], fill=(r, g, b))
img2.save("C:/Users/kingo/trimurti-redesign/images/hero/hero-2.jpg", quality=85)
print("Hero 2 created")

# Hero 3 - Deep green
img3 = Image.new('RGB', (1600, 900))
draw3 = ImageDraw.Draw(img3)
for y in range(900):
    t = y / 900
    r = int(15 + (60 - 15) * t)
    g = int(50 + (140 - 50) * t)
    b = int(30 + (80 - 30) * t)
    draw3.line([(0, y), (1600, y)], fill=(r, g, b))
img3.save("C:/Users/kingo/trimurti-redesign/images/hero/hero-3.jpg", quality=85)
print("Hero 3 created")

print("All done!")
