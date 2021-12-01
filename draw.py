import math
from PIL import Image

def main():
    image = Image.open("flower.jpg")
    #image.show()

    width, height = image.size
    print(width, height)
    size = 200 #100 fills the terminal, 50 is half
    modifier = width / size
    pixels = image.load()
    print("pixels: ", pixels)

    pixel_h = int(height / modifier)
    pixel_W = int(width / modifier)
    for x in range(pixel_h):
        pixel_x = x*modifier
        for y in range(pixel_W):
            pixel_y = y*modifier
            r,g,b = pixels[pixel_y, pixel_x]
            brightness = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
            complex_translate(brightness)
            #simple_translate(brightness)
        print('')

def simple_translate(brightness):
    #  .:-=+*#%@
    if brightness < 10:
        print("  ", end="")
    elif brightness < 30:
        print("` ", end="")
    elif brightness < 70:
        print("\" ", end="")
    elif brightness < 120:
        print("+ ", end="")
    elif brightness < 170:
        print("o ", end="")
    elif brightness < 220:
        print("% ", end="")
    else:
        print("@ ", end="")

def complex_translate(brightness):
    # $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.
    if brightness < 10:
        print("  ", end="")
    elif brightness < 15:
        print("` ", end="")    
    elif brightness < 20:
        print("\' ", end="")
    elif brightness < 40:
        print("- ", end="")
    elif brightness < 60:
        print("~ ", end="")
    elif brightness < 70:
        print("+ ", end="")
    elif brightness < 80:
        print("r ", end="")
    elif brightness < 100:
        print("t ", end="")
    elif brightness < 120:
        print("x ", end="")
    elif brightness < 140:
        print("C ", end="")   
    elif brightness < 160:
        print("X ", end="")
    elif brightness < 180:
        print("O ", end="")
    elif brightness < 200:
        print("0 ", end="")
    elif brightness < 220:
        print("# ", end="")
    elif brightness < 240:
        print("& ", end="")
    else:
        print("@ ", end="")

main()