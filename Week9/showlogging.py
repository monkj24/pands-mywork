# demonstrate logging
# Attributes 
# level
# filename
# filemode
 # format
# %(name)s, %(levels name), %(message), %(acttime), %(lineno)

import logging
logging.basicConfig(filename="./mainlog.log",
                    level=logging.WARN)

# prog does stuff
logging.debug("We are doing stuff")
logging.info("this is information")
logging.warning("oooh")
logging.error("not good")
logging.critical("really bad")
             
