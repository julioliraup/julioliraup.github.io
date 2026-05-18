AUTHOR = 'Julio Lira'
SITENAME = 'Julioliraup (jul10l1r4) - Blog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'
THEME = './casper2pelican/'
STATIC_PATHS = ['static', 'extra']
ARTICLE_EXCLUDES = ['extra']
DEFAULT_HEADER_IMAGE = '/static/main.gif'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

EXTRA_PATH_METADATA = {
    'extra/googleaa9a829f41211379.html': {'path': 'googleaa9a829f41211379.html'},
}
# Blogroll
LINKS = (
    ("Github", "https://github.com/julioliraup/"),
    ("Linkedin", "https://www.linkedin.com/in/jul10l1r4/"),
)

# Social widget
SOCIAL = (
        (),
)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
