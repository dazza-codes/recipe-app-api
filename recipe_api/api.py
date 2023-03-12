from ninja import NinjaAPI
from ninja import Schema


class HelloSchema(Schema):
    name: str = "world"


class UserSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str


class Error(Schema):
    message: str


def create_api_v1() -> NinjaAPI:
    from employees.api import EmployeeView

    api = NinjaAPI(csrf=True, version="1.0.0")

    @api.get("/add")
    def add(request, a: int, b: int):
        return {"result": a + b}

    @api.get("/hello")
    def get_hello(request, name: str = "world"):
        return f"Hello {name}"

    @api.post("/hello")
    def post_hello(request, data: HelloSchema):
        return f"Hello {data.name}"

    @api.get("/user", response={200: UserSchema, 401: Error})
    def get_user(request):
        if not request.user.is_authenticated:
            return 401, {"message": "Please sign in first"}
        return request.user

    api.add_router("", EmployeeView.create_router())

    return api


def api_factory(version: str = "1.0.0") -> NinjaAPI:
    apis = {
        "1.0.0": create_api_v1,
    }
    api_builder = apis[version]
    return api_builder()
