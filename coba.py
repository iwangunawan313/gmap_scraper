from botasaurus import *
from botasaurus import bt
import urllib.parse
from datetime import datetime
import pandas as pd

def toiso(date):
    return date.isoformat() 

def convert_timestamp_to_iso_date(timestamp):
    # Convert from microseconds to milliseconds
    milliseconds = int(timestamp) / 1000
    # Create a new Date object
    date = datetime.utcfromtimestamp(milliseconds)
    # Return the date in the specified format
    return toiso(date)

@browser(
    parallel= 10,
    block_images=True,
    keep_drivers_alive=True,
    reuse_driver=True,
    close_on_crash=True,
    headless=True,
    output=None
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


@browser(
    data=["ruko in bandung"],
    block_images=True,
    close_on_crash=True,
    headless=True,
    output=None
)
def scrape_places_links(driver: AntiDetectDriver, query):

    # Visit Google Maps
    def visit_google_maps():
        encoded_query = urllib.parse.quote_plus(query)
        url = f'https://www.google.com/maps/search/{encoded_query}'
        driver.get(url)

        # Accept Cookies for European users
        if driver.is_in_page("https://consent.google.com/"):
            agree_button_selector = 'form:nth-child(2) > div > div > button'
            driver.click(agree_button_selector)
            driver.google_get(url)

    # Scroll to the end of the places list to get all the places
    def scroll_to_end_of_places_list():
        end_of_list_detected = False

        while not end_of_list_detected:
            # Element that holds the list of places
            places_list_element_selector = '[role="feed"]'
            driver.scroll(places_list_element_selector)
            print('Scrolling...')

            # Check if we've reached the end of the list
            end_of_list_indicator_selector = "p.fontBodyMedium > span > span"
            if driver.exists(end_of_list_indicator_selector):
                end_of_list_detected = True

        print("Successfully scrolled to the end of the places list.")

    def extract_place_links():
        places_links_selector = '[role="feed"] > div > div > a'
        return driver.links(places_links_selector)

    visit_google_maps()
    scroll_to_end_of_places_list()

    # Get all place links
    places_links = extract_place_links()
    return places_links

data = scrape_places_links()
link = [str(item) for sublist in data for item in sublist]

# Initiate the web scraping link
hasil = scrape_places(link)
scrape_places.close()

# Write the data to the file "data.csv"
#bt.write_csv(hasil, "hasil_scrape.csv")
#bt.write_json(hasil, "hasil_scrape.json")

# Membuat DataFrame
df = pd.DataFrame(hasil)

# Menyimpan DataFrame ke Excel
excel_writer = pd.ExcelWriter('output/hasil_scrape.xlsx')
df.to_excel(excel_writer, sheet_name='Sheet1', index=False)
excel_writer._save()
