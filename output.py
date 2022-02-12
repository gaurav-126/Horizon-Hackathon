import web_data_scraper as wds
import custom_input as ci


def hello():
    print(wds.get_location(),wds.get_rain(),wds.alert())
    print(ci.get_location(),ci.get_rain(),ci.alert())
    
hello()