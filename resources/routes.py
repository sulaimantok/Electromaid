from .post import PostsApi, PostApi
from .auth import SignupApi, LoginApi
from .sensor import SensorsApi, SensorApi
from .notif import NotifsApi, NotifApi
from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
 api.add_resource(PostsApi, '/v1/post')
 api.add_resource(PostApi, '/v1/post/<id>')

 api.add_resource(SignupApi, '/v1/auth/signup')
 api.add_resource(LoginApi, '/v1/auth/login')

 api.add_resource(SensorsApi, '/v1/sensor')
 api.add_resource(SensorApi, '/v1/sensor/<id>')

 api.add_resource(ForgotPassword,'/v1/auth/forgot')
 api.add_resource(ResetPassword,'/v1/auth/reset')

 api.add_resource(NotifsApi,'/v1/notif')
 api.add_resource(NotifApi,'/v1/notif/<id>')
