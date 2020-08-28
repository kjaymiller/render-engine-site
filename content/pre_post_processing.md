title: Executing PRE and POST Processed Code
category: tips

Render Engine doesn't have any pre or post processing hooks to speak of because
of it's simple design.

It is still easy to execute code before or after you have run `render()` for
your site.

Here is a look at how this site is generated.

```python
from render_engine import Site, Page, Collection, Blog

site = Site()
site.strict = True
site.SITE_TITLE = "Render_Engine"
site.SITE_URL = "https://render-engine.site"


@site.register_route
class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"

@site.register_collection
class blog(Blog):
    site.render() # build out the tools
    template_path: 'content'
    routes = ['blog']
    markdown_extras = ['footnotes']
    subcollections = ['category']


if __name__ == "__main__":

  site.render() # build out the tools

```

Let's add a custom message to our logging when render-engine
starts and ends.

- import `logging` to your run.py
- setup your logging parameters to output to a file and to change the `log_level` to information[^1]

```python
import logging

logging.basicConfig(
                    filename="render-engine.log",
                    filemode="a",
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

```

- Add your log statement before `site.render()`

```python
if __name__ == "__main__":
  logging.info('started_site_build') # This runs before
  site.render() # build out the tools
  logging.info('finished_site_build') # This runs when finished
```

After you run `site.render()`, you should see a new `render-engine.log` your
directory with some basic information about your site. 
sl

```
13:23:53,651 root INFO started_site_build
13:23:53,655 root INFO subcollection_group='category'
13:23:53,659 root INFO filepath=PosixPath('output/index.html') written!
13:23:53,661 root INFO filepath=PosixPath('output/blog/blog.html') written!
13:23:53,669 root INFO filepath=PosixPath('output/blog.rss.xml') written!
u 13:23:53,669 root INFO finished_site_build
```

You can use this to execute commands like setting global variables, running
shell scripts and more.

  [^1]: setting log_level to information can also add logging information to the site that you did not expect due to render-engines dependencies.
