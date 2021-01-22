from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Sensor
from flask_restful import Resource
from resources.api_key import require_appkey
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, AlreadyExistsError, InternalServerError, UpdatingError, DeletingError, NotExistsError

class SensorsApi(Resource):
  #@jwt_required
  def get(self):
    try:
        sensors = Sensor.objects().to_json()
        return Response(sensors, mimetype="application/json", status=200)
    except DoesNotExist:
        raise NotExistsError
    except Exception:
        raise InternalServerError

  #@jwt_required
  def post(self):
    #id = sensor.id
    body = request.get_json()
    sensor = Sensor(**body).save()
    id = sensor.id
    return {'id': str(id)}, 200

class SensorApi(Resource):
  #@jwt_required
  @require_appkey
  def get(self, id):
    try:
        sensor = Sensor.objects.get(id=id).to_json()
        return Response(sensor, mimetype="application/json", status=200)
    except DoesNotExist:
        raise NotExistsError
    except Exception:
        raise InternalServerError

  #@jwt_required
  @require_appkey
  def put(self, id):
    try:
        body = request.get_json()
        Sensor.objects.get(id=id).update(**body)
        return {'id':str(id)}, 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingError
    except Exception:
        raise InternalServerError 
