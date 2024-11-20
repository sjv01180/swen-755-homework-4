import requests
# The client (unittest) can only contact the server using RESTful API calls


# For API calls using GET.  params and header are defaulted to 'empty'

def get_rest_call(test, url, params = {}, headers = {}, expected_code = 200):
    response = requests.get(url, params, headers=headers)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

def get_rest_payload_call(test, url, payload=None, headers={}, expected_code=200):
    '''Implements a REST api call using the POST verb with a JSON payload'''
    response = requests.get(url, json=payload, headers=headers)
    test.assertEqual(expected_code, response.status_code,
                    f'Response code to {url} not {expected_code}')
    return response.json()

# For API calls using POST.  params and header are defaulted to 'empty'

def post_rest_call(test, url, params = {}, headers = {},expected_code = 200):
    '''Implements a REST api using the POST verb'''
    response = requests.post(url, params, headers=headers)
    test.assertEqual(expected_code, response.status_code,
                    f'Response code to {url} not {expected_code}')
    return response.json()

def post_rest_payload_call(test, url, payload=None, headers={}, expected_code=200):
    '''Implements a REST api call using the POST verb with a JSON payload'''
    response = requests.post(url, json=payload, headers=headers)
    test.assertEqual(expected_code, response.status_code,
                    f'Response code to {url} not {expected_code}')
    return response.json()


# For API calls using PUT.  params and header are defaulted to 'empty'

def put_rest_call(test, url, params = {}, headers = {},expected_code = 200):
    '''Implements a REST api using the PUT verb'''
    response = requests.put(url, params, headers=headers)
    test.assertEqual(expected_code, response.status_code,
                    f'Response code to {url} not {expected_code}')
    return response.json()

def put_rest_payload_call(test, url, payload=None, put_header = {},expected_code = 200):
    '''Implements a REST api using the PUT verb'''
    response = requests.put(url, json=payload, headers = put_header)
    test.assertEqual(expected_code, response.status_code,
                    f'Response code to {url} not {expected_code}')
    return response.json()

def put_rest_payload_call(test, url, payload=None, headers={}, expected_code=200):
    '''Implements a REST api call using the PUT verb with a JSON payload'''
    response = requests.put(url, json=payload, headers=headers)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

# For API calls using DELETE.  header is defaulted to 'empty'

def delete_rest_call(test, url, headers={}, expected_code = 200):
    '''Implements a REST api using the DELETE verb'''
    response = requests.delete(url, headers = headers)
    test.assertEqual(expected_code, response.status_code,
                     f'Response code to {url} not {expected_code}')
    return response.json()

