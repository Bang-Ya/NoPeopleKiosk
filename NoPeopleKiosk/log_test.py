import logging
import logging.handlers

LOG_MAX_SIZE = 1024 * 1024 * 10

LOG_FILE_CNT = 10

LOG_LEVEL = logging.INFO

try:

    logger = logging.getLogger('log_test')

    logfile_H = logging.handlers.RotatingFileHandler("./logs/log_test.log", maxBytes=LOG_MAX_SIZE,
                                                     backupCount=LOG_FILE_CNT)

    # "%Y-%m-%d %H:%M:%S"를 "%m월%d일 %H:%M:%S"로 수정하여 연도를 때어내고 형식을 바꾸었음.
    formatter = logging.Formatter('[%(asctime)s|%(levelname)s|%(funcName)s|%(lineno)d] %(message)s',"%m월%d일 %H:%M:%S")

    logfile_H.setFormatter(formatter)

    logger.addHandler(logfile_H)

    logger.setLevel(LOG_LEVEL)

    logger.info("INFO 정보입니다")

    logger.debug("DEBUG 정보입니다")

    logger.warning("WARNING 정보입니다")

    logger.error("ERROR 정보입니다")

    logger.critical("CRITICAL 정보입니다")


except Exception as err:

    logger.error(err)