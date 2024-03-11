from django.test import TestCase

from tasks.models import Tag, Task


class ModelsTest(TestCase):
    def test_tag_str(self) -> None:
        tag = Tag.objects.create(name="Test")
        self.assertEqual(str(tag), tag.name)

    def test_task_str(self) -> None:
        task = Task.objects.create(
            content="Do something importent",
            created_at="2023-03-12",
            is_done=False
        )
        self.assertEqual(
            str(task),
            task.content
        )
