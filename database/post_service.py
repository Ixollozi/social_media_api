from database.models import UserPost, Comments, Hashtags, PostPhoto
from database import get_db


# показать все посты


def show_all_posts(main_text, reg_date, post_id):
    db = next(get_db())
    all_posts = db.query(UserPost).filter_by(main_text=main_text, reg_date=reg_date).all()
    if post_id == 1:
        user_post = db.query(UserPost).filter_by(id=post_id)
        return user_post
    return all_posts

# удалить пост


def delete_post(user_post):
    db = next(get_db())
    exact = db.delete(user_post=user_post.id)
    db.commit()
    return exact


# изменить пост


def update_user_post(user_id, new_text):
    db = next(get_db())
    update_post = db.query(UserPost).filter_by(id=user_id)
    update_post.main_text = new_text
    db.commit()
    return update_post

# функция получения комментариев определенного поста function(post_id)


def get_comments(post_id):
    db = next(get_db())
    comments = db.query(UserPost).filter_by(id=post_id).all()
    return comments

# функция публикации коментария function(post_id, user_id, text, reg_date)


def public_comment(post_id, user_id, text, reg_date):
    db = next(get_db())
    new_comment = UserPost(id=post_id, user_id=user_id, text=text, reg_date=reg_date)
    db.add(new_comment)
    db.commit()
    return new_comment

# функция изменения определенного комментария function(comment_id, new_comment_text)


def update_comment(comment_id, new_comment_text):
    db = next(get_db())
    update_comm = db.query(Comments).filter_by(id=comment_id).first()
    update_comm.text = new_comment_text
    db.commit()
    return update_comment

# Удалить определенный комментарий function(comment_id)


def delete_user_comment(comment_id):
    db = next(get_db())
    exact = db.delete(Comments).filter.by(id=comment_id).first()
    db.commit()
    return exact

# функция получения доступных в базе хештегов function(size) list[:size]


def get_hashtags(size):
    db = next(get_db())
    hashtags = db.query(Hashtags).all()
    return hashtags[:size]

# функция получения определенного хештега function(hashtag_name)


def get_user_hashtag(hashtag_name):
    db = next(get_db())
    get_user_tag = db.query(Hashtags).filter_by(hashtag=hashtag_name)
    return get_user_tag


