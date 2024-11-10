# utils/logger.py
import logging

def configurar_logger():
    logging.basicConfig(filename='bot.log', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
                                return logging.getLogger()

                                logger = configurar_logger()