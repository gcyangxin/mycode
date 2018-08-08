# coding=utf-8
import os,time
from multiprocessing import Pool
fie=raw_input('input save path,example:/home/user/xx:')
os.system('mkdir %s'%(fie))
x=raw_input('start_num: ')
y=raw_input('end_num: ')
str1='aws s3 cp s3://ygomi-test-us-east-1/20180109_release2.2.2.21_HP3567_patch_dengshuang/add_patch/rdb-test-aws-usa-device-'
str2='/ %s'%(fie)
str3='  --region us-east-1 --exclude "*" --include "*merge.jpg.gz"  --recursive'
l=[]

def run(txt):
    os.system(txt)
for n in range(int(x),int(y)+1):
    txt=str1+str(n)+str2+str3
    stt=time.time()
    try:
        print 'Download %s'%(n)
        print txt
        run(txt)
    except:
        print '%s timeout,next one '%(n)
        l.append(n)
    else:
        print '%s has done'%(n)
    finally:
        print 'Cost',round(time.time()-stt,1),'seconds'
with open('/home/user/unfinished.txt','w') as fb:
    fb.write(str(l))
print 'All files have done'
print 'unfinished files have saved /home/user/unfinished.txt'
