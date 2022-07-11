import time
from reservation import Reservation
from time_functions import sw_datetime_to_utc, time_until_checkin, strfdelta


def main():

    confirm_num = '2F8R4W'
    first_name = 'Brenton'
    last_name = 'Graham'

    # Instantiate reservation object
    reservation = Reservation(confirm_num, first_name, last_name)

    # View reservation information
    reservation.load_reservation_page()
    reservation.enter_information(submit=True)

    # Determine flight leg and flight date/time
    leg = reservation.leg()
    flight_date, flight_time = reservation.flight_datetime(leg=leg)
    print(f'\nFlight from {reservation.departure_location()} to {reservation.arrival_location()} '
          f'is scheduled for {flight_time} on {flight_date}...')

    # Open check-in page and enter information
    reservation.load_checkin_page()
    reservation.enter_information(submit=False)  # Wait until exactly 24hr before flight

    # Determine time until check-in
    flight_time_utc = sw_datetime_to_utc(f'{flight_date} {flight_time}')
    wait_time = time_until_checkin(flight_time_utc)
    print(strfdelta(wait_time, "\n{days} days, {hours} hours and {minutes} minutes until check-in."))

    # Sleep until check-in
    #time.sleep(wait_time.total_seconds())
    time.sleep(5)

    # Check-in
    reservation.click_submit()
    print('\nChecked in.')
    time.sleep(5)


if __name__ == "__main__":
   main()