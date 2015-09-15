import logging.config
import logging

log_cnf = './logging.cnf'
logging.config.fileConfig(log_cnf, disable_existing_loggers=False)

LOG = logging.getLogger(__name__)


import os
import sys
pkg_root = os.path.realpath(os.path.join(os.path.curdir, os.path.pardir))
sys.path.append(pkg_root)

from logdemo.inner import heartbeat


def main():
    LOG.info('heartbeat start ...')
    heartbeat.start()


if __name__ == '__main__':
    main()
