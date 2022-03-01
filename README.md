# plugin.video.intergalacticfm-review

Public catalog and admin overview of the Intergalactic FM plugins for Kodi. At
the moment only the video plugin is being report on.

## Public catalog

To view the public catalog with streams of the Intergalactic FM TV video plugin for Kodi, see [public-catalog-online.md](https://github.com/intergalacticfm/plugin.review.intergalacticfm/blob/master/admin-catalog-online.md) in your browser.


## Admin overview

To review the Intergalactic FM TV video plugin for Kodi, see [admin-overview-locally.md](admin-overview-locally.md) in your browser.


## Screenshots

Screenshots are in PNG but are optimized with `optipng` to reduce file size.


## Extra

Also available are [public-overview-locally.md](public-overview-locally.md) and [public-overview-online.md](https://github.com/intergalacticfm/plugin.review.intergalacticfm/blob/master/admin-overview-online.md).

For developers, see also the script `_update_locally.sh`.


## Prerequisists

First, make sure that [plugin.video.intergalacticfm](https://github.com/intergalacticfm/plugin.video.intergalacticfm)
has been checked out in `..`

Parse JSON file to Markdown and PDF by running

    ./overview.sh

For this, install first

    sudo npm install -g markdown-pdf


## Updates

Updates in Kodi's main repository can be made via
~~https://kodi.wiki/view/Submitting_Add-ons#Pull_requests~~
https://kodi.wiki/view/HOW-TO:Create_add-on_PRs_using_Git_Subtree_Merging

The command to run are:
    git clone https://github.com/intergalacticfm/repo-plugins
    cd repo-plugins
    git remote -v
    git checkout krypton
    TODO
    TODO
    TODO
    
    
    

