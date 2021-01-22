class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class AlreadyExistsError(Exception):
    pass

class UpdatingError(Exception):
    pass

class DeletingError(Exception):
    pass

class NotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class EmailDoesnotExistsError(Exception):
    pass

class BadTokenError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "AlreadyExistsError": {
         "message": "data with given name already exists",
         "status": 400
     },
     "UpdatingError": {
         "message": "Updating data added by other is forbidden",
         "status": 403
     },
     "DeletingError": {
         "message": "Deleting data added by other is forbidden",
         "status": 403
     },
     "NotExistsError": {
         "message": "data with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
     "EmailDoesnotExistsError": {
         "message": "Couldn't find the user with given email address",
         "status": 400
     },
     "BadTokenError": {
         "message": "Invalid token",
         "status": 403
      }
}
