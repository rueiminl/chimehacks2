from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'chimehack_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'chimehack_server.views.home'),
    url(r'^signup$', 'chimehack_server.views.signup', name='signup'),
    url(r'^settings$', 'chimehack_server.views.settings', name='settings'),
    url(r'^home$', 'chimehack_server.views.home', name='home'),
    url(r'^dresponseToText$', 'chimehack_server.views.dresponseToText', name='dresponseToText'),
    url(r'^login$', 'chimehack_server.views.login', name='login'),
    url(r'^verification$', 'chimehack_server.views.verification', name='verification'),
    url(r'^contactHelp/(?P<id>\d+)$', 'chimehack_server.views.contactHelp', name='contactHelp'),
    url(r'^responseToText$', 'chimehack_server.views.responseToText', name='responseToText'),


]
