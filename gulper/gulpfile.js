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
	'../static/sass/vendor/bootstrap/bootstrap.scss',
	'../static/sass/vendor/lightbox.css',
	'../static/sass/*.scss'
];

jsassets = [
	'../static/js/vendor/jquery.min.js',
	'../static/js/vendor/tether.js',
	'../static/js/vendor/bootstrap.js',
	'../static/js/vendor/lightbox.js',
	'../static/js/*.js'
];

watchDirs = [
	'../static/sass/**/*.scss',
	'../static/js/vendor/**/*.js',
	'../static/js/*.js'
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
	'scripts', 'uglify', 'styles', 'purify', 'prefix', 'minify'
));

// dev sequence
gulp.task('dev', sequence(
	'scripts', 'styles', 'prefix'
));

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
		.pipe(gulp.dest('../static/dist'))
})

gulp.task('scripts', function() {
	return gulp.src(jsassets)
		.pipe(concatenate('main.js'))
		.pipe(gulp.dest('../static/dist'))
})

gulp.task('uglify', function() {
	return gulp.src('../static/dist/main.js')
		.pipe(sourcemaps.init())
		.pipe(uglify())
		.pipe(sourcemaps.write('maps'))
		.pipe(gulp.dest('../static/dist'))
})

gulp.task('minify', function() {
	return gulp.src('../static/dist/main.css')
		.pipe(sourcemaps.init())
		.pipe(minify())
		.pipe(sourcemaps.write('maps'))
		.pipe(gulp.dest('../static/dist'))
})

gulp.task('purify', function() {
	return gulp.src('../static/dist/main.css')
		.pipe(purify(['../static/js/vendor/*.js', '../static/js/*.js', '../templates/*.html']))
		.pipe(gulp.dest('../static/dist'))
})

gulp.task('prefix', function() {
	return gulp.src('../static/dist/main.css')
		.pipe(autoprefixer({
			browsers: ['last 3 versions'],
			cascade: false
		}))
		.pipe(gulp.dest('../static/dist'))
})
