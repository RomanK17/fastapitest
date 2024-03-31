from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    'sqlite+aiosqlite:///:tasks.db:'
)
session = async_sessionmaker(engine, expire_on_commit=False)()

class Base(DeclarativeBase):
    pass

class TaskORM(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)