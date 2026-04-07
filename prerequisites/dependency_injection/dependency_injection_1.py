from fastapi import FastAPI, Depends, HTTPException, status

blogs = {
    "1": "FastAPI Prerequisite",
    "2": "Building APIs with FastAPI",
    "3": "Background Tasks | Celery x FastAPI"
}

users = {
    "8": "Jamie",
    "9": "Roman"
}

app = FastAPI(title="Dependency Injection")

def get_blog_or_404(id: str):
    blog = blogs.get(id)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} does not exist",
                            status_code=status.HTTP_404_NOT_FOUND)
    return blog

def get_object_or_404(model: dict, id: str):
    obj = model.get(id)
    if not obj:
        raise HTTPException(detail=f"Blog with id {id} does not exist",
                            status_code=status.HTTP_404_NOT_FOUND)
    return obj

class GetObjectOr404:
    def __init__(self, model) -> None:
        self.model = model

    def __call__(self, id:str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(
                detail=f"Object with id {id} does not exist",
                status_code=status.HTTP_404_NOT_FOUND
            )
        return obj

blog_dependency = GetObjectOr404(blogs)
user_dependency = GetObjectOr404(users)

@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(blog_dependency)):
    return blog_name

@app.get("/user/{id}")
def get_user(user_name: str = Depends(user_dependency)):
    return user_name

# @app.get("/blog/{id}")
# def get_blog(blog_name: str = Depends(get_blog_or_404)):
#     return blog_name