from PIL import Image
im=Image.open('/home/user/Pictures/tim.jpeg')
im1=im.resize((100,100)).convert('L')
w,h=im1.size
print w,h
txt=''

for i in range(w):
    for j in range(h):
        li = im1.getpixel((i, j))
        if li == 0:
            txt+=' '
        elif li<=100:
            txt+='.'
        elif 100<li<150:
            txt+='@'
        elif 150<=li<200:
            txt+='%'
        elif li>=200:
            txt +='#'
    txt = txt + '\n'
print txt
with open('/home/user/Pictures/1.txt','w') as f:
    f.write(txt)
print im1.show()

