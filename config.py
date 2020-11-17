import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or "kanjurus"
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///"+ os.path.join(base_dir, 'massage.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False