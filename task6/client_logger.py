import logging
import sys
import time


LOG = logging.getLogger('client.log')
fmt = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')

fhandler = logging.FileHandler(f'log/client_{time.strftime("%Y_%m_%d")}.log', encoding='utf-8')
fhandler.level = logging.DEBUG
fhandler.formatter = fmt

shandler = logging.StreamHandler(sys.stderr)
shandler.level = logging.ERROR
shandler.formatter = fmt

LOG.addHandler(fhandler)
LOG.addHandler(shandler)
LOG.setLevel(logging.DEBUG)

if __name__ == '__main__':
    LOG.info('logging started')
