#!/usr/bin/python
#coding: utf-8
import json,sys,getopt
from lxml import etree
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
class KmlGen:
	def __init__(self,path):
		self.path=path
		self.json_file=''
		self.fld=KML.Document(
			KML.name('new.kml'),
			KML.open('1'),
			KML.Style(
				KML.IconStyle(
				KML.scale('1.3'),
				KML.Icon(
					KML.href('http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png'),
			        	),
				KML.hotSpot(  x="20",y="2",xunits="pixels",yunits="pixels",),
				),id="color1"
			),
			KML.Style(
				KML.LineStyle(
					KML.color('ff00ffff'),
					KML.width('2')
				),id='type1'
			),
			KML.Style(
				KML.LineStyle(
					KML.color('ffffff00')
				),id='type2'
			),
			KML.styleMap(
				KML.pair(
					KML.key('normal'),
					KML.styleUrl('#type1')
				),
				KML.Pair(
					KML.key('highlight'),
		        			KML.styleUrl('#type2')
				)
			)
		)
	def loadjson(self,path):
		with open(self.path,'r') as tmp:
			self.json_file=json.load(tmp)
		return self.json_file
	def writecoord(self):
		fea_list=self.loadjson(self.path)['features']
		num=1
		for i in fea_list:
			coorlist=i['geometry']['coordinates']#[[8.4882786, 49.9307422], [8.4879952, 49.930298], [8.4878599, 49.9300566]]
			coord_str=''
			for cood in coorlist:
				if isinstance(cood,list):
					coord_str+=str(cood[0])+','+str(cood[1])+',0 '
				else:
					pass
			lookat=KML.Placemark(
				KML.name(num),
				KML.LookAt(
					KML.longitude(cood[0]),
					KML.latitude(cood[1]),
					KML.heading('-60'),
					KML.tilt('8.3'),
					KML.range('500')
				),
				KML.styleUrl('coolor1'),
				KML.Point(
					GX.drawOrder('1'),
					KML.coordinates(
						str(cood[0])+','+str(cood[1])+',0 '
					),
				),
			)
			place=KML.Placemark(
					KML.name(num),
					KML.styleUrl('#type1'),
					KML.visibility('1'),
					KML.description(''),
					KML.LineString(
						KML.extrude('1'),
						KML.coordinates(coord_str)
					)
			)
			self.fld.append(place),self.fld.append(lookat)
			num+=1
		with open('./new.kml','w') as f:
			f.write(etree.tostring(self.fld,pretty_print=True))
def usage():
	print '''
	usage : python ./jsontokml  json_file_path
	result: create a new kml file ,be named new.kml
	'''
if __name__ == '__main__':
	try:
		opts,args=getopt.getopt(sys.argv[1:],'h',['help'])
		if len(args)>0 and args[0] !=' ':
			path=args[0]
			KmlGen(path).writecoord()
		else:
			usage()
			sys.exit()
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit()
