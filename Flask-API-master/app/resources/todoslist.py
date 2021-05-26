from flask import request
from flask_restful import Resource, reqparse, abort

from typing import Dict, List, Any
from app.services import todosListService
from app.services.todosService import TODOS
from app.services.todosListService import TODOSLIST
from app.resources.login import token_required
from flask_cors import CORS, cross_origin


class TodoListManagementResource(Resource):
    @token_required
    def get(current_user,self) -> List:
        """
        Return all the todoLists in TODOSLIST  contained in the todosList service 
             todoLists_ids = get_todoLists_ids()
        all_todoLists = []
        for i in range(len(todoLists_ids)):
            todoLists_with_todos = list(filter(lambda todo: todo['id_list'] == todoLists_ids[i], TODOS))
            nameList = TODOSLIST[todoLists_ids[i]]
            todoLists_with_todos.insert(0, nameList)
            all_todoLists.insert(i,todoLists_with_todos)
        ---
        tags:
            - Flask API
        responses:
            200:
                description: JSON representing all the elements of the todosList service
        """  
   
        
        return {'data':TODOSLIST, 'status':200, 'message':'OK, successful HTTP request.'}



class TodoListManagementResourceByID(Resource):
    @token_required
    def get(current_user,self, todoList_id:int) -> List:
        
        """
        Return a TODOSLIST by ID contained in the todosList service 
        ---
        tags:
            - Flask API
        responses:
            200:
                description: JSON representing all the elements of the todosList service
        """  
        abort_if_todoList_doesnt_exist(todoList_id)

        for todolist in TODOSLIST:
            if todolist['id_list'] == todoList_id:
                todolist_wanted = todolist
        
        return {'data':todolist_wanted, 'status':200, 'message':'OK, successful HTTP request.'}

    @token_required
    def delete(current_user,self, todoList_id: int) -> Dict[str, Any]:
            """
            Delete a todoList in the todosList service and the todos of the list in the todos service
            ---
            tags:
                - Flask API
            parameters:
                - in: path
                name: todoList_id
                description: The id of the todoList to delete
                required: true
                type: string
            responses:
                200:
                    description: JSON representing the todos
                404:
                    description: The todo does not exist
            """
            abort_if_todoList_doesnt_exist(todoList_id)
            i = 0
            todos_ids = []
            indices = set()
            for i in range(len(TODOS)):
                if TODOS[i]['id_list'] == todoList_id:
                    indices.add(i)

            for i in sorted(indices, reverse=True):
                del TODOS[i]

            del TODOSLIST[todoList_id]

            return {'data':TODOSLIST, 'status':200, 'message': 'OK, successful HTTP request. TodoList deleted'}

    @token_required
    def put(current_user,self, todoList_id: int) -> Dict[str, Any]:

        """
        Create the content of a todoList in the todosList service
        ---
        tags:
            - Flask API
        parameters:
            - in: body
              name: attributes
              description: The name of the todoList to create
              schema:
                type: object
                required:
                    - name
                properties:
                  name:
                    type: string
        responses:
            201:
                description: JSON representing created todoList
            400:
                description: The parameters are missing or are not correct
        """
        body_parser = reqparse.RequestParser() 
        body_parser.add_argument('name', type=str, required=True, help="Missing the name of the task")
        args = body_parser.parse_args(strict=True) # Accepted only if this parameter is strictly declared in body else raise exception
        try:
            todo_Lists=get_todoLists_ids()
            id = getFirstMissingIDofTodoLists(todo_Lists)
            name = args['name']
            todo_List = {}
            todo_List['id_list'] = id
            todo_List['name_list'] = name
            TODOSLIST.insert(id, todo_List)
            return {'data':todo_List, 'status':201, 'message':'TodoList created'}
        except:
            abort(400)

    @token_required
    def patch(current_user,self,todoList_id) -> Dict[str, Any]:
        """
        Create the content of a todo in the todosList service
        ---
        tags:
            - Flask API
        parameters:
            - in: path
              name: todoList_id
              description: The id of the todoList to update
              required: true
              type: string
            - in: body
              name: attributes
              description: The updated name 
              schema:
                type: object
                properties:
                  name:
                    type: string
        responses:
            202:
                description: JSON representing updated todoList if new data has been given by the body
            400:
                description: The parameters are missing or are not correct
            404:
                description: The todo does not exist
        """
        abort_if_todoList_doesnt_exist(todoList_id)
        body_parser = reqparse.RequestParser()
        body_parser.add_argument('name_list', type=str, required=False, help="Missing the name of the task")
        args = body_parser.parse_args(strict=False)
        try:
            i = 0
            print(todoList_id)
            for todoList in TODOSLIST:               
                if (todoList['id_list'] != todoList_id):
                    i=i+1
                else:
                    break
            todoList_modified = TODOSLIST[i]
            name = args['name_list']
            if name != None:
                todoList_modified['name_list'] = name
            TODOSLIST[i] = todoList_modified
            print(todoList_modified['name_list'])
            return {'data':todoList_modified, 'status': 202, 'message': 'Updated todoList if new data has been given by the body'} # Accepted, updated or not if putting the same data
        except:
            abort(400)
        

def get_todoLists_ids() -> List[int]:
    return list(map(lambda todoLists: todoLists['id_list'],TODOSLIST))

def getFirstMissingIDofTodoLists(todoLists_ids) -> int:
    j = 0
    todoLists_ids.sort()
    for i in range(0,len(todoLists_ids)):
        if todoLists_ids[i] == j :
            j += 1
        else:
            break
    return j

def abort_if_todoList_doesnt_exist(todoList_id: int):
    todoLists_ids = get_todoLists_ids()
    if todoList_id not in todoLists_ids:
        abort(404,  message="Cannot find the TODO with id {}".format(todoList_id))
    