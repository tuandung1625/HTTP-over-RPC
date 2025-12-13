import xmlrpc.client
import json

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/MyServerRpc")

try:
    response = proxy.execute_http("https://jsonplaceholder.typicode.com/todos/1", "GET", {}, "")
    print("GET Status:", response['status_code'])
except Exception as e:
    print("GET REQUEST ERROR:", e)

print("Please enter data to send to the server: ")
user_name = input("Enter name: ")
age = input("Enter age:")
user_major = input("Enter major:")

my_mess = {
    'name': user_name,
    'age':age,
    'job': user_major
}

convert_2_jsStr = json.dumps(my_mess)
header = {'Content-type': 'application/json'}

try:
    test = proxy.execute_http("https://jsonplaceholder.typicode.com/posts", "POST", header, convert_2_jsStr)

    print("Status for POST method : ", test['status_code'])
    print("Response content:", test['content'])
except Exception as e:
    print("POST REQUEST ERROR: ", e)