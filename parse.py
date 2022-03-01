#!/usr/bin/env python3
'''Parses resources to create review.'''

from json import load
from datetime import datetime


def overview(out, now, locally=False):
    out.write('# Intergalactic FM streams for Kodi video plugin\n\n')
    streams = load(open('../plugin.video.intergalacticfm/resources/streams.json'))
    for key, values in streams.items():
        filename = values['label'].lower().replace(' ', '_')
        anchor = values['label'].lower().replace(' ', '-')
        if values['label'].lower() == 'mule driver': # exception
            filename = 'muledriver'
            anchor = 'mule-driver'
        elif values['label'].lower() == 'el camino': # exception
            filename = 'elcamino'
            anchor = 'el-camino'
        elif values['label'].lower() == 'cobra fm': # exception
            filename = 'cobrafm'
            anchor = 'cobra-fm'
        elif values['label'].lower() == 'murder capital tv': # exception
            filename = 'intergalactic_tv'
            anchor = 'intergalactic-tv'
        out.write('[![Poster](poster-examples/small-{}-poster.png "Poster")](#{})'.format(filename, anchor))
    out.write('\n\n')
    out.write('Below are the specific texts and images required by Kodi. '
              'Please, try to meet the requirements as close as possible. '
              'Kodi has many different views and we do not know which view '
              'for navigating and playing streams is used by the user. '
              'So using this format as described by Kodi itself gives the '
              'best result for all. Let is know when something needs to be '
              'changed. This overview has been automatically generated on '
              '{}.\n\n'.format(now))
    out.write('**Pleas note:** that the examples below with a **clearlogo** '
              'are **only** shown in Kodi when you hit pause. The clearlogo is '
              'not shown during normal playback. So a stream can still sport '
              'its own logos whereever on the screen they want.\n\n')
    for key, values in streams.items():
        filename = values['label'].lower().replace(' ', '_')
        if values['label'].lower() == 'mule driver': # exception
            filename = 'muledriver'
        elif values['label'].lower() == 'el camino': # exception
            filename = 'elcamino'
        elif values['label'].lower() == 'cobra fm': # exception
            filename = 'cobrafm'
        elif values['label'].lower() == 'murder capital tv': # exception
            filename = 'intergalactic_tv'
        out.write('## {}\n\n'.format(values['label']))
        out.write('**Tagline** (two to five words): *{}*\n\n'.format(values['tagline']))
        out.write('**Plot** (twenty to thirty words): *{}*\n\n'.format(values['plot']))
        out.write('**Genre** (one to three genres): *{}*\n\n'.format(values['genre']))
        out.write('**ID and basename**: `{}` and `{}`\n\n'.format(key, filename))
        out.write('**Poster** (1000 x 1500 PNG, main logo in center):\n')
        out.write('![Poster](poster-examples/{}-poster.png "Poster")\n\n'.format(filename))
        out.write('**Fanart** (1920 x 1080 JPG, only for background, max. quality 96, prefer 90):\n')
        if locally:
            if filename == 'intergalactic_tv':
                out.write('![Fanart](../plugin.video.intergalacticfm/resources/fanart.jpg "Fanart")\n\n')
            else:
                out.write('![Fanart](../plugin.video.intergalacticfm/resources/{}-fanart.jpg "Fanart")\n\n'.format(filename))
        else:
            if filename == 'intergalactic_tv':
                out.write('![Fanart](https://raw.githubusercontent.com/intergalacticfm/plugin.video.intergalacticfm/develop/resources/fanart.jpg "Fanart")\n\n')
            else:
                out.write('![Fanart](https://raw.githubusercontent.com/intergalacticfm/plugin.video.intergalacticfm/develop/resources/{}-fanart.jpg "Fanart")\n\n'.format(filename))
        out.write('**Clear logo** (800 x 310 PNG with transparency):\n')
        out.write('![Clear logo](clearlogo-examples/{}-clearlogo.png "CLearlogo")\n\n'.format(filename))

    out.close()

def catalog(out, now, locally=False):
    out.write('# Intergalactic FM streams for Kodi video plugin\n\n')
    streams = load(open('../plugin.video.intergalacticfm/resources/streams.json'))
    for key, values in streams.items():
        filename = values['label'].lower().replace(' ', '_')
        anchor = values['label'].lower().replace(' ', '-')
        if values['label'].lower() == 'mule driver': # exception
            filename = 'muledriver'
            anchor = 'mule-driver'
        elif values['label'].lower() == 'el camino': # exception
            filename = 'elcamino'
            anchor = 'el-camino'
        elif values['label'].lower() == 'cobra fm': # exception
            filename = 'cobrafm'
            anchor = 'cobra-fm'
        elif values['label'].lower() == 'murder capital tv': # exception
            filename = 'intergalactic_tv'
            anchor = 'intergalactic-tv'
        out.write('[![Poster](poster-examples/small-{}-poster.png "Poster")](#{})'.format(filename, anchor))
    out.write('\n\n')
    out.write('Streams are only available in Kodi if they are live. When they are not live, they are hidden.\n')
    out.write('\n\n')
    for key, values in streams.items():
        filename = values['label'].lower().replace(' ', '_')
        if values['label'].lower() == 'mule driver': # exception
            filename = 'muledriver'
        elif values['label'].lower() == 'el camino': # exception
            filename = 'elcamino'
        elif values['label'].lower() == 'cobra fm': # exception
            filename = 'cobrafm'
        elif values['label'].lower() == 'murder capital tv': # exception
            filename = 'intergalactic_tv'
        out.write('# {}\n\n'.format(values['label']))
        out.write('![menu item](poster-examples/{}-poster.png "menu item")\n\n'.format(filename))
        out.write('**Tagline** *{}*\n\n'.format(values['tagline']))
        out.write('**Plot** *{}*\n\n'.format(values['plot']))
        out.write('**Genre** *{}*\n\n'.format(values['genre']))
        out.write('**Background** (only shown behind menu)\n')
        if locally:
            if filename == 'intergalactic_tv':
                out.write('![background](../plugin.video.intergalacticfm/resources/fanart.jpg "background")\n\n')
            else:
                out.write('![background](../plugin.video.intergalacticfm/resources/{}-fanart.jpg "background")\n\n'.format(filename))
        else:
            if filename == 'intergalactic_tv':
                out.write('![background](https://raw.githubusercontent.com/intergalacticfm/plugin.video.intergalacticfm/develop/resources/fanart.jpg "background")\n\n')
            else:
                out.write('![background](https://raw.githubusercontent.com/intergalacticfm/plugin.video.intergalacticfm/develop/resources/{}-fanart.jpg "background")\n\n'.format(filename))
        out.write('**Logo** (only shown when pauzing stream)\n')
        out.write('![logo](clearlogo-examples/{}-clearlogo.png "logo")\n\n'.format(filename))

    out.write('# Colophon\n\n')
    out.write('The video plugin can be installed directly from within Kodi. For more information, see https://kodi.tv/addon/plugins-video-add-ons/intergalactic-fm-tv')
    out.write('\n\n')
    out.write('This overview has been automatically generated on '
              '{}.\n\n'.format(now))
    out.close()

now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
overview(open('admin-overview-online.md', 'w'), now)
overview(open('admin-overview-locally.md', 'w'), now, True)
catalog(open('public-catalog-online.md', 'w'), now)
catalog(open('public-catalog-locally.md', 'w'), now, True)
