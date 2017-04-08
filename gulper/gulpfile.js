// requirements
var
	gulp = require('gulp'),
	sass = require('gulp-sass'),
	debug = require('gulp-debug'),
	batch = require('gulp-batch'),
	watch = require('gulp-watch'),
	uglify = require('gulp-uglify'),
	postcss = require('gulp-postcss'),
	minify = require('gulp-clean-css'),
	purify = require('gulp-purifycss'),
	sequence = require('gulp-sequence'),
	concatenate = require('gulp-concat'),
	sourcemaps = require('gulp-sourcemaps'),
	autoprefixer = require('gulp-autoprefixer'),
	flexbugs = require('postcss-flexbugs-fixes'),

sassets = [
	'../pdx_res/static/sass/vendor/bootstrap/bootstrap.scss',
	'../pdx_res/static/sass/vendor/lightbox.css',
	'../pdx_res/static/sass/*.scss'
];

jsassets = [
	'../pdx_res/static/js/vendor/almond.js',
	'../pdx_res/static/js/vendor/jquery.min.js',
	'../pdx_res/static/js/vendor/tether.js',
	'../pdx_res/static/js/vendor/bootstrap/*.js',
	'../pdx_res/static/js/vendor/lightbox.js',
	'../pdx_res/static/js/vendor/scrollto.js',
	'../pdx_res/static/js/*.js'
];

watchDirs = [
	'../pdx_res/static/sass/**/*.scss',
	'../pdx_res/static/js/vendor/**/*.js',
	'../pdx_res/static/js/*.js'
];


// meta tasks
//
// watcher
gulp.task('watch', function() {
	watch(watchDirs, batch(function(events, done) {
		gulp.start('dev', done);
	}));
});

// prod sequence
gulp.task('default', sequence(
	'scripts', 'uglify', 'styles', 'prefix', 'minify'
));

// dev sequence
gulp.task('dev', function(callback){
 sequence(
	'scripts', 'styles', 'prefix'
	)(callback)
});

// tasks
gulp.task('styles', function() {
	return gulp.src(sassets)
		.pipe(sass().on('error', sass.logError))
		.pipe(postcss([require('postcss-flexbugs-fixes')]))
		.pipe(autoprefixer({
			browsers: ['last 2 versions'],
			cascade: false
		}))
		.pipe(concatenate('main.css'))
		.pipe(gulp.dest('../pdx_res/static/dist'))
})

gulp.task('scripts', function() {
	return gulp.src(jsassets)
		.pipe(concatenate('main.js'))
		.pipe(gulp.dest('../pdx_res/static/dist'))
})

gulp.task('uglify', function() {
	return gulp.src('../pdx_res/static/dist/main.js')
		.pipe(sourcemaps.init())
		.pipe(uglify())
		.pipe(sourcemaps.write('maps'))
		.pipe(gulp.dest('../pdx_res/static/dist'))
})

gulp.task('minify', function() {
	return gulp.src('../pdx_res/static/dist/main.css')
		.pipe(sourcemaps.init())
		.pipe(minify())
		.pipe(sourcemaps.write('maps'))
		.pipe(gulp.dest('../pdx_res/static/dist'))
})

gulp.task('purify', function() {
	return gulp.src('../pdx_res/static/dist/main.css')
		.pipe(purify(['../pdx_res/static/js/vendor/*.js', '../pdx_res/static/js/*.js', '../pdx_res/templates/*.html']))
		.pipe(gulp.dest('../pdx_res/static/dist'))
})

gulp.task('prefix', function() {
	return gulp.src('../pdx_res/static/dist/main.css')
		.pipe(autoprefixer({
			browsers: ['last 3 versions'],
			cascade: false
		}))
		.pipe(gulp.dest('../pdx_res/static/dist'))
})
