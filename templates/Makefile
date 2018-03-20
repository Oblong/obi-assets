# Where to install this project's bin, lib, etc. directories
# NOTE: this is kind of like DESTDIR in push.sh
PREFIX ?= /opt/oblong/astor

# Where to put $(PREFIX) when installing (normally empty; used by packagers)
# See https://www.gnu.org/prep/standards/html_node/DESTDIR.html
DESTDIR ?=
export DESTDIR

all:
	echo Nothing to build.

install:
	install -m 755 -d ${DESTDIR}${PREFIX}/share
	cp -a {{project_name}} ${DESTDIR}${PREFIX}/share/.
	find ${DESTDIR}${PREFIX}/share -type d | xargs chmod 755
	find ${DESTDIR}${PREFIX}/share -type f | xargs chmod 644
