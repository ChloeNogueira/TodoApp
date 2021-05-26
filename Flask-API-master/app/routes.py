from app import api

from app.resources.helloworld import HelloWorldResource, HelloWorldResourceNameToken, HelloWorldResourceNameURL, HelloWorldResourceNames
from app.resources.account import AccountResource
from app.resources.login import LoginResource
from app.resources.todos import TodoManagementResource, TodoManagementResourceByID, TodosListManagementResource
from app.resources.todoslist import TodoListManagementResourceByID, TodoListManagementResource

# Hello World
api.add_resource(HelloWorldResource, '/api/helloworld')
api.add_resource(HelloWorldResourceNameToken, '/api/hello')
api.add_resource(HelloWorldResourceNameURL, '/api/hello/<string:name>')
api.add_resource(HelloWorldResourceNames, '/api/hello/<int:count>')

# Create an account
api.add_resource(AccountResource,'/api/account')

# Login
api.add_resource(LoginResource, '/api/login')

# Todos app



#api.add_resource(TodoManagementResourceByID, '/api/todos/<int:todo_id>')

api.add_resource(TodoManagementResourceByID, '/api/lists/todos/<int:todoList_id>/<int:todo_id>')

api.add_resource(TodosListManagementResource, '/api/lists/todos/<int:todoList_id>')

api.add_resource(TodoListManagementResourceByID, '/api/lists/<int:todoList_id>')

api.add_resource(TodoListManagementResource, '/api/lists')

