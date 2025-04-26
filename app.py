from flask import Flask, render_template, jsonify
import sensor
import data_store

app = Flask(__name__)

@app.route('/')
def home():
    all_data = data_store.get_all_data()
    avg_temp = data_store.get_average_temperature()
    return render_template('index.html', data=all_data, average=avg_temp)

@app.route('/collect')
def collect():
    data = sensor.collect_data()
    data_store.store_data(data)
    return jsonify({"message": "Data collected", "data": data})

if __name__ == '__main__':
    app.run(debug=True)