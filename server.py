from xmlrpc.server import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler,DocXMLRPCServer,DocXMLRPCRequestHandler
import xmlrpc.client
from socketserver import ThreadingMixIn
import http.client
from urllib.parse import urlparse
class handler(DocXMLRPCRequestHandler):
    rpc_paths = ("/MyServerRpc",)
class MulThreadServer(ThreadingMixIn,DocXMLRPCServer):
    pass
server = MulThreadServer(("0.0.0.0",8000),requestHandler = handler,logRequests=True)
server.set_server_title("MY XML-RPC SERVER")
server.set_server_name("THIS XML-RPC SERVER CAN ACT AS HTTP PROXY TO TRANSFER HTTP REQUEST FOR CLIENT AND DO SOMETHINGS AWESOME !!!")
server.set_server_documentation("BELOW HERE IS SOME METHOD WE BUILD SO YOU CAN USE THEM !!!")
def execute_http(url,method,headers,body):
    """
    This function is use to get request from client demand and return for them the response 
    """
    try:
        execute_url = urlparse(url)
        if execute_url.scheme == "https":
            conn = http.client.HTTPSConnection(execute_url.netloc, timeout=10)
        else:
            conn = http.client.HTTPConnection(execute_url.netloc,timeout=10)
        path = execute_url.path or "/"
        if execute_url.query:
            path += "?" + execute_url.query
        if isinstance(body,str):
            body = body.encode('utf-8')
        conn.request(method,path, body=body, headers=headers)
        response = conn.getresponse()
        raw_content = response.read()
        try:
            content = raw_content.decode('utf-8')
        except UnicodeDecodeError:
            content = f"Response maybe not string , Size: {len(raw_content)} bytes"
        headers_response = dict(response.getheaders())
        conn.close()
        return{
            "status_code":response.status,
            "headers" : headers_response,
            "content" : content
        }
    except Exception as e:
        return {'status_code': 500,
                'headers':{} ,
                'content': f"Internal Server Error: {str(e)}"
        }
server.register_function(execute_http,"execute_http")
print("SERVER ARE WAITING......")
server.serve_forever()
