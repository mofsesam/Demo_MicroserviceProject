# Sesam connector with python and Flask

## File structure
Copy a template. (Can make a yeoman generator)
```
<project>
│   .gitignore
│   README.md
│   Dockerfile
│   docker-compose.yml
│
└───service
│   │   <connectorName>.py
│   │   requirements.txt
│   │   __init__.py
│   │
│   └───tests
│       │   conftest.py
│       │   pytest.ini
│       │   test_<connectorName>.py 
│       └───functional 
│       │   │   ...
│       │   │   ...
│       │
│       └───unit
│       │   │   ...
│       │   │   ...
│   
└───folder2
    │   file021.txt
    │   file022.txt
```

## Dockerfile
Instructions to build the service

## Tests
Test driven development with pytest

## Docker-compose
Simplifies building, testing and pushing.
Flow:
- docker-compose build
- docker-compose up # Start service(s) with arguments and environment variables from docker-compose.yml
- Test with curl and netbrowser if working
- docker-compose exec <serviceName> pytest / docker-compose run <serviceName> pytest
- docker-compose down # Stop and cleanup
- Repet steps above untill all tests pass
- docker-compose push # Push to personal dockerhub repository

