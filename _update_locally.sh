# Only use this script while developing!
# Exit Kodi, run this script and start Kodi again.
if [ -e ../plugin.video.intergalacticfm ]; then
    if [ -e ~/.kodi/addons/plugin.video.intergalacticfm ]; then
    	rm -rf ~/.kodi/addons/plugin.video.intergalacticfm/*
    	cp -a ../plugin.video.intergalacticfm/* ~/.kodi/addons/plugin.video.intergalacticfm/
    fi
	if [ -e ~/.var/app/tv.kodi.Kodi/data/addons/plugin.audio.intergalacticfm ]; then
        rm -rf ~/.var/app/tv.kodi.Kodi/data/addons/plugin.audio.intergalacticfm/*
    	cp -a ../plugin.video.intergalacticfm/* ~/.var/app/tv.kodi.Kodi/data/addons/plugin.audio.intergalacticfm
	fi
fi
#
#if [ -e ~/.kodi/addons/plugin.audio.intergalacticfm -a -e ../plugin.audio.intergalacticfm ]; then
#	rm -rf ~/.kodi/addons/plugin.audio.intergalacticfm/*
#	cp -a ../plugin.audio.intergalacticfm/* ~/.kodi/addons/plugin.audio.intergalacticfm/
#fi
