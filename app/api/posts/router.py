from flask import Blueprint
from app.database import get_session
from . import services


router = Blueprint('posts', __name__, url_prefix= '/posts')


@router.get('')
async def get_posts(offset: int = 0, limit: int = 10):
    db = await get_session()

    return await services.get_posts(db, offset, limit)


@router.add('')
async def add_post():
    db = await get_session()

    return await services.add_post(db)


@router.get('/<int:post_id>')
async def get_post(post_id: int):
    db = await get_session()

    return await services.get_post(db, post_id)


@router.put('/<int:post_id>')
async def update_post(post_id: int):
    db = await get_session()

    return await services.update_post(db, post_id)


@router.delete('/<int:post_id>')
async def remove_post(post_id: int):
    db = await get_session()

    return await services.remove_post(db, post_id)
