from flask import Flask, request, jsonify, Response, abort
from werkzeug.exceptions import HTTPException
import logging

logger = logging

app = Flask(__name__)

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

@app.route('/api/orders/update/<orderID>', methods=['GET','PUT','POST','DELETE']) 
def update_ticket(orderID):
    try:
        if request.method != 'PUT':
            return request.method 
            abort(405)
        else:
            return jsonify({'orders': orders})
    except HTTPException as e:
        logger.error(f"Connector http error {e}")
    except ConnectionError as e:
        logger.error(f"ConnectionError issue while fetching tickets{e}")
    except Exception as e:
        logger.error(f"Issue while fetching tickets from Zendesk {e}")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)