from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def orderpage():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])

def write_orders():
    ordername_receive = request.form['ordername_give']
    orderquantity_receive = request.form['orderquantity_give']
    orderaddress_receive = request.form['orderaddress_give']
    orderphoneno_receive = request.form['orderphoneno_give']

    order = {
        'order_name': ordername_receive,
        'order_quantity': orderquantity_receive,
        'order_address': orderaddress_receive,
        'order_phoneno': orderphoneno_receive
    } 

    db.orders.insert_one(order)
    return jsonify({'result':'success', 'msg':'주문이 완료되었습니다.'})
        

@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': orders})

    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)