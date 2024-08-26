# Python Socket Programming

### Description of this Program

This program allows two terminals to communicate with each other using socket programming in Python. It consists of two main components: the server and the client. The server listens for incoming connections, while the client connects to the server. Both components can send and receive messages, enabling a real-time chat between the terminals.

#### Server:
1. **Imports the Socket Library**: Utilizes the `socket` library to create and manage network connections.
2. **Creates a Socket**: Initializes a socket object with IPv4 addressing (`AF_INET`) and TCP protocol (`SOCK_STREAM`).
3. **Binds the Socket**: Associates the socket with a specific IP address (`localhost`) and port (`12345`).
4. **Listens for Connections**: Configures the socket to listen for incoming connections from clients.
5. **Accepts Connections**: Waits for a client to connect, then establishes a connection.
6. **Handles Communication**: In a loop, the server receives messages from the client, displays them, and sends responses back to the client.
7. **Closes the Connection**: Ends the connection when communication is complete.

#### Client:
1. **Imports the Socket Library**: Utilizes the `socket` library to create and manage network connections.
2. **Creates a Socket**: Initializes a socket object with IPv4 addressing (`AF_INET`) and TCP protocol (`SOCK_STREAM`).
3. **Connects to the Server**: Establishes a connection to the server running on `localhost` at port `12345`.
4. **Handles Communication**: In a loop, the client sends messages to the server, receives responses, and displays them.
5. **Closes the Connection**: Ends the connection when communication is complete.

### Multi-Client Handling (Advanced):
For handling multiple clients, the server uses threading:
1. **Threaded Client Handling**: Each client connection is managed in a separate thread, allowing concurrent communication with multiple clients.
2. **Server Loop**: Continuously accepts new client connections and starts a new thread for each one.

### Running the Program:
1. **Start the Server**: Run the server script in one terminal.
2. **Start the Client**: Run the client script in another terminal.
3. **Chat**: Type messages in the client terminal to send them to the server and vice versa.

This program demonstrates the fundamentals of socket programming in Python, enabling real-time text-based communication between two terminals.