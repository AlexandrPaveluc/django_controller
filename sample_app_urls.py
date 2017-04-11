from django.conf.urls import url, patterns, include

from sample_controller import SampleController

urlpatterns = patterns(
    '',
    url(r'^function/', include(SampleController.getUrls())),
)
