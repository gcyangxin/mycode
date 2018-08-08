#!/bin/bash
#!/usr/bin/expect -f
cd /home/user/3gpu/yx/dl-jinwen/; gedit test.py
cd ..
p1=`pwd`
ls ${p1}/test | grep jpg$ > ${p1}/name.txt
spawn ssh xin.yang@10.69.130.110
