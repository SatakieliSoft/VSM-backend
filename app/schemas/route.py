from pydantic import BaseModel

class RouteBase(BaseModel):
    name: str
    description: str | None = None
    gpx_file: str | None = None  # názov alebo relatívna cesta k súboru

class RouteCreate(RouteBase):
    pass

class RouteRead(RouteBase):
    id: int

    class Config:
        orm_mode = True
