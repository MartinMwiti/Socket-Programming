* **Socket programming** is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server

### Server :
* A server has a ``bind()`` method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port.
* A server has a ``listen()`` method which puts the server into listen mode. This allows the server to listen to incoming connections. 
* A server has an ``accept()`` and ``close()`` method. The accept method initiates a connection with the client and the close method closes the connection with the client.
