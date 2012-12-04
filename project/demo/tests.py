from django.test import TestCase
from django.contrib.sessions.models import Session

# don't actually do anything with this, but register the Session
# subclass
import utility.models

class DemoTest(TestCase):
    def test_demo(self):
        s = Session()
        from datetime import datetime
        s.expire_date = datetime.now()
        s.save()
        s.delete()
