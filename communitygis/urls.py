# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import url, include
from django.views.generic import TemplateView

from geonode.urls import urlpatterns
from geonode.monitoring import register_url_event

from django.urls import path, re_path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
## include your urls here
	url(r'^dashboard/', include('dashboard.urls')),
	url(r'^schoolgis/',include('school_gis.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# homepage = register_url_event()(TemplateView.as_view(template_name='site_index.html'))

urlpatterns = [
   url(r'^/?$',
       TemplateView.as_view(template_name='landing-page.html'),
       name='home'),
 ] + urlpatterns
