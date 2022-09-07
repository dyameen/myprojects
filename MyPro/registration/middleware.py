class NewMiddleware:

    def __init__ (self,get_response):
        self.get_response = get_response

    def __call__ (self,request,*args,**kwargs):
        response = self.get_response (request)
        print('hello!')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print(f'view name: {view_func.__name__}')
        pass
