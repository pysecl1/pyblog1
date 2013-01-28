__author__ = 'User'
from fixture_generator import fixture_generator

from models import Blogs, Posts


@fixture_generator(Blogs)
def test_blogs():
    """
     create test blogs collection
    """
    blog1 = Blogs.objects.create(title="Test blog 1", description="my test blog")