from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

def main():

    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")

        page.click('span[class="login pl-2"]')

        page.fill('input[id="username"]', login)
        page.fill('input[id="password"]', password)

        page.click('button[id="loginbtn"]')

        page.goto("https://www.moodle-trebesin.cz/course/view.php?id=277")

        page.click('h3[id="sectionid-3428-title"]')
        page.goto("https://www.moodle-trebesin.cz/mod/quiz/view.php?id=20378")

        page.click('button[class="btn btn-primary"]')
        page.wait_for_timeout(2000)

        #page.goto("https://www.moodle-trebesin.cz/mod/quiz/attempt.php?attempt=2550&cmid=20378")
        
        page.get_by_text("Beautiful Soup").click()
        page.wait_for_timeout(1000)

        page.click('input[id="mod_quiz-next-nav"]')
        page.wait_for_timeout(1000)

        page.get_by_text("JSON").click()
        page.click('input[id="mod_quiz-next-nav"]')
        page.wait_for_timeout(1000)

        page.get_by_text("POST").click()
        page.click('input[id="mod_quiz-next-nav"]')
        page.wait_for_timeout(1000)

        text_element = page.locator('p:text("24+18")')
        text = text_element.text_content()
        number = eval(text)

        text_42 = page.locator('p:text("42")')
        t_42 = int(text_42.text_content())

        if number == t_42:
            page.get_by_text("1405960").click()
            page.wait_for_timeout(1000)

            page.get_by_text("42").click()
            page.wait_for_timeout(500)

            page.get_by_text("44").click()
            page.wait_for_timeout(800)

            page.get_by_text("1405960").click()
            page.wait_for_timeout(700)

            page.get_by_text("42").click()

            page.click('input[id="mod_quiz-next-nav"]')
        else:
            print("chyba")
            
        page.wait_for_timeout(500)
        page.get_by_text("géčko").click()

        page.wait_for_timeout(1000)
        page.click('input[id="mod_quiz-next-nav"]')
        page.wait_for_timeout(1000)

        page.get_by_text("Odeslat vše a ukončit pokus").first.click()
        page.get_by_text("Odeslat vše a ukončit pokus").nth(1).click()






        input("klikni na cokoliv pro zavreni prohlizece")
        browser.close()

if __name__ == "__main__":
    main()
