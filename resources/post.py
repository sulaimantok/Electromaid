from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Post
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, AlreadyExistsError, InternalServerError, UpdatingError, DeletingError, NotExistsError

class PostsApi(Resource):
  def get(self):
    try:
        posts = Post.objects().to_json()
        return Response(posts, mimetype="application/json", status=200)
    except DoesNotExist:
        raise NotExistsError
    except Exception:
        raise InternalServerError

  @jwt_required
  def post(self):
    try:
        body = request.get_json()
        post = Post(**body).save()
        id = post.id
        return {'id': str(id)}, 200
    except (FieldDoesNotExist, ValidationError):
        raise SchemaValidationError
    except NotUniqueError:
        raise AlreadyExistsError
    except Exception as e:
        raise InternalServerError
 
class PostApi(Resource):
  @jwt_required
  def put(self, id):
    try:
        body = request.get_json()
        Post.objects.get(id=id).update(**body)
        return '', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingError
    except Exception:
        raise InternalServerError 
 
  @jwt_required
  def delete(self, id):
    try:
        post = Post.objects.get(id=id).delete()
        return '', 200
    except DoesNotExist:
        raise DeletingError
    except Exception:
        raise InternalServerError

  def get(self, id):
    try:
        posts = Post.objects.get(id=id).to_json()
        return Response(posts, mimetype="application/json", status=200)
    except DoesNotExist:
        raise NotExistsError
    except Exception:
        raise InternalServerError
