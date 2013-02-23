from django.conf.urls.defaults import patterns, url
from apps.blog.views import BlogView
from blog.views_api import BlogApiView

BLOGURL = r'^blog/(?P<blogname>[^/]+?)/get/(?P<n_from>\d+)/(?P<n_count>\d+)/$'
blog_view = BlogView()
blog_api_view = BlogApiView()

urlpatterns = patterns('',
                    url(r'^blog/$', blog_view, {'action': 'list_blogs'}),
                    url(r'^blog/(?P<blogname>[^/]+?)/$',
                        blog_view,
                        {'action': 'index'}),
                    url(r'^blog/(?P<blogname>[^/]+?)/add/$',
                        blog_view,
                        {'action': 'add'}),
                    url(BLOG_URL, blog_api_view, {'action': 'get'}),
)
