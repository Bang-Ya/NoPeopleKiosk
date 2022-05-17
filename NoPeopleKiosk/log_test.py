import logging
import logging.handlers
import os

LOG_MAX_SIZE = 1024 * 1024 * 10

LOG_FILE_CNT = 10

LOG_LEVEL = logging.INFO

try:
    logger = logging.getLogger('log_test')
    logfile_H = logging.handlers.TimedRotatingFileHandler(filename='logs//logfile.log',when='midnight', interval=0, backupCount=LOG_FILE_CNT, encoding='utf-8')

    # "%Y-%m-%d %H:%M:%S"를 "%m월%d일 %H:%M:%S"로 수정하여 연도를 때어내고 형식을 바꾸었음.
    formatter = logging.Formatter('[%(asctime)s|%(levelname)s|%(funcName)s|%(lineno)d] %(message)s',"%m월%d일 %H:%M:%S")
    logfile_H.setFormatter(formatter)
    logfile_H.suffix="%Y%m%d"
    logger.addHandler(logfile_H)
    logger.setLevel(LOG_LEVEL)

    logger.info("======================program start set======================")
    logger.info(" this version is =====1.0===== ")
    logger.info("start program set 1")
    logger.warning("start program set 2")
    logger.error("start program set 3")
    logger.critical("start program set 4")
    logger.debug("start program set ====debug====5")
    logger.info("======================program start set end======================")

except Exception as err:
    logger.error(err)