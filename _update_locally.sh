# Only use this script while developing!
# Exit Kodi, run this script and start Kodi again.
if [ -e ~/.kodi/addons/plugin.video.intergalacticfm ]; then
	rm -rf ~/.kodi/addons/plugin.video.intergalacticfm/*
	cp -a ../plugin.video.intergalacticfm/* ~/.kodi/addons/plugin.video.intergalacticfm/
fi
#
if [ -e ~/.kodi/addons/plugin.audio.intergalacticfm ]; then
	rm -rf ~/.kodi/addons/plugin.audio.intergalacticfm/*
	cp -a ../plugin.audio.intergalacticfm/* ~/.kodi/addons/plugin.audio.intergalacticfm/
fi
