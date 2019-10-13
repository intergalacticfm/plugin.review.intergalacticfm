# Only use this script while developing!
# Exit Kodi, run this script and start Kodi again.
rm -rf ~/.kodi/addons/plugin.video.intergalacticfm/*
cp -a ../plugin.video.intergalacticfm/* ~/.kodi/addons/plugin.video.intergalacticfm/
#
rm -rf ~/.kodi/addons/plugin.audio.intergalacticfm/*
cp -a ../plugin.audio.intergalacticfm/* ~/.kodi/addons/plugin.audio.intergalacticfm/
