from fastapi import HTTPException, status


def safe(address):
    def wrapper(function):
        def _(*args, **kwargs):
            try:
                func=function(*args, **kwargs)
                return func
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        return _
    return wrapper