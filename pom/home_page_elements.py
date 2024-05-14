

class HomePage:
    def __init__(self, page):
        self.celebrate_header = page.get_by_text("Celebrating Beauty and Style")
        self.celebrate_body = page.get_by_text("playwright-practice was founded by a group of"
                                               " like-minded fashion devotees, dete")
        self.celebrating_beauty_hdr = page.get_by_label("Shoes gallery").locator("a").filter(has_text="Quick View")