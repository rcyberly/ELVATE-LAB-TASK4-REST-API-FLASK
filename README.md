A clean and powerful RESTful API built using Python and Flask, designed to manage user data with full CRUD functionality. This project demonstrates how to build scalable endpoints, handle JSON requests, and maintain in-memory data structures — perfect for learning, prototyping, or showcasing backend skills.
CURL TESTING :


## 🧪 Sample Curl Commands

```bash
# Create a user
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{"id":1,"name":"Rajinder"}'

# Get all users
curl http://localhost:5000/users

# Get a specific user
curl http://localhost:5000/users/1

# Update a user
curl -X PUT http://localhost:5000/users/1 \
-H "Content-Type: application/json" \
-d '{"name":"Rajinder Singh"}'

# Delete a user
curl -X DELETE http://localhost:5000/users/1
