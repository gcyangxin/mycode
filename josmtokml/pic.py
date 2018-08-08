# coding=utf-8
import os
from timeout import timeout
x=raw_input('start_num')
y=raw_input('end_num')
str1='aws s3 cp s3://ygomi-test-us-east-1/20180109_release2.2.2.21_HP3567_patch_dengshuang/add_patch/rdb-test-aws-usa-device-'
str2='/ ./yxxxx/'
str3='  --region us-east-1 --exclude "*" --include "*merge.jpg.gz"  --recursive'
for n in range(int(x),int(y)+1):
    txt=str1+str(n)+str3
    try:
        run(txt)
    except:
        pass
@timeout(300)
def run(txt):
    os.system(txt)
