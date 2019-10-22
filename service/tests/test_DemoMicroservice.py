
def test_get_routes(client):
    """
    GIVEN a response
    WHEN endpoint /api/orders get a GET call
    THEN check response value
    """
    rv = client.get('/api/orders')
    assert b'Wimen1979' in rv.data

def test_put_routes(client):
    """
    GIVEN a response
    WHEN endpoint /api/orders/update/<int:orderID> get a call
    THEN check response value relativ to orderID and call method
    """
    rv = client.put('/api/orders/update/2')
    assert b'Wimen1979' in rv.data
    rv = client.put('/api/orders/update/3')
    assert 'Gotin1984' in rv.json['Username']
    rv = client.get('/api/orders/update/2')
    assert b'GET' in rv.data
    rv = client.post('/api/orders/update/2')
    assert b'POST' in rv.data
    rv = client.delete('/api/orders/update/2')
    assert b'DELETE' in rv.data