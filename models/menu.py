# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))
response.subtitle = T('Do you wanna be a Pyboy?')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Pyboys <pyboys@pyboys.com>'
response.meta.description = 'pyboys website'
response.meta.keywords = 'web2py, python, framework, geeks'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2012'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default','index'), [])
    ]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu+=[
        (SPAN('web2py',_style='color:yellow'),False, None, [
                ('web2py.com',False,'http://www.web2py.com', [
                        (T('Download'),False,'http://www.web2py.com/examples/default/download'),
                        (T('Support'),False,'http://www.web2py.com/examples/default/support'),
                        (T('Demo'),False,'http://web2py.com/demo_admin'),
                        (T('Quick Examples'),False,'http://web2py.com/examples/default/examples'),
                        (T('FAQ'),False,'http://web2py.com/AlterEgo'),
                        (T('Videos'),False,'http://www.web2py.com/examples/default/videos/'),
                        (T('Free Applications'),False,'http://web2py.com/appliances'),
                        (T('Plugins'),False,'http://web2py.com/plugins'),
                        (T('Layouts'),False,'http://web2py.com/layouts'),
                        (T('Recipes'),False,'http://web2pyslices.com/'),
                        (T('Semantic'),False,'http://web2py.com/semantic'),
                        ]),
                ]
         )]
_()

