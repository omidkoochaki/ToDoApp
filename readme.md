# ToDoApp

## Description
Users first sign up as `developers`. Admin can make them `manager`.
### Managers can:
- Create a new project and add developers to that.
- Add tasks to the projects and assign them to developers (if a developer is not previously added to the project, will be added when the manager assigns task to him/her)

### Developers can:
- Add tasks to the projects and assign them just to themselves.
- See all tasks assigned to them or not.


### Deployment:
use the below docker-compose command to deploy the project:
`docker-compose up -d --build`


### Documentation URL:
Docs URL:
`http://localhost:8000/`


## Next Step Ideas:
### add an Email Service
Email service should work in background using `Celery`, the email service purposes will be:
- notify project manager when a task status changes
- notify the manager when a project is defined
- notify the developers when a task assigns to them, or they are added to a project
- verify email address on sign up

all email service call APIs should protect against DoS attacks using `Throttling`.



