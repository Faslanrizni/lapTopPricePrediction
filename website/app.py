import pickle

import numpy as np
# import requests
from flask import Flask, render_template,request

app = Flask(__name__)


def prediction(list):
    fileName ='model/predictor.pickle'
    with open(fileName, 'rb') as file:
        model = pickle.load(file)
        pred_value =model.predict([list])
        return pred_value


@app.route('/', methods=['POST', 'GET'])
def index():
    pred = 0
    if request.method == 'POST':
        ram = request.form['ram']
        weight = request.form['weight']
        company = request.form['company']
        typename = request.form['typename']
        opsys = request.form['opsys']
        cpuname = request.form['cpuname']
        gpuname = request.form['gpuname']
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')

        featureList = []
        featureList.append(int(ram))
        featureList.append(float(weight))
        featureList.append(len(touchscreen))
        featureList.append(len(ips))

        company_list = ['acer', 'apple', 'asus', 'dell', 'hp', 'lenovo', 'msi', 'other', 'toshiba']
        typename_list = ['2in1convertible', 'gaming', 'netbook', 'notebook', 'ultrabook', 'workstation']
        opsys_list = ['linux', 'mac', 'other', 'windows']
        cpu_list = ['amd', 'intelcorei3', 'intelcorei5', 'intelcorei7', 'other']
        gpu_list = ['amd', 'intel', 'nvidia']

        def iterateList(list, value):
            for item in list:
                if item == value:
                    featureList.append(1)
                else:
                    featureList.append(0)

        iterateList(company_list, company)
        iterateList(typename_list, typename)
        iterateList(opsys_list, opsys)
        iterateList(cpu_list, cpuname)
        iterateList(gpu_list, gpuname)

        pred = prediction(featureList)*200

        pred = np.round(pred[0])





    return render_template('index.html',pred = pred)


if __name__ == '__main__':
    app.run(debug=True)
