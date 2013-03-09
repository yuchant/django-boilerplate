Django Boilerplate Project Tomita Style
---------------------------------------

Bootstrap + HTML5 Boilerplate, just tomita style.

That just means there's a lot of things I find convenient in this. You may enjoy it as well.

- Responsive design debugging snippet at top that displasy current range.
- Media querys conceptually simplified to `media-1` `media-1-max`, etc.
- No crazy scripts at the bottom causing issues with inline scripts / jquery / etc.
- Assumes assets/less compiled to assets/css
- Uses relative settings directory paths by default
- I'm sure this will be out dated. Sorry.
- Global templates dir
- Starts with `website` app for static pages.

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