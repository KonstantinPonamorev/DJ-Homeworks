import random

import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user('admin')


@pytest.fixture
def url():
    return '/api/v1/courses/'


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, url, course_factory):
    course = course_factory()

    response = client.get(url + f'{course.pk}/')

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course.name


@pytest.mark.django_db
def test_get_courses(client, url, course_factory):
    courses = course_factory(_quantity=20)

    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_get_course_by_id(client, url, course_factory):
    courses = course_factory(_quantity=20)
    index = random.randrange(0, len(courses) - 1)
    course = courses[index]

    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data[index]['name'] == course.name


@pytest.mark.django_db
def test_get_course_by_name(client, url, course_factory):
    courses = course_factory(_quantity=20)
    index = random.randrange(0, len(courses) - 1)
    course = courses[index]

    response = client.get(url + f'?name={course.name}')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course.name


@pytest.mark.django_db
def test_create_course(client, url):
    count = Course.objects.count()
    name = 'Test text'

    response = client.post(url, data={'name': name})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert Course.objects.first().name == name


@pytest.mark.django_db
def test_update_course(client, url, course_factory):
    course = course_factory()
    updated_name = 'New name'

    response = client.patch(url + f'{course.pk}/', data={'name': updated_name})

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == updated_name


@pytest.mark.django_db
def test_delete_course(client, url, course_factory):
    course = course_factory()
    count = Course.objects.count()

    response = client.delete(url + f'{course.pk}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1