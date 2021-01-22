from functools import wraps
from flask import request, abort


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        #with open('/home/sulaiman/Documents/Kuliah/Semester 5/RPL/elektromaid/resources/api.key', 'r') as apikey:
        with open('/app/resources/api.key', 'r') as apikey:
            key=apikey.read().replace('\n', '')
            #key = "eiWee8ep9due4deeshoa8Peichai8Eih"
        #if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
