import logging
import json


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, "%F"),
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


log = logging.getLogger("logger_bot")
log.setLevel(logging.INFO)

fh = logging.FileHandler(filename="logger.txt", mode="a", encoding="utf-8")
fh.setFormatter(JsonFormatter())
log.addHandler(fh)
