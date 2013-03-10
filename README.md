Bootstrap + HTML5 Boilerplate + Common Packages, Tomita Style.
---------------------------------------

My plot for world domination is stagnating due to wasted time loading the same plugins, configuring comically similar projects, and feeling utterly lazy about adding jQuery easing just because I'd have to go google it.

World domination can't wait.


###HTML:

- Bootstrap
- Media queryies are WTF confusing. I conceptually simplified `portrait phone`, `landscape phone`, `default`, `desktop` to  `media-1` `media-1-max`, etc. so my feeble brain can grasp this nonsense.
- Responsive design debugging snippet at top that displays current bootstrap media range.
- No crazy scripts at the bottom causing issues with inline scripts / jquery / etc. F' that! If you want to be that cool, please spent .2 seconds moving the script.
- Less is awesome. Never leave home without it.


###Django

- Hell yes we'll use the admin, are you kidding me?
- Uses relative settings directory with `PROJECT_DIR` and `SETTINGS_DIR`. How many times have I written that?
- Global templates dir, `MEDIA_ROOT = 'site_media'`, ` `STATICFILES_DIRS = 'assets'`
- Why don't we call the `ROOT_URLCONF` `root_urlconf.py` so it can be fuzzy differentiated vs 1000 other `urls.py` mmkay?
- Use SQLITE by default. If you need to change it, you'd have to change it anyways.
- No, we don't need to add anything in the user uploads directory to git.
- Serve files from `MEDIA_ROOT` @ `MEDIA_URL` when in `DEBUG_MODE`. Runserver now serves `staticfiles` automagically, why the hell not `MEDIA_ROOT`?
- Start with `website` app for static pages and it even comes with an `IndexView`, imagine that!


###Forcibly installed django apps

Yeah that's right... there are some apps that are unquestionably useful.

- Django Extensions. I know how much you like importing apps in the shell, but seriously, get over it.
- South. Without database migrations, you are nothing. http://south.aeracode.org/
- Pillow. Python Imaging Library with a better success rate. We like `ImageField` don't we?
- Django Debug Tolbar. This is what the `__unicode__` method that eats 100 queries per object listing doesn't want you to know.
- Fabric. Something that I only install when I've already repeated `ssh login, git pull, restart server` at least 100,000 times. Just have it from day one.


###Questionably forcibly installed django apps

I feel like these apps are used enough to warrant auto inclusion and explicit removal.

- Mailer. Don't we need to send emails?
- Sorl Thumbnails. Sometimes I don't use it, but only because *it's not installed already* and I am lazy.
- Gunicorn. Yeah, you might not be using it. You'll thank me later.
- PyLibMC. Django is as fast as a rock on steroids. There's no reason not to set up a tiny `memcached` server and enable the cache middleware.



## Common Packages

Common packages are included with commented out script tags in the base theme for easy awesomeness.

- jQuery Easing: http://gsgd.co.uk/sandbox/jquery/easing/ 
- jQuery Validation: http://bassistance.de/jquery-plugins/jquery-plugin-validation/
- jQuery Lazy Load: http://www.appelsiini.net/projects/lazyload


## Responsive design helpers

### Media query helpers

I find it much easier to deal with responsive design by using media query tags such as `media-1`, `media-2`, etc.

In general, always use `media-N` as a min-width. Use the `media-N-max` values as max widths.

To target browsers between media-1 and media-3 (what bootstrap would call "portrait phones" to "default"): 

    @media (min-width:@media-1) and (max-width:@media-3-max) {
        // ...
    }

### Media query debugger

The base theme.html template comes with a simple debug div which displays the current media query range.



Installation / Usage
--------------------

Either clone the repository and take the contents, or use it as a template provided to the django-admin.py command.

    django-admin.py startproject my_project --template=https://github.com/yuchant/django-boilerplate/archive/master.zip 