import logging
import time


# logging.basicConfig(
#     filename=f'log/app.log',
#     format='%(levelname)s %(filename)s %(asctime)s %(message)s',
#     level=logging.DEBUG
# )

LOG = logging.getLogger('server.log')
fmt = logging.Formatter('%(levelname)s %(filename)s %(asctime)s %(message)s')


fhandler = logging.FileHandler(f'log/server_{time.strftime("%Y_%m_%d")}.log', encoding='utf-8')
fhandler.level = logging.DEBUG
fhandler.formatter = fmt

LOG.addHandler(fhandler)
LOG.setLevel(logging.DEBUG)


if __name__ == '__main__':
    LOG.info('logging started')
