from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic,rating,title):
	article_object = Knowledge(
		topic = topic, 
		rating  = rating,
		title = title)
	session.add(article_object)
	session.commit()

def query_all_articles():
	return session.query(Knowledge).all()




	

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
query_all_articles
add_article("dance",9 , "dancing")
print(query_all_articles())


