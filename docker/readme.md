##Scipts to deploy my cool website

I'm still working out the bugs in this process..

#### deployment:
	build/pull docker image

	link up the necessary directories (compose handles this)

	add necessary directories for our logs

	update pip
	pip install requirements

	install node, npm and gulp
	install gulp plugins and dependencies
	use gulp to assemble, compile, and compress our assets
	put those assets somewhere that nginx can serve em out directly

	wrangle our nginx configs
	wrangle our uwsgi configs
	restart nginx

	start uwsgi
