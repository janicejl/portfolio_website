import logging

from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class ContactForm(webapp.RequestHandler):
	def post(self):
		sender = "janicejwl-contact <contact@janicejwl.appspotmail.com>"
		to = "Janice Leung <jjw1707@gmail.com>"
		name = self.request.get("name")
		email = self.request.get("email")
		subject = self.request.get("subject")
		body = self.request.get("message")

		content = "--------------------------------------------\nName: " + name + "\nEmail: " + email + "\n--------------------------------------------\n\n"+ body

		message = mail.EmailMessage(sender=sender, subject=subject)
		message.to = to
		message.body = content

		mail.send_mail(sender, to, subject, content)

		logging.info("email sent to " + `to` + " from " + email );
		self.redirect("/contact.html")

	
application = webapp.WSGIApplication(
                                     [('/contactForm', ContactForm)],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()