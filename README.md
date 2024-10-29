# IITBBS General Championship Hackathon - Team 31 - PS02 Backend

This is the backend service developed by Team 31 for Problem Statement 02 during the IIT Bhubaneswar General Championship Hackathon.

## Tech Stack
- Python FastAPI backend
- PostgreSQL database
- Asyncpg for async database operations

## Key Features
- User authentication with email/password
- Role-based access control
- Question and reply functionality
- Async database operations for better performance
- Input validation and error handling
- Connection pooling for database efficiency

## Getting Started

### Prerequisites
- Python 3.x
- PostgreSQL
- pip

### Environment Variables
```bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=testdb
DB_USER=testuser
DB_PASSWORD=test
CONNECTION_TIMEOUT=10
QUERY_TIMEOUT=60

### Database Configuration

- Minimum connections: 5
- Maximum connections: 100
- Connection timeout: 10 seconds (configurable)
- Query timeout: 60 seconds (configurable)
- Max inactive connection lifetime: 480 seconds

## API Endpoints
### User Management
- Signup
- Login 
- Update user information

### Questions
- Create questions
- Update questions

### Replies
- Create replies

## Team Members
- [Amrit](https://github.com/ad451)
- [Omkar](https://github.com/og118)
- [Pranav](https://github.com/npv12)