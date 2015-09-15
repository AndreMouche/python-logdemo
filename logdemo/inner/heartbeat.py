import time
import logging

LOG = logging.getLogger(__name__)

def start():
    while True:
        LOG.info('hello, I love you.')
        time.sleep(1)
