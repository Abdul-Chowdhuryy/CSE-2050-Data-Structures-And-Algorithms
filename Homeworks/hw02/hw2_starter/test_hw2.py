import unittest
from hw2 import Profile, Activity, Post, Message, User

class TestProfileProfile(unittest.TestCase):
    """Test cases for the Profile class."""
    def test_init(self):
        test_1 = Profile('john123', '12345', '5', 'john123@gmail.com')
        self.assertEqual(test_1.username, "john123")
        self.assertEqual(test_1.screen_time, '5')
        self.assertEqual(test_1.email, "john123@gmail.com")
    pass
    

class TestActivity(unittest.TestCase):
    """Test cases for the Activity class."""
    def test_init(self):
        user = User("Jim", "jim123", "Jimmy", "jim@gmail.com")
        activity = Activity(user, "Hello")
        self.assertEqual(activity.user, user)
        self.assertEqual(activity.content, "Hello")
    pass

class TestPost(unittest.TestCase):
    """Test cases for the Post class."""
    def test_init(self):
        user = User("Jim", "jim123", "Jimmy", "jim@gmail.com")
        activity = Activity(user, "Welcome to my channel")
        self.assertEqual(activity.user, user)
        self.assertEqual(activity.content, "Welcome to my channel")
    pass
    
        

class TestMessage(unittest.TestCase):
    """Test cases for the Message class."""
    def test_init(self):
        sender = User("Jim", "jim123", "Jimmy", "jim@gmail.com")
        receiver = User("Bob", "Bob123", "Bobby", "bob@gmail.com")
        message = Message(receiver, sender, "hey")
        self.assertEqual(message.user, sender)
        self.assertEqual(message.receiver, receiver)
        self.assertEqual(message.content, "hey")
    pass

class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    def setUp(self):
        self.user = User("kim", "kim123", "Kimmy", "Kim@gmail.com")

    # Add more test cases for other methods and classes
    
   

    def test_create_post(self):
        """Test creating a post for a user."""
        post = self.user.create_post("Test Post Content")
        # Check if the post is added to the user's posts list
        self.assertIn(post, self.user.posts)
        # Check if the user is correct
        self.assertEqual(post.user, self.user)
        # Check if the content of the post is correct
        self.assertEqual(post.content, "Test Post Content")
    

if __name__ == "__main__":
    unittest.main()

