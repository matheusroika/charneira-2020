class BaseConfig():
    DEPLOY = True
    CSP = {
        'default-src': ['\'self\'',
                    '\'unsafe-inline\'',
                    '\'unsafe-eval\'',
                    'cdnjs.cloudflare.com',
                    'code.jquery.com',
                    'cdn.jsdelivr.net',
                    'stackpath.bootstrapcdn.com',
                    '*.fontawesome.com',
                    'www.google.com',
                    '*.googleanalytics.com',
                    '*.google-analytics.com',
                    '*.googleapis.com',
                    'www.googletagmanager.com',
                    '*.gstatic.com',
                    '*.youtube.com',
                    'data:']
    }

    if DEPLOY:
        ENV = 'production'
        DEBUG = False
        uri = 'charneira.com.br'
    else:
        ENV = 'development'
        DEBUG = True
        uri = 'localhost'