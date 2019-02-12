if [ ! -e clearlogo-examples ]; then
	mkdir clearlogo-examples
fi
if [ ! -e poster-examples ]; then
	mkdir poster-examples
fi
for i in ../plugin.video.intergalacticfm/resources/*-clearlogo.png; do
	convert -composite test.png $i -gravity center clearlogo-examples/`basename $i`
done
for i in ../plugin.video.intergalacticfm/resources/*-poster.png; do
	convert $i -resize 30% poster-examples/`basename $i`
	convert $i -resize 10% poster-examples/small-`basename $i`
done
./parse.py
