#!/bin/sh
(epiphany-browser 127.0.0.1:8080/openhab.app?sitemap=main && pkill xinit)&
matchbox-window-manager
