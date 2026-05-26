from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def navbar_test(self, soup):
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

    def test_post_list(self):
        # blog 페이지 html을 response에 할당
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200) # 200은 정상

        soup = BeautifulSoup(response.content, 'html.parser') # 응답한 소스코드 분석해라!
        self.assertEqual(soup.title.text, 'Blog')

        # navbar = soup.nav
        # self.assertIn('Blog', navbar.text)
        # self.assertIn('About Me', navbar.text)
        self.navbar_test(soup)
        self.assertEqual(Post.objects.count(), 0)

        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물 없음', main_area.text)

        post_001 = Post.objects.create(
            title='This is the First Post', 
            content = 'Hello world. We are the world.',
        )
        post_002 = Post.objects.create(
            title = 'This is the Second Post',
            content = '''Isn't First everything, Right?''',
        )
        self.assertEqual(Post.objects.count(), 2)

        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)

        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        # 게시물 있으면 게시물 표시 없다면 아래꺼표시(그래서 NotIn 써야됨!)
        self.assertNotIn('아직 게시물 없음', main_area.text)
    
    def test_post_detail(self):
        post_000 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = 'Hello World, We are the world',
        )
        self.assertEqual(post_000.get_absolute_url(), '/blog/1')
        response = self.client.get(post_000.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        