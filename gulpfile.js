var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var cssmin = require('gulp-cssmin');
var stripComments = require('gulp-strip-css-comments');

var css = [
'./servicedesk/static/bower_components/AdminLTE/bootstrap/css/bootstrap.min.css',
'./servicedesk/static/bower_components/jquery/dist/jquery.datetimepicker.min.css',
'./servicedesk/static/bower_components/AdminLTE/dist/css/AdminLTE.min.css',
'./servicedesk/static/bower_components/fullcalendar/dist/fullcalendar.min.css',
'./servicedesk/static/bower_components/AdminLTE/dist/css/skins/_all-skins.min.css'
];

var js = [
'./servicedesk/static/bower_components/AdminLTE/plugins/jQuery/jquery-2.2.3.min.js',
'./servicedesk/static/bower_components/jquery-mask-plugin/src/jquery.mask.js',
'./servicedesk/static/bower_components/AdminLTE/bootstrap/js/bootstrap.min.js',
'./servicedesk/static/bower_components/jquery/dist/jquery.datetimepicker.full.min.js',
'./servicedesk/static/bower_components/AdminLTE/plugins/fastclick/fastclick.js',
'./servicedesk/static/bower_components/AdminLTE/dist/js/app.min.js',
'./servicedesk/static/bower_components/moment/moment.js',
'./servicedesk/static/bower_components/fullcalendar/dist/fullcalendar.min.js',
'./servicedesk/static/bower_components/fullcalendar/dist/locale-all.js'
];
gulp.task('minify-js', function(){
	gulp.src(js)
	.pipe(concat('allJs.min.js'))
	.pipe(uglify())
	.pipe(gulp.dest('./servicedesk/static'));
});
gulp.task('minify-css', function(){
	gulp.src(css)
	.pipe(concat('allCss.min.css'))
	.pipe(stripComments({all: true}))
	.pipe(cssmin())
	.pipe(gulp.dest('./servicedesk/static'))
});
gulp.task('default', ['minify-css', 'minify-js']);
