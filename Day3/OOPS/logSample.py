import logging

#the level is set to warning by 


logging.basicConfig(level=logging.DEBUG)

logging.debug('Hello,Debug')
logging.info("Hello, Infoo")
logging.warning('Hello, Warning')
logging.error("hello error")
logging.critical("hello, critical")