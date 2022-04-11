from PIL import Image
import PIL
frames=24

im_start=Image.open('1.jpg')
im_end=Image.open('2.jpg')
px_s=im_start.convert('RGB')
px_e=im_end.convert('RGB')
l, h=im_start.size
im_proces=Image.open('1.jpg')
pisels_proces=im_proces.load()
Matrix = [[[] for x in range(h)] for y in range(l)]
for x in range(l):
    for y in range(h):
        r1, g1, b1 = px_s.getpixel((x,y))
        r2, g2, b2 = px_e.getpixel((x, y))
        Matrix[x][y]=[(r2-r1)/frames, (g2-g1)/frames, (b2-b1)/frames]
pixels_now = im_proces.convert('RGB')
for frame in range(frames):
    for x in range(l):
        for y in range(h):
            r, g, b = pixels_now.getpixel((x, y))
            #print(r,g,b)
            pisels_proces[x,y]=(r+int(Matrix[x][y][0]*(frame+1)), g+int(Matrix[x][y][1]*(frame+1)), b+int(Matrix[x][y][2]*(frame+1)))
    im_proces.save('frames\\'+str(frame+1)+'.ppm')


