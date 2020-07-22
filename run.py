from render_engine import Site, Page, Collection

site = Site()
site.strict = True

@site.register_route
class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"

@site.register_collection
class Docs(Collection):
    content_path = 'content/docs'
    routes = ['docs']
    markdown_extras = ['header-ids', 'fenced-code-blocks']

site.render() # build out the tools
