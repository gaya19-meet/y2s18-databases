from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ = "knowledge"
	article_id = Column (Integer, primary_key = True)
	topic = Column(String)
	rating = Column(Integer)
	title = Column(String)
	def __repr__(self):
		return("If you want to learn about {}\n"
			   ", you should look at the Wikipedia article called:{}\n"
			   "We gave this article a rating of {} out of 10!\n").format(
			   self.topic, 
			   self.title ,
			   self.rating)
x = Knowledge(article_id = 1 , topic = "weather" , title = "rainbow" , rating = 9)
print (x)
