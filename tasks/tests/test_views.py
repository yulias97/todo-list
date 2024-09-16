from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag, Task

INDEX_URL = reverse("tasks:index")
TAG_LIST_URL = reverse("tasks:tag-list")


class TaskViewTests(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="test")
        self.task = Task.objects.create(
            content="Do something importent",
            created_at="2023-03-12",
            is_done=False
        )
        self.task.tags.set(Tag.objects.all())

    def test_retrieve_task_list(self) -> None:
        response = self.client.get(INDEX_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks),
        )
        self.assertTemplateUsed(response, "tasks/task_list.html")


class TagViewTest(TestCase):
    def setUp(self):
        Tag.objects.create(name="Test")

    def test_retrieve_tag_list(self) -> None:
        response = self.client.get(TAG_LIST_URL)
        self.assertEqual(response.status_code, 200)
        tags = Tag.objects.all()
        self.assertEqual(
            list(response.context["tag_list"]),
            list(tags),
        )
        self.assertTemplateUsed(response, "tasks/tag_list.html")
