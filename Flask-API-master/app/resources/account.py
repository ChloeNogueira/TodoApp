from flask import request
from flask_restful import Resource, reqparse, abort
from typing import Dict, List, Any

import uuid
from werkzeug.security import generate_password_hash, check_password_hash

from app.services.usersService import USERSLIST

class AccountResource(Resource):
    def post(self):
        body_parser = reqparse.RequestParser()
        body_parser.add_argument('usrnameauth', type=str, required=True, help="Missing the login of the user")
        body_parser.add_argument('pwdauth', type=str, required=True, help="Missing the password associated to the user login")
        args = body_parser.parse_args(strict=True) # Accepted only if these two parameters are strictly declared in body else raise exception
        try:   
            if(abort_if_username_is_not_unique(args['usrnameauth'])):
                return {'status':404,'message':'This username already exists, please choose an other one'}
            else:
                new_user = {}
                new_user['username'] = args['usrnameauth']
                new_user['password'] = generate_password_hash(args['pwdauth'], method='sha256')
                #new_user['password'] = args['pwdauth']
                new_user['public_id'] = str(uuid.uuid4())
                
                # On récupère la liste des id des users déjà existants
                ids_List=get_ids()
            
                # On récupère le premier id manquant parmi tous ceux existants déjà
                id = getFirstMissingID(ids_List)
                new_user['id'] = id
                USERSLIST.insert(id,new_user) 
                return {'data':new_user,'status':201,'message':'New user created'}
        except:
            abort(400)

def get_ids() -> List[int]:
    return list(map(lambda id: id['id'],USERSLIST))


def get_users_names() -> List[str]:
    return list(map(lambda users: users['username'],USERSLIST))
    
def getFirstMissingID(ids) -> int:
    j = 0
    ids.sort()
    for i in range(0,len(ids)):
        if ids[i] == j :
            j += 1
        else:
            break
    return j

def abort_if_username_is_not_unique(username: str):
    usernames = get_users_names()
    if username in usernames:
        return True
    
