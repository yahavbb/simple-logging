import logging
import sys
from logging import config

syslog_server = '127.0.0.1'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(module)s P%(process)d T%(thread)d %(message)s'
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
        'syslog-server': {
            'class': 'logging.handlers.SysLogHandler',
            'address': (syslog_server, 514),
            'facility': "local6",
            'formatter': 'verbose',
        },
        'syslog-daemon': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'facility': "local6",
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'output': {
            'handlers': ['syslog-server', 'stdout'],
            'level': logging.ERROR,
            'propagate': True,
        },
        'local': {
            'handlers': ['syslog-daemon', 'stdout'],
            'level': logging.DEBUG,
            'propagate': True,
        },
    }
}
LOG_LEVEL_MAPPING = {
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}


def run():
    config.dictConfig(LOGGING)
    server = logging.getLogger("output")
    local = logging.getLogger("local")
    
    while True:
        data =input("Enter log message\n")
        log_level = LOG_LEVEL_MAPPING.get(data.lower().split(" ")[0])
        data = data.split(" ",1)[1]

        if log_level is not None:
            server.log(log_level, data)
            local.log(log_level, data)
if __name__ == '__main__':
    run()
