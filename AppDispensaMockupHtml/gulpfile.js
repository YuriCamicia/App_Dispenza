var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var cssmin = require('gulp-cssmin');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var runSequence = require('run-sequence');


gulp.task('css', function() {
  gulp.src('assets/scss/main.scss')
    .pipe(sass({outputStyle: 'nested'}).on('error', sass.logError))
    .pipe(autoprefixer({
      browsers: ['last 10 versions'],
      cascade: false
    }))
    .pipe(cssmin())
    .pipe(rename('style.min.css'))
    .pipe(gulp.dest('./build/css/'));

});

// Build frontend stuff
gulp.task('default', function() {
  runSequence('css');
});

// Watch on CSS and JS
gulp.task('watch', function() {
  gulp.watch("assets/scss/*.scss", ['css']);
});
