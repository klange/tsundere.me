# tsundere.me

Automatically locates faces using [facedetect](http://www.thregr.org/~wavexx/hacks/facedetect/) and then composites tsun~tsun~ eyes over them.

tsundere.me runs under uwsgi behind nginx, which handles all of the static files.

Processed images are uploaded anonymously to imgur.

If you're trying to run your own instance, note that I've hardcoded several paths and you'll need an imgur API client ID.
