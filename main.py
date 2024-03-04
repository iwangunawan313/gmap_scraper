from botasaurus import *
from botasaurus import bt
import urllib.parse

@browser(
    block_images=True,
)

def scrape_places(driver: AntiDetectDriver, link):

    # Visit an individual place and extract data
    def scrape_place_data():
        driver.get(link)

        # Accept Cookies for European users
        if driver.is_in_page("https://consent.google.com/"):
            agree_button_selector = 'form:nth-child(2) > div > div > button'
            driver.click(agree_button_selector)
            driver.get(link)

        # Extract title
        title_selector = 'h1'
        title = driver.text(title_selector)

        # Extract phone number
        phone_xpath = "//button[starts-with(@data-item-id,'phone')]"
        phone_element = driver.get_element_or_none(phone_xpath)
        phone = phone_element.get_attribute(
            "data-item-id").replace("phone:tel:", "") if phone_element else None

        return {
            "title": title,
            "phone": phone,
        }
    return scrape_place_data()

link = [
            copas linknya di sini
]
     
if __name__ == "__main__":
    # Initiate the web scraping link
    scrape_places(link)
