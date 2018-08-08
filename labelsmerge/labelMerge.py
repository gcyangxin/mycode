#coding: utf-8
import json,os,copy,math
dellabel=(
'merged',
'forked',
'diversion',
#'road-marking',
'road',
'unlabelled',
'direction'
)
def GetLineLength(l):
    length=0
    num=len(l)
    for n in range(num):
        if n < num-1:
            p1=l[n]
            p2=l[n+1]
            c_length = math.pow((p1[0]-p2[0]),2) + math.pow((p1[1]-p2[1]),2)
            length += math.sqrt(c_length)
        elif n == num-1:
            p1=l[0]
            p2=l[n]
            c_length = math.pow((p1[0]-p2[0]),2) + math.pow((p1[1]-p2[1]),2)
            length += math.sqrt(c_length)
    return round(length,1)
def selectlabel(jp):
    with open(jp,'r') as f:
        jsonfile=json.load(f)
    jsoncpfile=copy.deepcopy(jsonfile)
    for i in jsonfile['objects']:
        if i['label'] in dellabel:
            jsoncpfile['objects'].remove(i)
    return jsoncpfile
def selectdash(jp1):
    jslist=[]
    with open(jp1,'r') as f1:
        jf1=json.load(f1)
    for x in jf1['objects']:
        if x['label'] in 'dashed':
            x['label']='dash-connect'
            jslist.append(x)
    return jslist
def writejson():
    jsonfile2=selectlabel(jp)
    jslist=selectdash(jp1)
    h=jsonfile2['imgHeight']
    w=jsonfile2['imgWidth']
    roaddit={
            "date": "",
            "deleted": 0,
            "draw": True,
            "id": 999,
            "label": "road",
            "polygon": [
                [
                    0,
                    0
                ],
                [
                    0,
                    h-1
                ],
                [
                    w-1,
                    h-1
                ],
                [
                    w-1,
                    0
                ]
            ],
            "user": "",
            "verified": 0
        }



    jsonfile2['objects'][0:0]=jslist
    jsonfile3=copy.deepcopy(jsonfile2)
    for i in jsonfile2['objects']:
        polygon=i['polygon']
        if GetLineLength(polygon) < 110:#设置最大像素周长
            jsonfile3['objects'].remove(i)


    jsonfile3['objects'].insert(0,roaddit)
    with open(os.path.join(save_path,x),'w') as f3:
        f3.write(json.dumps(jsonfile3,indent=4))
if __name__ == '__main__':
        con_path='/home/user/Documents/dl/tools/labelTool/convert/test'
        dis_path='/home/user/Documents/dl/tools/labelTool/convert/disseleted_for_yx'
        save_path='/home/user/Documents/dl/tools/labelTool/convert/test/2'
        jsonlist=[x for x in os.listdir(con_path) if '.json' in x]
        for x in jsonlist:
            jp=os.path.join(dis_path,x)
            jp1=os.path.join(con_path,x)
            writejson()
