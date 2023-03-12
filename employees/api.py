from datetime import date

from django.shortcuts import get_object_or_404
from ninja import Router
from ninja import Schema

from employees.models import Employee


class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None


class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None


class Error(Schema):
    message: str


class EmployeeView:
    model = Employee
    schema_in = EmployeeIn
    schema_out = EmployeeOut

    @classmethod
    def get(cls, pk: int):
        return get_object_or_404(cls.model, id=pk)

    @classmethod
    def put(cls, pk: int, payload: EmployeeIn) -> dict[str, bool]:
        record = get_object_or_404(cls.model, id=pk)
        for attr, value in payload.dict().items():
            setattr(record, attr, value)
        record.save()
        return {"success": True}

    @classmethod
    def delete(cls, pk: int) -> dict[str, bool]:
        record = get_object_or_404(cls.model, id=pk)
        record.delete()
        return {"success": True}

    @classmethod
    def create_router(cls) -> Router:
        api = Router()

        @api.get("/employees", response=list[cls.schema_out])
        def list_objects(request):
            return cls.model.objects.all()

        @api.post("/employees")
        def create_object(request, payload: cls.schema_in):
            employee = cls.model.objects.create(**payload.dict())
            return {"id": employee.id}

        @api.get("/employees/{employee_id}", response=cls.schema_out)
        def get_object(request, employee_id: int):
            return cls.get(pk=employee_id)

        @api.put("/employees/{employee_id}")
        def update_object(request, employee_id: int, payload: cls.schema_in):
            return cls.put(pk=employee_id, payload=payload)

        @api.delete("/employees/{employee_id}")
        def delete_object(request, employee_id: int):
            return cls.delete(pk=employee_id)

        return api
