import psutil
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def indexofapp():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 90 or mem_percent > 90:
        Message = "High CPU or Memory Detected, scale up!!!"
    return f"CPU Utilization: {cpu_percent} and MemoryUtilization: {mem_percent}"


if __name__ == '__main__':
  app.run(debug=True, host ='0.0.0.0')

