import os

from .base_setting import PROJECT_DIR


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, "dist", "static")
MEDIA_ROOT = os.path.join(PROJECT_DIR, "dist", "media")

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "fastagram", "static"),
# ]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


PIPELINE = {
    'STYLESHEETS': {
        'style': {
            'source_filenames': (
              'css/*.css',
            ),
            'output_filename': 'css/style.css',
        },
    },
    'JAVASCRIPT': {
        'fastagram': {
            'source_filenames': (
              'js/*.js',
            ),
            'output_filename': 'js/fastagram.js',
        }
    }
}


# PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
# PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
