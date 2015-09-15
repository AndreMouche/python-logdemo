import time
import logging

LOG = logging.getLogger(__name__)

def start():
    while True:
        LOG.info('hello, I love you.')
        LOG.debug('debug , I hate you.')
        LOG.warn('warn, I do not like you')
        LOG.error('error, I fuck you')
        time.sleep(1)
