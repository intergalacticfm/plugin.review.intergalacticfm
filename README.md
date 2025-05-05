# plugin.video.intergalacticfm-review

Public catalog and admin overview of the Intergalactic FM plugins for Kodi. At the moment only the video plugin is being report on.

## Public catalog

To view the public catalog with streams of the Intergalactic FM TV video plugin for Kodi, see [public-catalog-online.md](https://github.com/intergalacticfm/plugin.review.intergalacticfm/blob/master/public-catalog-online.md) in your browser.

## Admin overview

To review the Intergalactic FM TV video plugin for Kodi, see [admin-overview-online.md](https://github.com/intergalacticfm/plugin.review.intergalacticfm/blob/master/admin-overview-online.md) in your browser.

## Screenshots

Screenshots are in PNG but are optimized with `optipng` to reduce file size.

## Extra

Also available locally are [public-overview-locally.md](public-overview-locally.md) and [admin-overview-locally.md](admin-overview-locally.md) in your browser.

For developers, see also the script `_update_locally.sh`.

## Prerequisists

First, make sure that [plugin.video.intergalacticfm](https://github.com/intergalacticfm/plugin.video.intergalacticfm) has been checked out in `..`

Parse JSON file to Markdown and PDF by running

    ./overview.sh

For this, install first

    sudo npm install -g markdown-pdf

## URL

Note that the video URL can look like:
- https://intergalactic.tv/live/tv/playlist.m3u8
- https://intergalactic.tv/show/reveal/playlist.m3u8

and can be tested with vlc or mpv. The video addon cannot query live the website. All info for all channels needs to be in the addon. Also take care on how the artwork is found.

## Review

Install

    pip install -U kodi-addon-checker

and run

    kodi-addon-checker --branch matrix ../plugin.audio.intergalacticfm
    kodi-addon-checker --branch omega ../plugin.audio.intergalacticfm
    kodi-addon-checker --branch matrix ../plugin.video.intergalacticfm
    kodi-addon-checker --branch omega ../plugin.video.intergalacticfm

## Updates

Check the proper version of the required script.module imports at
https://mirrors.kodi.tv/addons/

Updates in Kodi's main repository can be made via https://kodi.wiki/view/HOW-TO:Create_add-on_PRs_using_Git_Subtree_Merging See also our repo for that https://github.com/intergalacticfm/repo-plugins

