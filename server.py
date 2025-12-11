from xmlrpc.server import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler,DocXMLRPCServer,DocXMLRPCRequestHandler
import requests
import xmlrpc.client
class handler(DocXMLRPCRequestHandler):
    rpc_paths = ("/MyServerRpc")
server = DocXMLRPCServer(("localhost",8000),requestHandler = handler,logRequests=True)
server.set_server_title("MY XML-RPC SERVER")
server.set_server_name("THIS XML-RPC SERVER CAN ACT AS HTTP PROXY TO TRANSFER HTTP REQUEST FOR CLIENT AND DO SOMETHINGS AWESOME !!!")
server.set_server_documentation("BELOW HERE IS SOME METHOD WE BUILD SO YOU CAN USE THEM !!!")
def execute_http(url,method,headers,body):
    """
    This function is use to get request from client demand and return for them the response 
    """
    try:
        response = requests.request(
           method = method,
           url = url,
           headers = headers,
           data = body     
        )
        return {
            'status_code' : response.status_code,
            'headers' : dict(response.headers),
            'content' : xmlrpc.client.Binary(response.content)
        }
    except Exception as e:
        return {'status_code': 500,'headers':{} ,'content': xmlrpc.client.Binary(str(e).encode())}
server.register_function(execute_http,"execute_http")
print("SERVER ARE WAITING......")
server.serve_forever()