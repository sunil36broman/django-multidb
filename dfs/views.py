# from django.shortcuts import render

# Create your views here.

#./todo/views.py

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Customer, Pasenger
from django.db import connections
# from . serializers import TodoSerializer
# from rest_framework.views import APIView
# from django.contrib.auth.decorators import permission_required
# from rest_framework.permissions import IsAuthenticated
# from django.utils.decorators import method_decorator

# Create your views here.

class DBooksListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # pass
    # @method_decorator(login_required)
    # @method_decorator(permission_required('todo.view_todo', raise_exception=True))
    # @method_decorator(permission_required(('todo.view_todo','todo.change_todo'), raise_exception=True))
    # @method_decorator(permission_required('todo.view_todo', raise_exception=True))
    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get(self,request):
        
        customerr = Customer.objects.all()
        pasenger = Pasenger.objects.all()

        
      
        print("customerr-rrrrr-",customerr)
        print("pasenger-rrrrr-",pasenger)

        

        # with connections['books_db'].cursor() as cursor:
        #     cursor.execute("SELECT * FROM department")
        #     data=self.dictfetchall(cursor)
        #     print(data)

        with connections['dfs_db'].cursor() as cursor:
            cursor.execute("SELECT * FROM customer")
            data=self.dictfetchall(cursor)
            print(data)    
        # serializer = TodoSerializer(todos, many=True)
        return Response({'data':"value"})

class DBooksDetailAPIView(APIView):
    pass
    # @method_decorator(permission_required('todo.view_todo', raise_exception=True))
    # def get(self,request,pk):
    #     todos = Todo.objects.get(id=pk)
    #     serializer = TodoSerializer(todos, many=False)
    #     return Response(serializer.data)

# class CreateTodoAPIView(APIView):

#     # @permission_required('todo.add_todo', raise_exception=True)
#     @method_decorator(permission_required('todo.add_todo', raise_exception=True))
#     def post(self,request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class UpdateTodoAPIView(APIView):

#     # @permission_required('todo.change_todo', raise_exception=True)
#     @method_decorator(permission_required('todo.change_todo', raise_exception=True))
#     def post(self,request,pk):
#         todo = Todo.objects.get(id=pk)
#         serializer = TodoSerializer(instance=todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

# class ApprovedTodoAPIView(APIView):

#     # @permission_required('todo.change_todo', raise_exception=True)
#     @method_decorator(permission_required('todo.todo_approved', raise_exception=True))
#     def get(self,request,pk):
#         # todo = Todo.objects.get(id=pk)
#         # serializer = TodoSerializer(instance=todo, data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         return Response({"serializer.data":"ddsdsd"})

# class DeleteTodoAPIView(APIView):

#     # @permission_required('todo.delete_todo', raise_exception=True)
#     @method_decorator(permission_required('todo.delete_todo', raise_exception=True))
#     def get(self,request,pk):
#         todo = Todo.objects.get(id=pk)
#         todo_instance = Todo.objects.get(id=pk)
#         todo_instance.delete()
#         return Response('Deleted')
