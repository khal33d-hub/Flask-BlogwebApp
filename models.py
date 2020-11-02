import pymongo
import datetime
from bson import ObjectId
db = pymongo.MongoClient("mongodb+srv://khal:onaolapo16.@cluster0.ibqpf.gcp.mongodb.net/mydb?retryWrites=true&w=majority").mydb


class PostModel:

    def __init__(self, author="", content="", title=''):
        self.author = author
        self.content = content
        self.title = title
        self.created_date = datetime.datetime.now()

    def save(self):
        """
        insert new post into db
        """
        return db.post.insert(self.__dict__)

    def get_post(self, id):
        """
        get post by id
        return db.post.find_one({"_id": id})
        """
        return db.post. find_one({"_id": ObjectId(id)})

    def get_posts(self):
        """
        get all post
        """
        return list(db.post.find({}))

    def delete_post(self, id):
        """
        remove post by id
        """
        return db.post.delete_one({"_id": ObjectId(id)})

    def update_post(self, id, post):
        """
        update post by id

        """
        return db.post.update({"_id": ObjectId(id)}, post)
