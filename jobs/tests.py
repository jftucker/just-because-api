from django.test import TestCase
from django.contrib.auth.models import User

from .models import Job


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        testuser2 = User.objects.create_user(
            username='testuser2', password='abc123')
        testuser2.save()
        
        test_job = Job.objects.create(
            author = testuser1, 
            title='Test', 
            description ='Content...',
        )
        test_job.workers.add(User.objects.get(id=1))
        test_job.save()

    def test_job_content(self):
        job = Job.objects.get(id=1)
        expected_author = f'{job.author}'
        expected_title = f'{job.title}'
        expected_description = f'{job.description}'
        expected_workers = f'{job.workers}'

        print('this:', User.objects.get(id=1))

        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'Test')
        self.assertEqual(expected_description, 'Content...')
        self.assertEqual(expected_workers, 'auth.User.None')