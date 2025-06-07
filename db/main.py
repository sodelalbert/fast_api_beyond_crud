from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import CONFIG


engine = AsyncEngine(
    create_engine(
        url=CONFIG.DATABASE_URL,
        echo=True,
    )
)


async def init_db():
    """
    Initialize the database connection.
    This function can be used to create tables or perform initial setup.
    """
    async with engine.begin() as conn:
        # Here you can create tables or perform other setup tasks
        statement = text("Select 'hello';")
        result = await conn.execute(statement)
        print(result.all())
    print("Database initialized.")
