from django.db import models

# Create your models here.
class Data(models.Model):
    # URL	Web Browser	User Name	Password	Password Strength	User Name Field	Password Field	Created Time	Modified Time	Filename
    common_id = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)
    web_browser = models.TextField(default=None, null=True)
    user_name = models.TextField(default=None, null=True)
    password = models.TextField(default=None, null=True)
    password_strength = models.TextField(default=None, null=True)
    user_name_field = models.TextField(default=None, null=True)
    password_field = models.TextField(default=None, null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    modified_time = models.DateTimeField(auto_now=True, null=True)
    filename = models.TextField(default=None, null=True)


    def __str__(self):
        return f"Data: {self.common_id}, {self.url}, {self.web_browser}, {self.user_name}, {self.password}, {self.metadata}"