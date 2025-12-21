from flask import Flask, render_template, jsonify
from code1 import get_matplotlib_plot
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/get-grafik')
def get_grafik():
  data_output = get_matplotlib_plot()
  return jsonify(data_output)

if __name__ == '__main__':
  app.run(debug=True)
