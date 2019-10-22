from flask import Flask, request, jsonify, Response, abort
from flask_sqlalchemy import SQLAlchemy

from sesamutils import sesam_logger
from sesamutils.flask import serve

app = Flask(__name__)
logger = sesam_logger('DemoMicroservice', app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    Orders = db.Column(db.String(80))
    TotalSum = db.Column(db.Integer())

    def __repr__(self):
        return '<User %r>' % self.username

orders = [
{
    'id': 1,
    'Username': u'Unjudosely',
    'Orders': u'Thinkpad',
    'TotalSum': 8000
    },
    {
    'id': 2,
    'Username': u'Wimen1979',
    'Orders': u'MacbookPro',
    'TotalSum': 12000
    },
    { 'id': 3,
    'Username': u'Gotin1984',
    'Orders': u'Chormebook',
    'TotalSum': 10000
    }

]

@app.route('/api/orders')
def get_orders():
    return jsonify({'orders': orders})

@app.route('/api/orders/update/<int:orderID>', methods=['GET','PUT','POST','DELETE']) 
def update_ticket(orderID):
    try:
        if request.method != 'PUT':
            return request.method 
            abort(405)
        else:
            return jsonify(orders[orderID-1])
    except ConnectionError as e:
        logger.error(f"ConnectionError issue while fetching tickets{e}")
    except Exception as e:
        logger.error(f"Issue while fetching tickets from Zendesk {e}")

if __name__ == "__main__":
    serve(app)