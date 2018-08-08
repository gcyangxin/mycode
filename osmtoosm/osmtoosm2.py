#!/usr/bin/python
#coding: utf-8
from lxml import etree
import sys,getopt,time
class OsmToOsm:
	'''this fuction could genearate osm files from osm files'''
	def __init__(self,path):
		self.node_dict={}
		self.fin_node={}
		self.path=path
		self.tree=etree.parse(self.path)
		self.way_type=[
		'motorway',
		'trunk',
		'primary',
		'secondary',
		'tertiary',
		'motorway_link',
		'trunk_link',
		'primary_link',
		'secondary_link',
		#'tertiary_link'
		]
		#['motorway','trunk','primary','secondary','tertiary','motorway_link','trunk_link','primary_link','secondary_link','']
		self.way_element_list=[]
		self.osm=etree.Element('osm',version="0.6")
	def selectway(self):
		for w in self.way_type:
			p='way/tag/[@v="%s"]..'%(w)
			self.way_element_list+=self.tree.findall(p)
			if len(self.tree.findall(p)) == 0:
				pass
			else:
				print '%s  has been finded'%(w)
		#print self.way_element_list
		return self.way_element_list
	def nodedict(self):
		node_element_list=self.tree.findall("node")
		for k in node_element_list:
			coord=((k.get('lon'),k.get('lat')))
			self.node_dict[k.get('id')]=coord
		return self.node_dict#{'62543370': ('-82.9388230', '42.4068880')}
	def findallnode(self):
		for one in self.selectway():
			node_list=one.findall('nd')
			#print node_list
			node_id_list=[i.get('ref') for i in node_list]#['4216340519', '62896832', '62781702', '62635072', '62896828', '62896826', '62896824', '62896822', '62701255', '4216340518']
			for t in node_id_list:#t=ref:'62894014
				self.fin_node[t]=self.nodedict().get(t)#{'62894014':('-82.9574098','42.428562')}
		return self.fin_node#{'4216340519':(-82.9574098,42.428562)}
	def write(self):
		starttime=time.time()
		fin_list=self.findallnode().items()
		for x in fin_list:#('4216340519', ('-82.9371179', '42.4034025'))
			self.osm.append(etree.Element('node'))
			self.osm[-1].set('id' , x[0])
			self.osm[-1].set('visible' , 'true')
			self.osm[-1].set('version' , '2')
			self.osm[-1].set('lon',x[1][0])
			self.osm[-1].set('lat',x[1][1])
			#self.osm[-1].tail='\n'
		for a in range(len(self.way_element_list)):
			self.osm.append(self.way_element_list[a])
		with open('./new.osm','w') as f:
			f.write(etree.tostring(self.osm))
		endtime=time.time()
		print 'cost time:',round(endtime-starttime,1),'seconds'

def usage():
	print '''
usage:  python ./osmToosm.py  /home/user/oldname.osm
result: creat a file and to be  named ./new.osm

'''

if __name__ == '__main__':
	try:
		opts,args = getopt.getopt(sys.argv[1:],'h',['help','casedir='])
		if len(args) > 0 and args[0] !='':
			path=args[0]
			OsmToOsm(path).write()
		else:
			usage()
			sys.exit()
	except getopt.GetoptError as error:
		print str(error)
		usage()
		sys.exit()
