import database as db


async def get_user(telegram_id: int):
    async with db.pool.acquire() as conn:
        return await conn.fetchrow(
            "SELECT * FROM users WHERE user_id = $1", telegram_id
        )


async def create_user(telegram_id: int):
    async with db.pool.acquire() as conn:
        return await conn.fetchrow(
            """
            INSERT INTO users (user_id)
            VALUES ($1)
            RETURNING *
            """,
            telegram_id,
        )


async def get_or_create_user(telegram_id: int):
    user = await get_user(telegram_id)
    if user:
        return user
    return await create_user(telegram_id)


async def update_article(telegram_id: int, article: int):
    async with db.pool.acquire() as conn:
        await conn.execute(
            "UPDATE users SET article = $1 WHERE user_id = $2", article, telegram_id
        )


async def get_article(telegram_id: int):
    async with db.pool.acquire() as conn:
        return await conn.fetchrow(
            """
            SELECT article FROM users WHERE user_id = $1
            """,
            telegram_id,
        )

async def get_all_users():
    async with db.pool.acquire() as conn:
        return await conn.fetch(
            """
            SELECT user_id, article FROM users
            """
        )