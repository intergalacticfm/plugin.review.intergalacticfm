if [ ! -e clearlogo-examples ]; then
	mkdir clearlogo-examples
fi
for i in ../plugin.video.intergalacticfm/resources/*-clearlogo.png; do
	convert -composite test.png $i -gravity center clearlogo-examples/`basename $i`
done
./parse.py
markdown-pdf overview.md
