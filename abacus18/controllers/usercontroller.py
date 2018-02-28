from pyramid.view import view_config
from ..helpers.helper import Helper
import os
import bcrypt
from pyramid.response import Response, FileResponse
from ..models import Session


from ..models.usermodel import user
@view_config(route_name='users.login', request_method="POST")
def login(request):
    try: 
        session = Session()
        request_body = request.json_body
        if 'email' in request_body and 'password' in request_body:
            '''
                         SELECT * FROM user where user.email = emailEntered
            '''
            result_set = session.query(user) \
                            .filter(user.email == request_body['email']).first()
                            
            code = 0
            message = ''
            response_body = ''
            if not result_set:
                code = 404
                message = 'user not found'
            else: 


                password = request_body['password'].encode('utf8') 
                hashed = result_set.password.encode('utf8')
                if bcrypt.checkpw(password, hashed):
                    code = 200
                    message = 'Success'
                    response_body = {
                        'token' :   request.create_jwt_token(result_set.email, user_id=result_set.id),
                         'userDetails' : {
                                'role' : result_set.role,
                                'email': result_set.email
                             }   
                                }
                else:
                    code = 401
                    message = 'Unauthorized'
        else:
                code = 500
                message = 'Incomplete Data'
                response_body = 'Email or Password Missing'        
        session.close()    
        return    Helper.construct_response(code, message, response_body)
    except Exception as e:
        print(e)
        return Helper.construct_response(500, str(e) , 'Server Error')