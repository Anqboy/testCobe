import logging, sys
from flask import Flask

app = Flask(__name__)
i = 0


sys.stdout = open('log2.log', 'a')


@app.route("/")
def hello():
    app.logger.critical("this is a CRITICAL message)")
    print(i)
    i += 1
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug = True, threaded = True)


# logger = logging.getLogger()
# handler = logging.StreamHandler()
# logger.addHandler(handler)


# # fileHandler = logging.FileHandler("firstLog.log")
# # logger.addHandler(fileHandler)


# consoleHandler = logging.StreamHandler()
# logger.addHandler(consoleHandler)

# app.logger.handlers = logger