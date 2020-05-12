#! /bin/sh

NAME=$1

VERSIONS="git $(seq 24 24 | sed 's/^/0./') 0.24-zh"

for v in $VERSIONS; do
	cp --no-clobber "%%CHROOT_DGLDIR%%/data/crawl-$v-settings/init.txt" "%%CHROOT_RCFILESDIR%%/crawl-$v/$NAME.rc"
	cp --no-clobber "%%CHROOT_DGLDIR%%/data/crawl-git.macro" "%%CHROOT_RCFILESDIR%%/crawl-$v/$NAME.macro"
done

mkdir -p "%%CHROOT_MORGUEDIR%%/$NAME"
mkdir -p "%%CHROOT_TTYRECDIR%%/$NAME"
