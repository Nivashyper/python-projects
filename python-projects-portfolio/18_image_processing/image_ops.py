from PIL import Image

def grayscale(src, dst):
    Image.open(src).convert("L").save(dst)

def resize(src, dst, size=(256,256)):
    Image.open(src).resize(size).save(dst)

if __name__ == "__main__":
    print("Use grayscale('in.jpg', 'out.jpg') etc.")
