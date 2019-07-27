import sys
import os

from PIL import Image


thumb_size = 200,200

def main(indir, outdir):

    totalSize = 0
    files = os.listdir(indir)
    files.sort()
    for filename in files:
        if filename.endswith(".jpg"):
            inpath = indir + "/" + filename

            img = Image.open(inpath)
            width, height = img.size
            filesize =str(len(img.fp.read())/1000000)

            print("Image:", filename, " -- ", width,"x",height, " -- ", filesize, "MB")

            if width > height:
                diff = (width - height) / 2
                img = img.crop((diff, 0, width - diff, height))
            elif height > width:
                diff = (height - width) / 2
                img = img.crop((0, diff, width, height-diff))

            img = img.resize(thumb_size, Image.ANTIALIAS)

            path = outdir + "/" + filename
            img.save(path, format="JPEG",quality=40)

            totalSize += os.path.getsize(path)

    print("Total size of images: ", totalSize/1000000, "MB")



if __name__=="__main__":
    main(sys.argv[1], sys.argv[2])
