from fastapi.staticfiles import StaticFiles


class CustomStaticFiles(StaticFiles): 
    async def get_response(self, path: str, scope): 
        response = await super().get_response(path, scope) # Add your custom logic here return response
        return response