from flask import Blueprint

from .posts.router import router as posts_router


router = Blueprint('api', __name__, url_prefix= '/api')
router.register_blueprint(posts_router)
