# fastAPI_with_chat

# Project Overview

    The project is a FastAPI-based chat application that allows users to register, log in, and engage in real-time conversations. It utilizes JWT (JSON Web Tokens) for user authentication and leverages SQLAlchemy for database interactions. The application includes functionalities for user management and chat features.

# Key Features
User Registration and Authentication:

Users can sign up with a unique username and password.
Passwords are securely hashed before being stored in the database.
Users can log in to the application, generating an access token that is used for subsequent authenticated requests.
Token-Based Authentication:

Uses JWT for managing user sessions.
Upon logging in, an access token is generated and stored as an HTTP-only cookie, enhancing security.
Chat Functionality:

Users can navigate to a chat page after logging in, where they can initiate and participate in conversations.
Chat functionality allows users to send and receive messages, enabling real-time communication.
Database Integration:

Utilizes SQLAlchemy for ORM (Object Relational Mapping) to interact with the database.
The database stores user information and chat history, ensuring data persistence.
Web Interface:

The application uses Jinja2 templates for rendering HTML pages.
The front end is designed to provide a user-friendly interface for login and chat interactions.
Routing Structure:

The application is structured using routers to organize routes for authentication (auth), chat functionality (chat), and other application features.
Each module (like auth, routes, and chat) has its own routing logic to maintain clean and manageable code.

# Technologies Used

FastAPI: For building the web framework and managing routes.
SQLAlchemy: For ORM and database interactions.
Jinja2: For rendering HTML templates.
JWT (JSON Web Tokens): For secure user authentication and session management.
HTML/CSS: For creating the front-end user interface.


# Project Structure

The project has a modular structure, which helps in organizing code effectively:

main.py: The entry point for the FastAPI application where routers are included, and the application is configured.
auth.py: Contains routes and logic for user authentication (registration and login).
routes.py: Manages the chat routes and user interactions.
chat: Directory for static files and templates, enhancing the user interface.
database.py: Handles database connection and configuration.
models.py: Defines the data models (like User) for the database.
hashing.py: Contains functions for password hashing and verification.

# Use Case

This project can be used in various scenarios, including:

Real-Time Communication: It can serve as a platform for users to communicate in real-time.
Chat Applications: The core functionality can be extended to support group chats, private messaging, or integration with other applications.





# FILE STRUCTURE

FastAPI_with_Chat/
│
├── main/
│   ├── templates/
│   │   ├── base.html         # Base template
│   │   ├── signup.html       # Signup page
│   │   ├── login.html        # Login page
│   │   └── chat.html         # Chat interface
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css    # Custom CSS (optional)
│   │   ├── js/
│   │   │   └── chat.js       # JavaScript for chat WebSockets
│   ├── main.py               # FastAPI entry point
│   ├── models.py             # Database models
│   ├── schemas.py            # Pydantic schemas
│   ├── auth.py               # Authentication (JWT)
│   ├── chat.py               # WebSocket chat logic
│   ├── utils.py              # Utility functions (password hashing, JWT helpers)
│   └── database.py           # Database connection setup
│   └── hashing.py            # Hashing for password
├── requirements.txt          # Python dependencies
└── .env                      # Environment variables (secret keys)
