# HTTP Proxy over XML-RPC

This project implements a lightweight HTTP proxy system using Python's standard `xmlrpc` library. It acts as a bridge, allowing a client to send HTTP request specifications (URL, method, headers, body) to a server via XML-RPC. The server then executes the actual HTTP request to the target destination and returns the response details to the client.

## Project Overview

The system consists of two main components:

1.  **The Server:** A multithreaded XML-RPC server that exposes a remote procedure to execute HTTP requests. It utilizes `http.client` to connect to external URLs.
2.  **The Client:** An interactive command-line interface (CLI) that prompts the user for request details, validates the input, and transmits the request to the server.

## Features

* **Multithreading:** Uses `ThreadingMixIn` to handle multiple client requests concurrently.
* **Protocol Support:** Supports both HTTP and HTTPS targets.
* **Method Support:** Handles standard HTTP methods including GET, POST, PUT, and DELETE.
* **Header Customization:** Allows users to inject custom headers via JSON input.
* **Self-Documenting:** The server is built on `DocXMLRPCServer`, making documentation accessible via a web browser when the server is running.
* **Zero External Dependencies:** Built entirely using Python standard libraries.

## Requirements

* Python 3.6 or higher.
* Network connectivity (for the server to reach external URLs).

## Architecture

The data flow operates as follows:

1.  **User Input:** The user provides the target URL, HTTP method, headers, and body via the `client.py` terminal.
2.  **RPC Call:** The client wraps this data and sends an XML-RPC request to the server endpoint (`/MyServerRpc`).
3.  **Execution:** The server parses the URL, establishes a connection using `http.client`, and sends the request to the internet.
4.  **Response Relay:** The server captures the status code, headers, and content from the external site and returns them as a dictionary to the client.

## Installation

No installation of external packages is required. Ensure you have Python installed.

1.  Clone the repository or download the source files.
2.  Ensure you have the following two files:
    * `server.py` (Contains the `MulThreadServer` and request handler)
    * `client.py` (Contains the interactive CLI)
