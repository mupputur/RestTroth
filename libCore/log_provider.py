import logging
import os,datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s::%(filename)s::%(lineno)s::%(funcName)s\::%(msg)s')



filehandler = logging.FileHandler('G:\RestAPIFramework\logs/framework{}.log'.format
                           (datetime.datetime.strftime(datetime.datetime.now(),'%d%m%Y')))
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

class Logger:
    """
    def __init__(self,logger =None):
        self.logger = logger or logging.getLogger(__name__)
    """
    @classmethod
    def log_info(self, msg):
        logger.info(msg)

    @classmethod
    def log_error(self, msg):
        logger.error(msg)

    @classmethod
    def log_warning(self, msg):
        logger.warning(msg)