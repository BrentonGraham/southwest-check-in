from datetime import datetime
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time_functions import sw_datetime_to_utc


class Reservation():

    def __init__(self, confirm_num, first_name, last_name):

        # Set instance variables
        self.confirm_num = confirm_num
        self.first_name = first_name
        self.last_name = last_name

        # Set driver
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def load_reservation_page(self):
        """
        Loads view reservation web page
        """
        self.driver.get('https://mobile.southwest.com/view-reservation')

    def load_checkin_page(self):
        """
        Loads check-in web page
        """
        self.driver.get('https://mobile.southwest.com/check-in')

    def enter_information(self, submit):
        """
        Enters and submits reservation information. Used when either viewing reservation or check in webpage.
        :param submit: T/F, whether or not the submit button should be clicked
        """
        self.driver.implicitly_wait(10)  # Wait for up to 10sec
        self.driver.find_element('name', 'recordLocator').send_keys(self.confirm_num)  # Enter confirmation number
        self.driver.find_element('name', 'firstName').send_keys(self.first_name)  # Enter first name
        self.driver.find_element('name', 'lastName').send_keys(self.last_name)  # Enter last name

        if submit:
            self.driver.find_element('class name', 'button--yellow').click()  # Click submit button

    def click_submit(self):
        """
        Clicks 'submit' on either reservation or check-in webpage
        """
        self.driver.find_element('class name', 'button--yellow').click()

    def leg(self):
        """
        Determines if user is on first (departing) or second (returning) leg of trip using the current time
        :return: Leg of flight ('departing' or 'returning')
        """
        # Retrieve dates and times for all flights in reservation
        self.driver.implicitly_wait(10)  # Wait for up to 10sec
        dates = self.driver.find_elements('class name', 'flight-day')
        times = self.driver.find_elements('class name', 'flight-time')

        # Parse out dates/times to depart/return and convert to datetime format (UTC)
        depart_datetime = sw_datetime_to_utc(f'{dates[0].text} {times[0].text}')

        # Determine which leg of the trip the passenger is on using datetime logic
        if depart_datetime > datetime.now(tz=pytz.UTC):
            return 'departing'

        else:
            return 'returning'

    def flight_datetime(self, leg):
        """
        :param leg: Leg of flight ('departing' or 'returning')
        :return: Flight time
        """
        # Indices to use for finding elements with the same class name
        leg_index = {'departing': {'date': 0, 'time': 0}, 'returning': {'date': 1, 'time': 2}}

        # Retrieve dates and times for all flights in reservation
        self.driver.implicitly_wait(10)  # Wait for up to 10sec
        dates = self.driver.find_elements('class name', 'flight-day')
        times = self.driver.find_elements('class name', 'flight-time')

        # Get and return leg-specific date and time
        date, time = dates[leg_index[leg]['date']].text, times[leg_index[leg]['time']].text
        return date, time

    def departure_location(self):
        """
        :return: Returns departure location for flight
        """
        self.driver.implicitly_wait(10)  # Wait for up to 10sec if element not found
        departure_location = self.driver.find_element('class name', 'airport-info--detail').text.split(' to\n')[0]
        return departure_location

    def arrival_location(self):
        """
        :return: Returns arrival location for flight
        """
        self.driver.implicitly_wait(10)  # Wait for up to 10sec if element not found
        arrival_location = self.driver.find_element('class name', 'airport-info--detail').text.split(' to\n')[1]
        return arrival_location

