# Social Media API

A Django REST Framework–based Social Media API with token authentication.

## Features
- Custom user model
- Token-based authentication
- User registration & login
- User profile management
- Followers/following system (foundation)

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

Posts Endpoints
Endpoint	Method	Description
/api/posts/	GET	List posts (paginated)
/api/posts/	POST	Create post
/api/posts/{id}/	GET	Retrieve post
/api/posts/{id}/	PUT/PATCH	Update post (owner only)
/api/posts/{id}/	DELETE	Delete post (owner only)
Comments Endpoints
Endpoint	Method	Description
/api/comments/	GET	List comments
/api/comments/	POST	Create comment
/api/comments/{id}/	PUT/PATCH	Update comment
/api/comments/{id}/	DELETE	Delete comment
