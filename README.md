Bootstrap + HTML5 Boilerplate + Common Packages, Tomita Style.
---------------------------------------

My plot for world domination is stagnating due to wasted time loading the same plugins, configuring comically similar projects, and feeling utterly lazy about adding jQuery easing just because I'd have to go google it.

World domination can't wait.


###Django

- Hell yes we'll use the admin, are you freakin kidding me?
- Uses relative settings directory with `PROJECT_DIR` and `SETTINGS_DIR`. How many times have I written that?
- Global templates dir in project root.
- `MEDIA_ROOT = 'site_media'`
- `STATICFILES_DIRS = 'assets'`
- Why don't we call the `ROOT_URLCONF` `root_urlconf.py` so it can be fuzzy differentiated vs 1000 other `urls.py` mmkay?
- Use SQLITE by default. If you need to change it, you'd have to change it anyways.
- No, we don't need to add anything in the user uploads directory to git.
- Serve files from `MEDIA_ROOT` @ `MEDIA_URL` when in `DEBUG_MODE`. Runserver now serves `staticfiles` automagically, why the hell not `MEDIA_ROOT`?
- Start with `website` app for static pages and it even comes with an `IndexView`, imagine that!


###Forcibly installed django apps

Yeah that's right... there are some apps that are unquestionably useful.

- Django Extensions: I know how much you like importing apps in the shell, but seriously, get over it.
- South: Without database migrations, you are nothing. http://south.aeracode.org/
- Pillow: Python Imaging Library with a better success rate. We like `ImageField` don't we?
- Django Debug Tolbar: The `__unicode__` method you wrote that eats 100 queries per object listing doesn't want you to know about this.
- Fabric: Something that I only install when I've already repeated `ssh login, git pull, restart server` at least 100,000 times. Save yourself the trouble.


###Questionably forcibly installed django apps

I feel like these apps are used enough to warrant auto inclusion and explicit removal.

- Mailer. Don't we need to send emails?
- Sorl Thumbnails. Sometimes I don't use it, but only because *it's not installed already* and I am lazy.
- Gunicorn. Yeah, you might not be using it. You'll thank me later.
- ~~PyLibMC. Django is as fast as a rock on steroids. There's no reason not to set up a tiny `memcached` server and enable the cache middleware.~~ The only reason not to include this is because it requires a non python dependency (memcached itself.)


###HTML:

- Bootstrap
- Media queryies are WTF confusing. I conceptually simplified `portrait phone`, `landscape phone`, `default`, `desktop` to  `media-1`, `media-1-max`, `media-2`, etc. so my feeble brain can grasp this nonsense.
- Responsive design debugging snippet at top that displays current bootstrap media range.
- No crazy scripts at the bottom causing issues with inline scripts that need jQuery. F' that! If you want to be that cool, please spent .2 seconds moving the script.
- Less is awesome. Never leave home without it.


## Common Packages

Common packages are included with commented out script tags in the base theme for easy awesomeness.

- jQuery Easing: http://gsgd.co.uk/sandbox/jquery/easing/ 
- jQuery Validation: http://bassistance.de/jquery-plugins/jquery-plugin-validation/
- jQuery Lazy Load: http://www.appelsiini.net/projects/lazyload


## Responsive design helpers

### Media query helpers

Bootstraps default descriptions are a little confusing. The variable names do not have enough common in the variable names.

Am I on tablet portrait or phone horizontal right now?

I find it much easier to deal with responsive design by using media query tags which simply indexes smallest-to-largest designs.


- @media-1
- @media-1-max
- @media-2
- @media-2-max
- @media-3
- @media-3-max
- @media-4
- @media-4-max

Use the `media-N` variables for min-width queries.  
Use the `media-N-max` for max-width queries.

To target browsers between media-1 and media-3 (what bootstrap would call "portrait phones" to "default"): 

    @media (min-width:@media-1) and (max-width:@media-3-max) {
        // ...
    }

### Media query debugger

The base theme.html template comes with a simple debug div which displays the current media query range.

For example: `media-2 to media-3-max`.




Installation and Usage
----------------------

Either clone the repository and take the contents, or use it as a template provided to the django-admin.py command.

    django-admin.py startproject my_project --template=https://github.com/yuchant/django-boilerplate/archive/master.zip 


## Folder Structure

Note: I've set this up to build the project container folder as well as the django project root, so you will get a triple nested structure if you don't change the name of the root project folder after running `startproject`. 

Example:

    $ django-admin.py startproject my_project

Will result in a structure like so:

    ── my_project
        ├── my_project
            ├── my_project


So rename the top-level my_project to something generic. It's not required, but something just feels *off* about that idea.

The reason I do this is because I want my django project to be in a folder in my virtualenv simply called "django_project". It needs to be consistent across sites so I can easily crawl directories for `django_project/conf/` and auto register supervisor scripts, nginx configurations, etc for multiple sites on one server.


    ├── my_project # renamed to something like "django_project"
    │   ├── conf
    │   │   ├── gunicorn
    │   │   │   └── gunicorn.py
    │   │   ├── nginx
    │   │   │   └── nginx.conf
    │   │   └── supervisor
    │   │       └── gunicorn.conf
    │   ├── my_project
    │   │   ├── assets
    │   │   │   ├── bootstrap
    │   │   │   ├── css
    │   │   │   ├── img
    │   │   │   ├── js
    │   │   │   └── less
    │   │   ├── manage.py
    │   │   ├── my_project
    │   │   │   ├── __init__.py
    │   │   │   ├── root_urlconf.py
    │   │   │   ├── settings.py
    │   │   │   └── wsgi.py
    │   │   ├── templates
    │   │   │   ├── 404.html
    │   │   │   ├── 500.html
    │   │   │   └── theme.html
    │   │   └── website
    │   │       ├── __init__.py
    │   │       ├── models.py
    │   │       ├── templates
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── README.md
    │   └── requirements.txt



## Recommended setup

I'd recommend the following setup:

1. create a virtualenv `virtualenv example.com`
2. cd into it `cdvirtualenv`
3. Create the django project `django-admin.py startproject django_project --template=https://github.com/yuchant/django-boilerplate/archive/master.zip` 
4. cd into the django project container `cd django_project`
5. install the dependencies: `pip install -r requirements.txt`
6. cd into the django project itself: `cd django_project`
7. syncdb: `python manage.py syncdb`
8. migrate: `python manage.py migrate`
9. run your dev server: `python manage.py runserver`
