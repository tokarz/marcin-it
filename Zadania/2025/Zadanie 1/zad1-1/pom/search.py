


class SearchPage :
    def __init__(self , page):
        self.page = page
        self.page_search_imput = page.get_by_label("Szukaj", exact=True)

    def navigate(self):
        self.page.goto("https://www.google.com/")
        self.page.get_by_role("button", name="Zaakceptuj wszystko").click()

    def search(self , text):
        self.page_search_imput.fill(text)
        self.page_search_imput.press("Enter")

