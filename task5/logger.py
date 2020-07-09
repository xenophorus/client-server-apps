import logging

logging.basicConfig(
    filename='log01.log',
    format='%(levelname)s %(asctime)s %(message)s',
    level=logging.DEBUG
)

LOG = logging.getLogger('app.basic')

LOG.debug('debug')
LOG.info('info')
LOG.error('error')
LOG.critical('critical')

