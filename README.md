django最佳实践 项目目录结构布局
=====
1. 参考下列链接建立的目录， 详情请到网站观看
2. 项目目录为 参考 请根据自己需要选择使用。

参考链接：
=====
[quora](http://www.quora.com/What-are-some-Best-Practices-for-Django-Development)

    Joseph Misiti, I develop websites using Django.
    60 votes by Bulat Bochkariov, Christopher Burnor, Ken Saggy, (more)
    Here are some things I have learned over the years that have helped me:

    1. Try to setup your projects with the following directory structure

    /myproject
       /apps
       /configs
       /settings
       /deploy
       /static
       /templates
       urls.py
       fabfile.py


    apps - contains subfolders with specific functionality (static, accounts, etc)

    configs - stores all configuration related scripts (gunicorn, nginx, celery, mongdb, redis, etc). It's useful because you can use fabric (put command) to copy these over to the correct locations on a server

    deploy - contains all deploy scripts, set up in similar manner to this project[1]

    A lot of examples you see online put everything into a single fabfile.py, but that gets really messy as a project gets larger. Having a deploy folder that is organized like django-fabtastic allows you to cut-and-paste it over into other projects if you are using the same technologies

    settings - a folder (not a file like settings.py) that is setup based on this reference [2]

    You could use local_settings.py, production_settings.py etc. but that yipit guys got it right and that is definitely the way to go

    static - contains js, css, images, types/fonts

    templates - all your html files

    2. Use gunicorn[3] instead of apache. If for no other reason, a print statement in code wont crash the entire site. Gunicorn is less bloated and very easy to configure. And large sites like instagram are using it at web scale so dont let people tell you its not a good idea - it will make your job easier and you can leave the office and drink a lot more beer

    3. Use celery for anything that can be made asynchronous (sending emails, uploading photos, etc). Dont make the user wait for the request to return, push it onto a queue and let celery do the work for you. Also, do not use rabbitmq as the celery backend, use redis. RabbitMQ is supposedly more stable and messages cant get lost, but it's also a pain to configure and 99% of people can afford to lose a message because a lost message really doesnt matter that much.

    4. If you are going to use a SQL-based solution, then use South for migrations. I  have had a lot of success migrating away (completely) from Django's ORM[7] and sticking to PyMongo[5] + MongoEngine[5]. Development is way more fun if you're using MongoDB, if you do not believe me, try it out. Say goodbye to painful schema migrations. Ya, and I know, MongoDB doesn't scale, but guess what, it does.

    5. If you need to make a REST API, then use Django-TastyPie[8]. Unfortunately, there is currently no good solution for constructing RESTful APIs if your backend is MongoDB. If I am wrong, provide a link please because no one on StackOverflow could[9]

    6. Do not use test.py for unit tests, put them in a directory called tests/__init__.py and import them in that __init__.py file. Also, trying using
    nose, it's really cool.[10]

    7. Look and good open source project for reference. The most obviously is the Django project itself[11], but Newsblur[12] and Everyblock[13] are also great references:

    That is it- that is 3 years worth of trail-and-error for free!




[心内求法:python开源项目目录结构参考](http://www.cnblogs.com/holbrook/archive/2012/02/24/2366386.html)

    .tx/                                       如果你使用Transifex进行国际化的翻译工作，创建此目录
            config                           Transifex的配置文件
    $PROJ_NAME/                    按照你实际的项目名称创建目录。如果有多个子项目，就创建多个目录
    docs/                                    项目文档
    wiki/                                      如果有wiki，可以创建此目录
    scripts/                                 项目用到的各种脚本
    tests/                                    测试代码
    extras/                                  扩展，不属于项目必需的部分，但是与项目相关的sample、poc等，下面给出4个例子：
            dev_example/
            production_example/
            test1_poc/
            test2_poc/
    .gitignore                             版本控制文件，现在git比较流行
    AUTHORS                           作者清单
    INSTALL                              安装说明
    LICENSE                              版权声明
    MANIFEST.in                       装箱清单文件
    MAKEFILE                           编译脚本
    README                              项目说明文件，其他需要的目录下也可以放一个README文件，说明该目录的内容
    setup.py                               python模块的安装脚本


[django最佳实践：项目布局](http://www.cnblogs.com/holbrook/archive/2012/02/25/2368231.html)

    project结构
    这里定义的是python开源项目目录结构中的$PROJ_NAME目录内的内容，需要与python开源项目目录结构结合起来。
    PROJ_NAME/
         __init__.py      这几个文件是django创建project所必须的，不做过多说明
         manage.py
         settings.py
         urls.py
         apps/               即使是“小”工程，也建议分成多个app，每个app足够简单，只解决某一个方面的问题 （注1）
             myapp1/
             myapp2/
         extra_apps/     引用的其他app。
         libs/                加载第三方模块，可以避免版本冲突，按照标准的site-packages管理（注2）
               python*.*/　　指定python版本号
                   site-packages/
                   requirements.pip    #pip的依赖说明文件
         tests/          project级别的测试，对于每个app，还要有自己的测试代码
         static/          静态内容
                css/
                js/
                images/
         uploads/       上传文件所在目录
         templates/    模板目录，覆盖app的模板
                flatpages/
                comments/
                example/
                app1/
                app2/
         templatetags/    tag目录

    注1：指定app加载，在settings.py中设置：

    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'extras'))
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))
    注2：自定义libs的加载，在settings.py中设置：

    sys.path.insert(0, '/{{MY_LIB)}/site-packages/*****.egg')
    sys.path.insert(0, '/{{MY_LIB}} /site-packages/')
    app目录结构
    $APP_NAME/
         tests/                    app级别的测试代码
         models/                 注1
              __init__.py
              Amodels.py
              Bmodels.py
         templates/              注2
         templatetags/        tag目录

    注1：如果很好的控制app的规模，Model类数量少，可以使用惯用的models.py文件中, 否则将models做成一个package
    接下来可以有两种做法：

    1. 在__init__.py中import所有的Model类
    2. 指定Model的元类（Meta）的app_label, 参考这里

    注2：如果extend 工程下的base.html， 使用 !base.html