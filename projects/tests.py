

from rest_framework.test import APITestCase

from projects.models import Project
from users.models import User
from django_seed import Seed

seeder = Seed.seeder()


class ProjectsRelationWithUsersQueryTest(APITestCase):
    def setUp(self):
        self.project_owner = User(email='project@manager.co')
        self.project_owner.set_password('Po@12345')
        self.project_owner.is_manager = True
        self.project_owner.save()
        seeder.add_entity(User, 20)
        user_pks = seeder.execute()
        self.project = Project.objects.create(title='TEST PROJ', manager=self.project_owner,
                                              budget=1000.0, description='test project')
        all_users = User.objects.all()
        for user in all_users:
            self.project.developers.add(user)
        self.headers = self.headers = {
            'Content-Type': 'application/json',
        }
        res = self.client.post('/api/login/', data={'email': 'project@manager.co', 'password': 'Po@12345'},
                               **self.headers)

        self.headers.update({
            'HTTP_AUTHORIZATION': f'Bearer {res.json().get("access")}',
        })

    def test_num_of_query(self):
        with self.assertNumQueries(4):
            self.client.get(path=f'/api/projects/{self.project.id}/', **self.headers)
