from database import session, TaskORM
from schemas import STaskAdd


class TaskRepository(object):
    @classmethod
    async def add_one(cls, task:STaskAdd) -> int:
        async with session:
            task_dict = task.model_dump() # преобразовываем в словарик

            task = TaskORM(**task_dict) # аргументами будут ключи и значения из словаря
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls):
        query = select(TaskORM)
        result = await session.execute(query)
        task_models = result.scalars().all()
        return task_models
