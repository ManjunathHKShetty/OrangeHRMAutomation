import os
import logging


class LogGen:
    @staticmethod
    def loggen():
        log_dir = "C:\\Users\\Ifomet\\Desktop\\PyCharmProjects\\OrangeHRM_Automation\\Logs"

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(
            filename=os.path.join(log_dir, 'auto.log'),
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m%d%Y %I:%M:%S %p',
            level=logging.INFO,
            force=True
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
