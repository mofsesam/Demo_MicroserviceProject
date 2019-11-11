import os

from flask import Flask, request, jsonify, Response, abort

from sesamutils import sesam_logger, VariablesConfig
from sesamutils.flask import serve

required_env_vars = ["SUBDOMAIN"]
optional_env_vars = ["DEBUG", "LOG_LEVEL", ("API_ROOT","zendesk.com/api/v2/tickets/")] # Default values can be given to optional environment variables by the use of tuples

app = Flask(__name__)

logger = sesam_logger('DemoMicroservice', app=app,timestamp=True)

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
            abort(405) # Check closer what Flask abort does
            logger.error(f"ConnectionError issue while fetching tickets{request.method}")
        else:
            return jsonify(orders[orderID-1])
    except ConnectionError as e:
        logger.error(f"ConnectionError issue while fetching tickets{e}")
    except Exception as e:
        logger.error(f"Issue while fetching tickets from Zendesk {e}")

@app.route('/api/generic/<path:txt>', methods=['GET','PUT','POST','DELETE'])
def get_generic(txt):
    return jsonify({'generic': f'{request.method} {txt}','orders': orders })

@app.route('/api/show/config')
def get_config():
    return jsonify({'config': config})

if __name__ == "__main__":
    config = VariablesConfig(required_env_vars, optional_env_vars=optional_env_vars)
    logger.info(str(config))
    # if not config.validate():
    #     os.sys.exit(1)

    serve(app)