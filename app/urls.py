# Create your urls here.
from django.conf.urls import patterns, include, url
# -*- encoding: utf-8 -*-
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='app.login'),
    url(r'^dashboard/$', views.welcome_view, name='app.welcome'),
    url(r'^signup/$', views.signup_view, name='app.signup'),
    url(r'^login/$', views.logins_view, name='app.logins'),
    url(r'^nosotros/$', views.us_view, name='app.us'),
    url(r'^documentacion-api/$', views.tasks_view, name='app.tasks'),
    url(r'^empresas/$', views.companies_view, name='app.companies'),
    url(r'^temas/$', views.categories_view, name='app.categories'),
    url(r'^temas/(?P<slug>[^\.]+)/$', views.category_view, name='app.category'),
    url(r'^blog/$', views.blogs_view, name='app.blogs'),
    url(r'^blog/(?P<slug>[^\.]+)/$', views.blog_view, name='app.blog'),
    url(r'^eventos/$', views.dates_view, name='app.dates'),
    url(r'^tienda/$', views.products_view, name='app.products'),
    url(r'^pagos/$', views.payments_view, name='app.payments'),
    url(r'^pago/(?P<slug>[^\.]+)/$', views.payment_view, name='app.payment'),
    url(r'^cart/$', views.cart_view, name='app.cart'),
    url(r'^confirmando/$', views.confirmbuy_view, name='app.confirmbuy'),
    url(r'^addcart/(?P<slug>[^\.]+)/$', views.addcart_view, name='app.addcart'),
    url(r'^deletecart/(?P<slug>[^\.]+)/$', views.deletecart_view, name='app.deletecart'),
    url(r'^buyment/$', views.buyment_view, name='app.buyment'),
    url(r'^confirmar-pagos/$', views.paymentc_view, name='app.paymentc'),
    url(r'^addbuyment/$', views.addbuyment_view, name='app.addbuyment'),
    url(r'^salir/$', views.logout_view, name='app.logout'),
    url(r'^nuevo-audio/$', views.uploadtrack_view, name='app.uploadtrack'),
    url(r'^audios/(?P<slug>[^\.]+)/$', views.track_view, name='app.track'),
    url(r'^publicar/$', views.createblog_view, name='app.createblog'),
    url(r'^usuario/(?P<slug>[^\.]+)/$', views.userprofile_view, name='app.userprofile'),
    url(r'^actualizar/foto-perfil/(?P<slug>[^\.]+)/$', views.updateavatar_view, name='app.updateavatar'),
    url(r'^actualizar/nombre-usuario/(?P<slug>[^\.]+)/$', views.updatenickname_view, name='app.updatenickname'),
    url(r'^actualizar/miembro-color-a/(?P<slug>[^\.]+)/$', views.updatecolora_view, name='app.colora'),
    url(r'^actualizar/miembro-color-b/(?P<slug>[^\.]+)/$', views.updatecolorb_view, name='app.colorb'),
    url(r'^actualizar/miembro-color-c/(?P<slug>[^\.]+)/$', views.updatecolorc_view, name='app.colorc'),
    url(r'^actualizar/miembro-color-d/(?P<slug>[^\.]+)/$', views.updatecolord_view, name='app.colord'),
    url(r'^actualizar/miembro-color-e/(?P<slug>[^\.]+)/$', views.updatecolore_view, name='app.colore'),
    url(r'^actualizar/miembro-color-f/(?P<slug>[^\.]+)/$', views.updatecolorf_view, name='app.colorf'),
    url(r'^actualizar/miembro-color-g/(?P<slug>[^\.]+)/$', views.updatecolorg_view, name='app.colorg'),
    url(r'^actualizar/miembro-color-h/(?P<slug>[^\.]+)/$', views.updatecolorh_view, name='app.colorh'),
    url(r'^actualizar/miembro-color-i/(?P<slug>[^\.]+)/$', views.updatecolori_view, name='app.colori'),
    url(r'^actualizar/miembro-color-j/(?P<slug>[^\.]+)/$', views.updatecolorj_view, name='app.colorj'),
    url(r'^actualizar/miembro-color-k/(?P<slug>[^\.]+)/$', views.updatecolork_view, name='app.colork'),
    url(r'^actualizar/miembro-color-l/(?P<slug>[^\.]+)/$', views.updatecolorl_view, name='app.colorl'),
    # API REST 
    url(r'^api/tracks', views.TracksApi.as_view(), name='api-tracks'),
    url(r'^api/device', views.device, name='api-device'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]