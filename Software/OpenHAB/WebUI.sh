#!/bin/sh
(epiphany-browser 127.0.0.1:8080/openhab.app?sitemap=demo && pkill xinit)&
matchbox-window-manager
