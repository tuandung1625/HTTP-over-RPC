import xmlrpc.client
import json

proxy = xmlrpc.client.ServerProxy("http:/192.168.1.13:8000/MyServerRpc")

def get_valid_input(prompt, func):  
    while True:
        user_input = input(prompt).strip()
        try:
            return func(user_input)
        except ValueError as e:
            print(f"Error: {e}. Try again")

def check_url(text):
    if not text.startswith("http"):
        raise ValueError("URL must start with http or https")
    return text

def check_method(text):
    result = text.upper()
    valid_methods = {"GET","POST","PUT","DELETE"}
    if result not in valid_methods:
        raise ValueError(f"Method must be one of: {valid_methods}")
    return result

def check_header(text):
    if text == "":
        return {}
    
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        raise ValueError("Header must have a valid JSON format")
    
    if not isinstance(data,dict):
        raise ValueError("Header must be a dict type")
    return data  

def client_main():
    print("------ PREPARING REQUEST ------\n")
    url = get_valid_input("Enter URL: ",check_url)
    method = get_valid_input("Enter method: ",check_method)
    header = get_valid_input("Enter header: ",check_header)
    body = ""
    if method in ["POST","PUT"]:
        body = input("Enter body load: ").strip()
    else:
        print(f"Skip body for {method}")

    print(f"Sending {method} request to server...........")

    try:
        response = proxy.execute_http(url,method,header,body)

        print("\n------ RESPONSE FROM SERVER ------")
        print(f"Status: {response.get('status_code')}")
        print(f"Content: {response.get('content')}")
        print('------ FINISH RESPONSE ------')
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    client_main()
