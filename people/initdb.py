# -*- coding: utf-8 -*-
"""
    数据库操作(Author类\Article类\Tag类)
        values_list函数--获取元组形式结果
        values函数--获取字典形式结果
        extra函数--转化成别名
        select_related函数-- 多表关联（一对多 多对一）[使用SQL的JOIN一次性取出相关的内容]
        prefetch_related函数--多表关联（多对多） [使用SQL的JOIN一次性取出相关的内容]
        defer函数--排除不需要的字段(节省内存)
        only函数--仅选择需要的字段(节省内存)

"""
import random
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_demo.settings')
django.setup()

author_name_list = ['WeizhongTu', 'twz915', 'dachui', 'zhe', 'zhen']
article_title_list = ['Django 教程', 'Python 教程', 'HTML 教程']


def create_authors():
    from people.models import Author
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        # 随机生成9位数的QQ，
        author.qq = ''.join(
            str(random.choice(range(10))) for _ in range(9)
        )
        author.addr = 'addr_%s' % (random.randrange(1, 3))
        author.email = '%s@ziqiangxuetang.com' % (author.addr)
        author.save()


def create_articles_and_tags():
    from people.models import Article, Author, Tag
    # 随机生成文章
    for article_title in article_title_list:
        # 从文章标题中得到tag  split(正则,分割次数)
        tag_name = article_title.split(' ', 1)[0]

        # 根据name查询没有则根据条件创建一个记录
        tag, created = Tag.objects.get_or_create(name=tag_name)

        # 随机获取一个作者记录  random.choice(序列)
        random_author = random.choice(Author.objects.all())

        for i in range(1, 21):
            title = '%s_%s' % (article_title, i)
            article, created = Article.objects.get_or_create(
                title=title, defaults={
                    'author': random_author,  # 随机分配作者
                    'content': '%s 正文' % title,
                    'score': random.randrange(70, 101),  # 随机给文章一个打分
                }
            )
            article.tags.add(tag)


# 删除方法
def people_del():
    from people.models import Article, Author, Tag
    Tag.objects.all().delete()
    Article.objects.all().delete()
    Author.objects.all().delete()


# 全局查询
def people_query_all():
    from people.models import Article, Author, Tag
    print(Article.objects.all().values())
    print(Author.objects.all().values())
    print(Tag.objects.all().values())


# values_list、values、 extra
def people_query_sql():
    from people.models import Author, Article, Tag
    # sql语句
    print(Author.objects.filter(name="WeizhongTu"))

    # 显示指定字段 (元组结果)
    print(Author.objects.values_list('name', 'qq'))
    print(Author.objects.values_list('name', flat=True))

    # 显示指定字段 (字典结果)
    print(Author.objects.values('name', 'qq'))

    # 查询twz915这个人的文章标题
    print(Article.objects.filter(author__name='zhen').values_list('title', flat=True))

    # 查询tag中的name信息并使用别名tag_name
    # 通过查看其执行的sql 发现转化的别名tag_name和原来的name都有
    tags = Tag.objects.all().extra(select={'tag_name': 'name'})
    print('name = ' + str(tags[0].name))
    print('tag_name = ' + str(tags[0].tag_name))

    # 使用defer排除
    print(Tag.objects.all().extra(select={'tag_name': 'name'}).defer('name'))

    # 同时从控制台看到每使用tags[0]都会执行一遍sql,所以先将结果集保存后再使用就不会多次执行sql
    # 使用select_related将Article和author关联查询
    articles = Article.objects.all().select_related('author')[:10]
    al = articles[0]
    print('title = ' + str(al.title))
    print('content = ' + str(al.content))
    print('score = ' + str(al.score))


# select_related、prefetch_related
def people_query_sql_2():
    from people.models import Author, Article, Tag

    # 同时从控制台看到每使用tags[0]都会执行一遍sql
    # 所以先将结果集保存后再使用就不会多次执行sql
    articles = Article.objects.all().select_related('author')[:10]
    print('title = ' + str(articles[0].title))
    print('content = ' + str(articles[0].content))

    # 使用select_related将Article和Author关联查询
    # (多端Article对一端Author)
    articles = Article.objects.all().select_related('author')[:10]
    al = articles[0]  # 取一个 则sql会添加 limit 1
    print('title = ' + str(al.title))
    print('content = ' + str(al.content))
    print('score = ' + str(al.score))

    # 使用prefetch_related将Article和Tag关联查询
    # (多端Article对多端Tag)
    articles = Article.objects.all().prefetch_related('tags')[:10]
    print(articles)


# defer、only
def people_query_sql_3():
    from people.models import Author, Article, Tag

    # 文章列表页，只需要文章的标题和作者 (不起作用待定)
    # print(Article.objects.all().defer('title', 'content'))
    # print(Author.objects.all().only('name'))

    # 原生sql
    authors = Author.objects.raw('select id from people_author limit 1')
    for i in authors:
        print(i)


# annotate
def people_query_sql_4():
    from people.models import Article
    from django.db.models import Count
    from django.db.models import Avg
    from django.db.models import Sum

    # sql语句--聚合函数 计算每个作者的文章数(数量)
    # SELECT author_id, COUNT(author_id) AS count FROM blog_article GROUP BY author_id
    ps = Article.objects.all().values('author_id') \
        .annotate(count=Count('author')) \
        .values('author_id', 'count')

    print(ps)

    # sql语句--聚合函数 求一个作者的所有文章的得分平均值(平均数)
    # SELECT author_id, AVG(score) AS avg_score FROM people_article GROUP BY author_id
    ps = Article.objects.all().values('author_id') \
        .annotate(avg_score=Avg('score')) \
        .values('author_id', 'avg_score')
    print(ps)

    # sql语句--聚合函数 求一个作者所有文章的总分(和)
    # SELECT author_id, Sum(score) AS sum_score FROM people_article GROUP BY author_id
    ps = Article.objects.all().values('author_id') \
        .annotate(sum_score=Sum('score')) \
        .values('author_id', 'sum_score')
    print(ps)


def main():
    # people_del()

    # create_authors()
    # create_articles_and_tags()

    # people_query_all()
    # people_query_sql()
    # people_query_sql_2()
    people_query_sql_3()
    # people_query_sql_4()


if __name__ == '__main__':
    main()
    print("Done!")
