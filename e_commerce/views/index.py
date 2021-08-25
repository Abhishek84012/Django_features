'''CLASS BASED VIEW:- https://ccbv.co.uk/
'''
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.generic import TemplateView


class index(TemplateView):
    """All methods override because we should understand the flow.
    """
    template_name = "index.html"

    def _allowed_methods(self):
        print("Called _allowed_methods")
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

    def dispatch(self, request, *args, **kwargs):
        print("Called dispatch")
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print("Called get")
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        print("Called get_context_data")
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs

    def get_template_names(self):
        print("Called get_template_names")
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            return [self.template_name]

    def http_method_not_allowed(self, request, *args, **kwargs):
        print("CAlled http_method_not_allowed")
        # logger.warning(
        # 'Method Not Allowed (%s): %s', request.method, request.path,
        # extra={'status_code': 405, 'request': request}
        # )
        return HttpResponseNotAllowed(self._allowed_methods())

    def __init__(self, **kwargs):
        print("Callled init")
        """
        Constructor. Called in the URLconf; can contain helpful extra
        keyword arguments, and other things.
        """
        # Go through keyword arguments, and either save their values to our
        # instance, or raise an error.
        for key, value in kwargs.items():
            setattr(self, key, value)

    def options(self, request, *args, **kwargs):
        print("Callled options")
        """Handle responding to requests for the OPTIONS HTTP verb."""
        response = HttpResponse()
        response['Allow'] = ', '.join(self._allowed_methods())
        response['Content-Length'] = '0'
        return response

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        print("Callled render_to_response")
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

    def setup(self, request, *args, **kwargs):
        print("called setup")
        """Initialize attributes shared by all view methods."""
        if hasattr(self, 'get') and not hasattr(self, 'head'):
            self.head = self.get
        self.request = request
        self.args = args
        self.kwargs = kwargs
