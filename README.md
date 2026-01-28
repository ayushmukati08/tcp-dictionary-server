# TCP Dictionary Server using NLP (WordNet)

## Overview
This project implements a **client–server dictionary application** using **TCP socket programming in Python**.
The server uses **NLTK’s WordNet** lexical database to fetch definitions of words requested by multiple clients concurrently.

The main focus of this project is to demonstrate:
- Client–server communication using TCP
- Multithreading on the server side
- Basic use of NLP resources (WordNet)
- Clean protocol handling and input validation

This project is suitable as an **academic level networking + NLP foundation project**.

---

## Features
- TCP-based client–server architecture
- Multithreaded server (handles multiple clients simultaneously)
- Word definition lookup using WordNet
- Graceful client disconnection using a command-based protocol
- Client-side input validation to prevent invalid requests
- Simple, readable, and modular code structure

---

## Technologies Used
- **Python 3**
- **Socket Programming (TCP/IP)**
- **Multithreading**
- **NLTK (WordNet corpus)**

---

## Project Structure
```
.
├── server.py        # Multithreaded TCP server
├── client.py        # TCP client for user interaction
└── README.md        # Project documentation
```

---

## How It Works

### Server Side
- Listens on a TCP port (`localhost:9999`)
- Accepts incoming client connections
- Spawns a new thread for each connected client
- Receives a word from the client
- Fetches its definition using WordNet
- Sends the definition back to the client
- Closes the connection gracefully when the client sends `__exit__`

### Client Side
- Connects to the server over TCP
- Takes word input from the user
- Prevents empty input from being sent
- Sends valid words to the server
- Displays the received definition
- Terminates connection cleanly on `exit`

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Install Required Dependencies
```bash
pip install nltk
```

### 3. Download WordNet Data (Run Once)
```python
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
```

---

## Running the Project

### Step 1: Start the Server
```bash
python server.py
```

### Step 2: Run the Client
```bash
python client.py
```

### Step 3: Use the Application
```
Enter word (exit to quit): computer
Meaning: a machine for performing calculations automatically
```

---

## Limitations
- Uses only the most common WordNet meaning of a word
- Does not handle contextual word sense disambiguation
- TCP message handling is kept simple using delimiters
- No persistent storage or logging

These limitations are intentional to keep the project focused and understandable.

---

## Future Scope
- Improve word sense selection using part-of-speech tagging
- Accept full sentences instead of single words
- Rank multiple meanings instead of returning only the first one
- Add basic logging (queries, response time)
- Introduce a structured message format (e.g., JSON)

---

## Learning Outcomes
- Understanding of TCP socket communication
- Practical experience with multithreaded servers
- Exposure to NLP resources like WordNet
- Clear separation of client-side and server-side responsibilities
- Handling real-world networking edge cases

---

## Author
**Ayush Mukati**  
MCA (Master of Computer Applications)
National Institute of Technology Patna
---

## License
This project is intended for academic and learning purposes.
