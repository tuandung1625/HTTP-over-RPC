import xmlrpc.client
import json
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/MyServerRpc")
try:
    response=proxy.execute_http("https://jsonplaceholder.typicode.com/todos/1","GET",{},"")
    print("Connect successfull !! Status:", response['status_code'])
except Exception as e:
    print("OUR SERVICE HAVE SOME ERROR !!")
    print("LOG FOR ERROR : ",e)

print("Status : ",response['status_code'])
content = response['content']
print(content)
my_message = {'name':'tuan'}
make_message_to_string = json.dumps(my_message)
my_headers = {'Content-Type': 'application/json'}
test = proxy.execute_http("https://jsonplaceholder.typicode.com/posts","POST",my_headers,make_message_to_string)
print("Status for post method : ",test['status_code'])