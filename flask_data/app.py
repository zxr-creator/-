from multiprocessing.sharedctypes import Value
from operator import ge
from unicodedata import name
from django.http import response
from django.shortcuts import render
from flask import Flask, render_template, request,redirect,url_for
from flask import jsonify
from flask_cors import CORS
from matplotlib.font_manager import json_load
from matplotlib.pyplot import get
from pathy import BasePath
import json
from flask_sqlalchemy import SQLAlchemy
import csv

DEBUG = True
PROVINCE = None
DATA1 = None

app = Flask(__name__)
app.config.from_object(__name__)
cors = CORS(app)

#设置编码
app.config['JSON_AS_ASCII'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
# 指定数据库文件
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
# 允许修改跟踪数据库
db = SQLAlchemy(app)
 
@app.route('/api/getMsg', methods=['GET', 'POST'])
def province():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\datas.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getBar', methods=['GET','POST'])
def DATA1():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\bardata.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getScatter', methods=['GET','POST'])
def DATA2():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\scatterdata.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getPie', methods=['GET','POST'])
def DATA3():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\piedata.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata', methods=['GET','POST'])
def DATA4():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})
 
@app.route('/api/getlinedata1', methods=['GET','POST'])
def DATA5():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata1.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata2', methods=['GET','POST'])
def DATA6():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata2.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata3', methods=['GET','POST'])
def DATA7():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata3.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata4', methods=['GET','POST'])
def DATA8():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata4.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata5', methods=['GET','POST'])
def DATA9():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata5.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata6', methods=['GET','POST'])
def DATA10():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata6.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata7', methods=['GET','POST'])
def DATA11():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata7.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata8', methods=['GET','POST'])
def DATA12():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata8.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata9', methods=['GET','POST'])
def DATA13():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata9.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata10', methods=['GET','POST'])
def DATA14():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata10.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata11', methods=['GET','POST'])
def DATA15():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata11.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata12', methods=['GET','POST'])
def DATA16():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata12.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata13', methods=['GET','POST'])
def DATA17():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata13.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata14', methods=['GET','POST'])
def DATA18():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata14.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata15', methods=['GET','POST'])
def DATA19():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata15.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata16', methods=['GET','POST'])
def DATA20():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata16.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata17', methods=['GET','POST'])
def DATA21():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata18.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata18', methods=['GET','POST'])
def DATA22():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata18.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata19', methods=['GET','POST'])
def DATA23():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata19.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata20', methods=['GET','POST'])
def DATA24():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata20.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata21', methods=['GET','POST'])
def DATA25():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata21.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata22', methods=['GET','POST'])
def DATA26():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata22.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata23', methods=['GET','POST'])
def DATA27():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata23.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata24', methods=['GET','POST'])
def DATA28():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata24.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata25', methods=['GET','POST'])
def DATA29():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata25.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata26', methods=['GET','POST'])
def DATA30():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata26.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata27', methods=['GET','POST'])
def DATA31():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata27.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata28', methods=['GET','POST'])
def DATA32():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata28.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata30', methods=['GET','POST'])
def DATA33():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata30.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata31', methods=['GET','POST'])
def DATA34():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata31.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 

@app.route('/api/getlinedata32', methods=['GET','POST'])
def DATA35():
    try:
        with open('D:\\VS_code\\code\\JavaScript\\vue\\demo\\flask_data\\static\\linedata\\linedata32.json','r',encoding='UTF-8') as f:
            jsonStr = json.load(f)
            return json.dumps(jsonStr)
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)}) 
# 启动运行
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8002)   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='120.79.80.194') # 这里可通过 host 指定在公网IP上运行