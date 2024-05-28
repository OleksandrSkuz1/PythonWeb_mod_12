import asyncio
from src.database.db import sessionmanager
from src.entity.models import Base
from src.schemas.contact import ContactSchema
from faker import Faker
from src.entity.models import Contact

fake = Faker()

async def create_fake_contacts(n=100):
    async with sessionmanager.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with sessionmanager.async_session() as session:
        emails_used = set()  # Набір унікальних електронних адрес

        for _ in range(n):
            email = fake.unique.email()  # Генеруємо унікальний електронний адрес
            while email in emails_used:
                email = fake.unique.email()  # Якщо адрес вже використовується, генеруємо новий
            emails_used.add(email)  # Додаємо адрес до набору

            contact_data = ContactSchema(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,
                phone=fake.phone_number(),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=60),
                additional_data=fake.text(max_nb_chars=50)  # Генеруємо рядок до 50 символів
            )
            db_contact = Contact(**contact_data.dict())
            session.add(db_contact)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(create_fake_contacts())

