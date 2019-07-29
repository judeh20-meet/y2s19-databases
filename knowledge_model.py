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
	__tablename__= "Articles"
	article_url= Column(Integer, primary_key =True)
	article_name= Column(String)
	article_topic= Column(String)
	article_rating= Column(Integer)
	def __repr__(self):
		return ("Article Url: {}\n"
			"Article Name: {} \n"
			"Article Topic: {} \n"
			"Article Rating: {}").format(
			self.article_url, self.article_name, self.article_topic, self.article_rating)

Dairy = Knowledge(article_url = "https://en.wikipedia.org/wiki/Cheese", article_name = "Cheese", article_topic = "Cheese", article_rating = 10 )
print(Dairy)