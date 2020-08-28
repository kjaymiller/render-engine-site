from render_engine import Site, Page, Collection, Blog

site = Site()
site.strict = True
site.Title = j

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


if __name__ == "__main__":
    site.render()
