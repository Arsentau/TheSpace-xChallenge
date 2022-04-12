from django.test import TestCase
from . import queries

class Test_queries_builders(TestCase):
    def test_todo_query(self):
        name = "Short Title"
        description = "This is the description"
        result = queries.set_todo_query(name, description)
        self.assertEqual(result.get('name'), name)
        self.assertEqual(result.get('desc'), description)
        self.assertEqual(result.get('pos'), "bottom")
    
    def test_type_error_todo_query(self):
        with self.assertRaises(TypeError):
            result = queries.set_todo_query()
    
    def test_bug_query(self):
        description = "This is the description"
        members = [
            {
                "id": "987654321",
                "fullName": "Test User",
                "username": "testuser"
            },
            {
                "id": "654987321",
                "fullName": "Test User 1",
                "username": "testuser1"
            },
            {
                "id": "123456789",
                "fullName": "Test User 2",
                "username": "testuser2"
            }
        ]
        result = queries.set_bug_query(description, members)
        idMembers = result.get('idMembers')
        self.assertEqual(result.get('desc'), description)
        self.assertTrue(idMembers[0] == members[0].get("id") or idMembers[0] == members[1].get("id") or idMembers[0] == members[2].get("id"))
    
    def test_task_query(self):
        name = "This is the title"
        labels_map = {
            "Mantainance": "settings.TRELLO_LABEL_ID_MANTAINANCET",
            "Research": "settings.TRELLO_LABEL_ID_RESEARCHT",
            "Test": "settings.TRELLO_LABEL_ID_TEST"
        }
        label = "Mantainance"
        label_id = labels_map.get(label)
        result=queries.set_task_query(name, label, labels_map)
        self.assertEqual(result.get('name'), name)
        self.assertEqual(result.get('idLabels'), [label_id])

