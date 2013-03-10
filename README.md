Bootstrap + HTML5 Boilerplate + Common Packages, Tomita Style.
---------------------------------------

My plot for world domination is stagnating due to wasted time loading the same plugins, configuring comically similar projects, and feeling utterly lazy about adding jQuery easing just because I'd have to go google it.

World domination can't wait.

**HTML:**

- Media queryies are WTF confusing. I conceptually simplified `portrait phone`, `landscape phone`, `default`, `desktop` to  `media-1` `media-1-max`, etc. so my feeble brain can grasp this nonsense.
- Responsive design debugging snippet at top that displays current bootstrap media range.
- No crazy scripts at the bottom causing issues with inline scripts / jquery / etc. F' that! Please go save .1 seconds elsewhere.
- Less is awesome. Never leave home without it.

**Django:**

- Hell yes we'll use the admin, are you kidding me?
- Uses relative settings directory with `PROJECT_DIR` and `SETTINGS_DIR`. How many times have I written that?
- Global templates dir, `MEDIA_ROOT = 'site_media'`, ` `STATICFILES_DIRS = 'assets'`
- Freakin call the `ROOT_URLCONF` `root_urlconf.py` so it can be fuzzy differentiated vs 1000 other `urls.py`
- Use SQLITE by default. If you need to change it, you'd have to change it anyways.
- No, we don't need to add anything in the user uploads directory to git.
- Start with `website` app for static pages.

**General**

- I hate you .DS_Store. Sincerely, me.


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