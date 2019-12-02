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
(https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) ?

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
(https://www.digitalocean.com/community/tutorials/how-to-configure-a-continuous-integration-testing-environment-with-docker-and-docker-compose-on-ubuntu-14-04)
Simplifies building, testing and pushing.
Flow:
- docker-compose build
- docker-compose up # Start service(s) with arguments and environment variables from docker-compose.yml
- Test with curl and netbrowser if working
  - docker-compose exec <serviceName> pytest # If running
  - docker-compose run <serviceName> pytest # If not running
  - docker-compose exec <serviceName> sh # If you want an interactiv shell in running container. You  can use vi on sh
- docker-compose down # Stop and cleanup, often you can do a new build without a cleanup
- Repet steps above untill all tests pass
- docker-compose push # Push to personal dockerhub repository

Shell scripts need to be made executable: git update-index --add --chmod=+x <shell-script>

## Test with Postman
- Use a local-dev environment for local testing of container {{BASE_URL}} e.g. http://localhost:5000
- Use a <node-systemName>-dev environment with JWT authentication (JWT token in collection Authorization environment? ) {{BASE_URL}} e.g. https://<dev-node-cloud-url>/api/system/<systemName>/proxy/<endpoint>
- Remember that transforms and sinks expect POST and JSON lists. All, including source (GET) must return JSON list with "Content-Type: application/json".

## Test connector in Sesam
Test in personal Sesam dev node.
- Add service to node as microservice with docker image from personal dockerhub repository
- Add test pipe(s) using service
- Test with sesam (sync) client ??

## Sesam community use Travis CI
https://github.com/sesam-community/guidelines
https://docs.travis-ci.com/user/docker/
Shell scripts need to be made executable: git update-index --add --chmod=+x <shell-script>

## Quality assurance before production
- Only qualified developers can accept a pull request to master on production git repository