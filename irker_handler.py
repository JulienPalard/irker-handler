import json
import logging.handlers

__version__ = "0.0.1"


class IrkerHandler(logging.handlers.DatagramHandler):
    def __init__(self, to):
        """Sends logs to an irker daemon.

        See man irkerd for `to` parameter.
        """
        super().__init__("127.0.0.1", 6659)
        self.to = to

    def makePickle(self, record):
        return json.dumps({"to": self.to, "privmsg": record.getMessage()}).encode(
            "UTF-8"
        )
