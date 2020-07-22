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

    def __init__(self):
        super().__init__()
        self.markdown_extras.append('toc')
        self.markdown_extras.append('header-ids')

        for page in self.pages:
            print(page.markup)

site.render() # build out the tools
