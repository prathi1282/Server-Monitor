from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return f"cpu_usage {cpu}\nmemory_usage {memory}\ndisk_usage {disk}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)