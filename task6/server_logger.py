import logging
import time
import sys


LOG = logging.getLogger('server.log')
fmt = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')

fhandler = logging.FileHandler(f'log/server_{time.strftime("%Y_%m_%d")}.log', encoding='utf-8')
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
