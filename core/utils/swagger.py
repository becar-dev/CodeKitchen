# core/utils/swagger.py

from drf_yasg.generators import OpenAPISchemaGenerator

class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self, *args, **kwargs):
        return {
            'Basic': {
                'type': 'basic'
            },
            'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header',
                'description': 'JWT authorization header. Format: Bearer <your_token>'
            }
        }
