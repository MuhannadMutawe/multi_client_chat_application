# Multi-Client Chat Application 💬

A real-time multi-client chat application built with **Python**, using **Sockets**, **Threading**, and a simple **Tkinter GUI**.  
This project demonstrates how to create a basic client-server architecture where multiple users can connect and communicate simultaneously.

---

## 🚀 Features

- ✅ Multi-client support using Python threads
- ✅ Real-time message broadcasting
- ✅ Graphical User Interface (GUI) with Tkinter
- ✅ Nickname system for users
- ✅ Automatic join/leave notifications
- ✅ Enter key support for sending messages
- ✅ Graceful client disconnection handling
- ✅ Lightweight and beginner-friendly networking project

---

## 🛠️ Technologies Used

- **Python 3**
- **Socket Programming**
- **Threading**
- **Tkinter GUI**

---

## 📂 Project Structure

```bash
multi_client_chat_application/
│
├── server.py     # Chat server
├── client.py     # Chat client with GUI
└── README.md
```

---

## ⚙️ How It Works

### Server

- Listens for incoming client connections
- Handles multiple clients using threads
- Broadcasts messages to all connected users
- Detects disconnections automatically

### Client

- Connects to the server
- Opens a GUI chat window
- Sends and receives messages in real-time
- Displays chat history dynamically

---

## 📸 Preview

### Chat Client Interface

```text
+----------------------------------+
|        Chat Room                 |
+----------------------------------+
| User1: Hello                     |
| User2: Hi there!                 |
|                                  |
+----------------------------------+
| Type your message here...        |
+----------------------------------+
|            Send                  |
+----------------------------------+
```

---

## 🔧 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/multi-client-chat-application.git
cd multi-client-chat-application
```

---

### 2️⃣ Run the Server

```bash
python server.py
```

Server will start listening on:

```python
HOST = "127.0.0.1"
PORT = 55555
```

---

### 3️⃣ Run the Client

Open another terminal:

```bash
python client.py
```

Run multiple clients to simulate a real chat room.

---

## 🧠 Concepts Practiced

This project helps in understanding:

- TCP Socket Programming
- Client-Server Architecture
- Multithreading in Python
- GUI development with Tkinter
- Real-time communication systems

---

## 📌 Future Improvements

- 🔐 Add encryption for messages
- 🌍 Support remote connections
- 🎨 Improve GUI design
- 🟢 Online users list
- 💾 Chat history storage
- 📁 File sharing support
- 😊 Emoji support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## ⭐ Show Your Support

If you like this project:

- 🌟 Star the repository
- 🍴 Fork it
- 📢 Share it with others

---

## 📜 License

This project is open-source and available under the MIT License.
