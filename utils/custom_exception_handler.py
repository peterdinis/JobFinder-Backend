from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """
    Custom exception handler to provide additional exception handling.
    """
    # Get the standard DRF response
    response = exception_handler(exc, context)

    # Get the exception class name
    exception_class = exc.__class__.__name__

    # Example of custom exceptions
    if exception_class == 'ValidationError':
        custom_response_data = {
            'error': 'Custom validation error message.',
            'details': response.data if response else None,
        }
        response.data = custom_response_data

    elif exception_class == 'NotFound':
        custom_response_data = {
            'error': 'The requested resource was not found.',
            'details': response.data if response else None,
        }
        response.data = custom_response_data

    # Log the exception (use a logging library for production)
    print(f"Exception occurred: {exception_class} | Context: {context}")

    return response