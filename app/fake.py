
def generate_fake(count=100):
	from sqlalchemy.exc import IntegrityError
	from random import seed
	import forgery_py
	seed()
	for i in range(count):
		u = User(email=forgery_py.internet.email_address(),
				username=forgery_py.internet.user_name(True),
				password=forgery_py.lorem_ipsum.word(),
				confirmed=True,
				name=forgery_py.name.full_name(),
				location=forgery_py.address.city(),
				about_me=forgery_py.lorem_ipsum.sentence(),
				member_since=forgery_py.date.date(True))
		db.session.add(u)
		try:
			db.session.commit()
		except IntegrityError:
			db.session.rollback()		