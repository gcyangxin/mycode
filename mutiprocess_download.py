from multiprocessing import Pool
import os,time
fie=raw_input('input save path.Example:/home/user/xx:')
os.system('mkdir %s'%(fie))
x=raw_input('start_num: ')
y=raw_input('end_num: ')
str1='timeout 300 aws s3 cp s3://ygomi-test-us-east-1/20180113144808_HP-8-16_20180115_release2_2_2_21_dengshuang_patch/uploads/rdb-test-aws-usa-device-'
str2='/ %s'%(fie)
str3='  --region us-east-1 --exclude "*" --include "*origin.jpg.gz"  --recursive'
txt_l=[]
def run(txt):
    print txt
    os.system(txt)
def gettxt():
    for n in range(int(x),int(y)+1):
        txt=str1+str(n)+str2+str3
        txt_l.append(txt)
gettxt()
p=Pool()
for t in range(len(txt_l)):
    txt=txt_l[t]
    p.apply_async(run,args=(txt,))
p.close()
p.join()
print 'all done'

