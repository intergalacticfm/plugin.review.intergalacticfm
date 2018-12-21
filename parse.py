#!/usr/bin/env python3

from json import load
from datetime import datetime
from pprint import pprint


def write(out, now, locally=False):
    out.write('# Intergalactic FM streams for Kodi plugin\n\n')
    out.write('Below are the specific texts and images required by Kodi. '
              'Please, try to meet the requirements as close as possible. '
              'Kodi has many different views and we do not know which view '
              'for navigating and playing streams is used by the user. '
              'So using this format as described by Kodi itself gives the '
              'best result for all. '
              'This overview has been automatically generated on {}.\n\n'.format(now))
    
    streams = load(open('../plugin.video.intergalacticfm/resources/streams.json'))
    for key, values in streams.items():
        filename = values['label'].lower().replace(' ', '_')
        out.write('## {}\n\n'.format(values['label']))
        out.write('**Tagline** (two to five words): *{}*\n\n'.format(values['tagline']))
        out.write('**Genre** (one to three genres): *{}*\n\n'.format(values['genre']))
        out.write('**Plot** (twenty to thirty words): *{}*\n\n'.format(values['plot']))
        out.write('**ID and basename**: `{}` and `{}`\n\n'.format(key, filename))
        out.write('**Poster** (1000 x 1500 PNG, main logo in center):\n')
        if locally:
            out.write('![Poster](../plugin.video.intergalacticfm/resources/{}-poster.png "Poster")\n\n'.format(filename))
        else:
            out.write('![Poster](https://raw.githubusercontent.com/intergalacticfm/plugin.video.intergalacticfm/master/resources/{}-poster.png "Poster")\n\n'.format(filename))
        out.write('**Fanart** (1920 x 1080 JPG, only for background):\n')
        if locally:
            out.write('![Fanart](../plugin.video.intergalacticfm/resources/{}-fanart.jpg "Fanart")\n\n'.format(filename))
        else:
            out.write('![Fanart](https://raw.githubusercontent.com/intergalacticfm/plugin.video.intergalacticfm/master/resources/{}-fanart.jpg "Fanart")\n\n'.format(filename))
        out.write('**Clear logo** (810 x 310 PNG with transparency):\n')
        out.write('![Clear logo](clearlogo-examples/{}-clearlogo.png "Fanart")\n\n'.format(filename))
    
    out.close()

now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
write(open('overview-online.md', 'w'), now)
write(open('overview-locally.md', 'w'), now, True)
