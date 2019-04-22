import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def host_info():
    return (
        f'Running:\n'
        f'* host: {os.environ["HOSTNAME"]}\n'
        f'* time: {time.ctime()}\n'
    )

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
