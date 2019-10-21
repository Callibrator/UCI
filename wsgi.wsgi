#!/usr/bin/python
import sys
import logging
import os


logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/UCI')



os.chdir("/var/www/UCI")


from app import app as application

#application.run(host="0.0.0.0", port=5000)
