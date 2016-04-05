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
        'vendor': {
            'source_filenames': (
              'css/vendor/*.css',
            ),
            'output_filename': 'css/vendor/vendor.css',
        },
        'style': {
            'source_filenames': (
              'css/*.css',
            ),
            'output_filename': 'css/style.css',
        },
    },
    'JAVASCRIPT': {
        'vendor': {
            'source_filenames': (
              'js/vendor/*.js',
            ),
            'output_filename': 'js/vendor/vendor.js',
        },
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
# PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
# PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
