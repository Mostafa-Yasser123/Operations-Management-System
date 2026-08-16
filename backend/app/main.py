
from fastapi import FastAPI

from app.modules.shifts.router import router as shifts_router
from app.modules.users.router import router as users_router
from app.modules.auth.router import router as auth_router
from app.modules.store.router import router as store_router
from app.modules.equipment.router import router as equipment_router
from app.modules.audit_logs.router import router as audit_logs_router
from app.modules.performance.router import router as performance_router
from app.modules.salary.router import router as salary_router
from app.modules.custody.router import router as custody_router

app = FastAPI(
    title="Operations Management System API",
    version="1.0.0",
    description="Backend API for the Operations Management System"
)


app.include_router(users_router)
app.include_router(auth_router)
app.include_router(store_router)
app.include_router(equipment_router)
app.include_router(audit_logs_router)
app.include_router(shifts_router)
app.include_router(performance_router)
app.include_router(salary_router)
app.include_router(custody_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Operations Management System API"
    }

