from sqlalchemy import text

from app.database.session import engine
from app.modules.users.model import User

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        print("Database connection successful ✅")
        print(result.fetchone())

except Exception as e:
    print("Database connection failed ❌")
    print(e)

print(User.__tablename__)