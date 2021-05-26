from flask import request, redirect, url_for
from flask_restful import Resource, reqparse, abort
from typing import Dict, List, Any

import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

from app.services.usersService import USERSLIST

class LoginResource(Resource):

    def post(self):
        body_parser = reqparse.RequestParser()
        body_parser.add_argument('usrname', type=str, required=True, help="Missing the login of the user")
        body_parser.add_argument('pwd', type=str, required=True, help="Missing the password associated to the user login")
        args = body_parser.parse_args(strict=True) # Accepted only if these two parameters are strictly declared in body else raise exception
        try:
            usr_name = args['usrname']
            password_hash = args['pwd']       
            if (not abort_if_username_doesnt_exist(usr_name)):
                user_trying_to_connect = get_user(usr_name)[0]
                # On vérifie que le mot de passe saisi est identique à celui de l'utilisateur dans le service usersService 
                if check_password_hash(user_trying_to_connect['password'],password_hash):
                #if (user_trying_to_connect['password'] == password_hash):
                    encoded_jwt = jwt.encode({'public_id': user_trying_to_connect['public_id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},'thisissecret',algorithm='HS256').decode('utf-8')
                    message = 'Logged in successfully'
                    status = 200
                    return {'token':encoded_jwt,'message':message,'status':status}
                else:
                    return {'status':404,'message':"Your password is incorrect, try again"}
            else:
                return {'status':404,'message':'Your username does not exists'}

            
        except:
            abort(400)

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return {'message': 'Token is missing'}
        try:
            data = jwt.decode(token, "thisissecret",algorithms=['HS256'])
            current_user = get_user_public_id(data['public_id'])
        except:
            return {'message': 'Token is invalid'}

        return f(current_user, *args, **kwargs)
    
   return decorator

def get_users_names() -> List[str]:
    return list(map(lambda users: users['username'],USERSLIST))

def get_user(username:str):
    return list(filter(lambda user: user['username'] == username, USERSLIST))

def get_user_public_id(public_id:str):
    return list(filter(lambda user: user['public_id'] == public_id, USERSLIST))
    
def abort_if_username_doesnt_exist(username: str):
    usernames_list = get_users_names()
    if username not in usernames_list:
        return True
    