# Sprout exercise

## Project requirements

- docker
- docker-compose
- makefile command

## Running this project

`docker-compose up` 

or

`make run`

And naviagate to:

Exercise API:
http://localhost:5000/docs

ML API:
http://localhost:5001/docs

## Running tests

`docker-compose run backend bash -c "pytest"`

or 

`make test`

## Notes

Project layout inspired by:
https://github.com/tiangolo/full-stack-fastapi-postgresql

### API

I choose fastapi for this project as I like the data serialization and auto documentation functionality. It is also un-opinionated so I can structure my code how I want to. I did think about making this async to take advantage of the performance benefits of fastapi but as I wanted to be quick and avoid any
3rd party async issues I choose to write synchronous code so fastapi would use
threads instead of co-routines. 

For this project I wanted to experiment and try an example template project structure. I want to keep my logic de-coupled so I can move and re-use it if I want to. I'm a fan of hexagional architecture a domain driven pattern (similar to onion architecture) and use that for personal projects. I didn't use it here as it does come with more abstractions than we need for this project.

Feel free to have a look here:
https://github.com/jwnwilson/authorizer#domain-driven-development

### ML service

I setup the ML service as another fastapi service and joined them with docker. I don't like running jobs with the potential to be slow directly on an API and would usually break this off onto background processs with event driven architecture. This is so the system is robust and can handle slowdown or spikes in demand gracefully.

### Testing

I tend to follow the testing trophy approach of more integrations tests, static typing with mypy and typescript. This allows me to work "outside in" and test features first then build confidence with unit tests once the implementation has been completed.

You can see that on this project, I could have done TDD and built the requests first if I wanted to. I tend to use TDD for bugs as they are a great way to replicate the issue and then the regression test exists.

I also use cypress for E2E testing in professional projects.

Looking forward to hearing your feedback.




