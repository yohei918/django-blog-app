from django.db import models

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Category(models.Model):
    name = models.CharField("カテゴリー", max_length=255)
    slug = models.SlugField("URL",unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='カテゴリー'
        verbose_name_plural='カテゴリー'



class Tag(models.Model):
    name = models.CharField("タグ", max_length=255)
    slug = models.SlugField("URL",unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='タグ'
        verbose_name_plural='タグ'


class Post(models.Model):
    title=models.CharField("タイトル", max_length=200)
    # content=models.TextField("本文")
    content = MarkdownxField(verbose_name='本文')
    image=models.ImageField(verbose_name='画像',upload_to='uploads/',null=True,blank=True)
    created_at=models.DateTimeField("作成日",auto_now_add=True)
    updated_at=models.DateTimeField("更新日",auto_now=True)
    is_published=models.BooleanField("公開設定",default=False)

    category = models.ForeignKey(Category,verbose_name = 'カテゴリー', on_delete=models.PROTECT, null=True, blank=True)
    tag = models.ManyToManyField(Tag, verbose_name = 'タグ', blank=True)

    def conver_markdown_to_html(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='記事'
        verbose_name_plural='記事'

class Comment(models.Model):
    name = models.CharField(verbose_name='名前',max_length=100)
    text = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    post = models.ForeignKey(Post, verbose_name='記事', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name='コメント'
        verbose_name_plural='コメント'

class Reply(models.Model):
    name = models.CharField(verbose_name='名前',max_length=100)
    text = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)

    post = models.ForeignKey(Comment,verbose_name="コメント", on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name='返信'
        verbose_name_plural='返信'








