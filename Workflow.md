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

## Git
(https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) ??
Development:
- Personal sesam github account for development.
- E.g. integrated git workflow in Visual Studio Code
- New branch for new features

Production:
- Pull request to https://github.com/sesam-community or https://github.com/datanav or eqvivalent to customer system

## Dockerfile
Instructions to build the service

## Tests
Test driven development with pytest

(https://flask.palletsprojects.com/en/1.1.x/testing/)
(https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)


## Docker-compose
Simplifies building, testing and pushing.
Flow:
- docker-compose build
- docker-compose up # Start service(s) with arguments and environment variables from docker-compose.yml
- Test with curl and netbrowser if working
  - docker-compose exec <serviceName> pytest # If running
  - docker-compose run <serviceName> pytest # If not running
  - docker-compose exec <serviceName> sh # If you want an interactiv shell in running container. You  can use vi on sh
- docker-compose down # Stop and cleanup
- Repet steps above untill all tests pass
- docker-compose push # Push to personal dockerhub repository

## Test connector in Sesam
Test in personal Sesam dev node.
- Add service to node as microservice with docker image from personal dockerhub repository
- Add test pipe(s) using service
- Test with sesam (sync) client ??

## Quality assurance before prouction
- Only qualified developers can accept a pull request to master on production git repository