
# TODO: IMPORTANT! Watch sections on pytest and fixture, and Data Driven testing before building POM for entire app!
# TODO: Fixtures are ideal for any repetitive steps in the beginning or the end of tests
# TODO: Use POM helper methods only for repetitive steps in the middle of your tests

class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):   # fixture is better suited for this task
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, name, address, email, phone, subj, message):
        self.page.fill("[placeholder=\"Enter your name\"]", name)
        self.page.fill("[placeholder=\"Enter your address\"]", address)
        self.page.fill("[placeholder=\"Enter your email\"]", email)
        self.page.fill("[placeholder=\"Enter your phone number\"]", phone)
        self.page.fill("[placeholder=\"Type the subject\"]", subj)
        self.page.fill("textarea", message)
        # self.page.press('[aria-label="Enter your search term"]', "Enter")
