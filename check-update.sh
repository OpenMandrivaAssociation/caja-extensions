#!/bin/sh
mate_component=caja-extensions
mate_ver=$(curl "https://mate-desktop.org/" 2>/dev/null |grep "released"|sed -e 's,.*-mate-,,;s,-released.*,,;' |head -n1 |tr - .)
curl "https://pub.mate-desktop.org/releases/$mate_ver/" 2>/dev/null |grep "$mate_component" |sed -e "s,.*${mate_component}-,,;s,\.tar\.xz.*,,;" |tail -n1

