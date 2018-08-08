#coding: utf-8
日志
import logging
import time
def create_logger(log_file_name='./running.log',
           log_level=logging.DEBUG,
           log_date_format='%Y-%m-%d %H:%M:%S%z',
           log_formater='%(asctime)s %(filename)s:%(levelname)s %(message)s'
           ):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=log_level, format=log_formater, datefmt=log_date_format)
    handler=logging.FileHandler(log_file_name)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(log_formater))
    logger.addHandler(handler)
    return logger
logger=create_logger()
for i in range(10):
    logger.debug('%s'%(i))

参数，时间
parser = argparse.ArgumentParser()
parser.add_argument('queryDir', type=str)
parser.add_argument('--image_size', type=int, default=2048, choices=[320,640,1024,2048])
args = parser.parse_args()
if os.path.isdir(args.queryDir):
#######
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
$ python3 prog.py foo
foo


baseDir = 'images_' + time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())) + '/'

