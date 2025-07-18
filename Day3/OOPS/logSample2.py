import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format='%(name)s - %(levelname)s - %(message)s'
)

logging.debug('Hello,Debug')
logging.info("Hello, Infoo")
logging.warning('Hello, Warning')
logging.error("hello error")
logging.critical("hello, critical")