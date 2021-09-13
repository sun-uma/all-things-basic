"""
UMS 12/09/2021 - Initial Version
This project takes input from the user_request and writes the details into a
Request_info table. It performs validations on the data and writes the
response to a table Response_info.
"""

from datetime import date, datetime
import logging
import json
import mysql.connector
import mysql.connector.constants

import database_config


class DBConnect:
    """
    This class opens a connection with the database.
    """

    def __init__(self):
        try:
            self.database = mysql.connector.Connect(
                host=database_config.user['host'],
                user=database_config.user['user'],
                password=database_config.user['pass'],
                database=database_config.user['database']
            )
            self.db_cursor = self.database.cursor()
        except mysql.connector.Error as err:
            print(err)


class Request:
    """
    This class takes user_request input using get functions. It inherits
    DBConnect to write into the table Request_info.
    """

    def __init__(self):
        self.db_connection = DBConnect()
        self.__first_name = None
        self.__middle_name = None
        self.__last_name = None
        self.__dob = None
        self.__gender = None
        self.__nationality = None
        self.__current_city = None
        self.__state = None
        self.__pin_code = None
        self.__qualification = None
        self.__salary = None
        self.__pan_number = None
        self.__request_time = None

    def set_first_name(self, first_name: str):
        """ Set first name """
        self.__first_name = first_name

    def set_middle_name(self, middle_name: str):
        """ Set middle name """
        self.__middle_name = middle_name

    def set_last_name(self, last_name: str):
        """ Set last name """
        self.__last_name = last_name

    def set_dob(self, dob: str):
        """ Set date of birth """
        self.__dob = dob

    def set_gender(self, gen: str):
        """ Set gender """
        self.__gender = gen

    def set_nationality(self, nat: str):
        """ Set nationality """
        self.__nationality = nat

    def set_current_city(self, city: str):
        """ Set current city """
        self.__current_city = city

    def set_state(self, state: str):
        """ Set state """
        self.__state = state

    def set_pin_code(self, pin: str):
        """ Set pin code"""
        self.__pin_code = pin

    def set_qualification(self, qualification: str):
        """ Set qualifications """
        self.__qualification = qualification

    def set_salary(self, sal: str):
        """ Set salary """
        self.__salary = sal

    def set_pan_number(self, pan: str):
        """ Set pan number"""
        self.__pan_number = pan

    def set_request_time(self):
        """ Set request time """
        self.__request_time = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')

    def get_first_name(self):
        """ Returns first name """
        return self.__first_name

    def get_middle_name(self):
        """ Returns middle name """
        return self.__middle_name

    def get_last_name(self):
        """ Returns last name """
        return self.__last_name

    def get_dob(self):
        """ Returns date of birth """
        return self.__dob

    def get_gender(self):
        """ Returns gender """
        return self.__gender

    def get_nationality(self):
        """ Returns nationality """
        return self.__nationality

    def get_current_city(self):
        """ Returns current city """
        return self.__current_city

    def get_state(self):
        """ Returns state """
        return self.__state

    def get_pin_code(self):
        """ Returns pin code """
        return self.__pin_code

    def get_qualification(self):
        """ Returns qualifications """
        return self.__qualification

    def get_salary(self):
        """ Returns salary """
        return self.__salary

    def get_pan_number(self):
        """ Returns pan number """
        return self.__pan_number

    def get_request_time(self):
        """ Returns request time """
        return self.__request_time

    def write_request_info(self):
        """ Writes all details into Request_info database """
        logging.info('Inside write_request')
        self.set_request_time()

        new_query = 'INSERT INTO Request_info (first_name, middle_name, last_name, ' \
                    'dob, gender, nationality, current_city, state, pin_code, ' \
                    'qualification, salary, pan_number, request_time) ' \
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        parameters = (self.get_first_name(), self.get_middle_name(), self.get_last_name(),
                      self.get_dob(), self.get_gender(), self.get_nationality(),
                      self.get_current_city(), self.get_state(), self.get_pin_code(),
                      self.get_qualification(), self.get_salary(), self.get_pan_number(),
                      self.get_request_time())
        logging.info(parameters)

        try:
            self.db_connection.db_cursor.execute(new_query, parameters)
            self.db_connection.database.commit()
        except ConnectionError as err:
            print(err)

        logging.info('Successfully written to database')


class Response:
    """
    This class takes an object of Request and performs validation on its attributes.
    It constructs the response in json format and writes to the Response_info database.
    """

    def __init__(self, request: Request):
        self.request = request
        self.request_id = None
        self.response = None

    def get_request_id(self):
        """ Gets request id from Request_info table """
        logging.info('Inside get_request_id')

        new_query = 'SELECT id FROM Request_info WHERE request_time = %s'
        parameter = (self.request.get_request_time(),)
        logging.info(parameter)
        self.request.db_connection.db_cursor.execute(new_query, parameter)

        self.request_id = self.request.db_connection.db_cursor.fetchone()[0]
        self.response = {'Request_id': self.request_id, 'Response': 'Success'}

        return self.request_id

    def validate_required_fields(self):
        """ Ensures all required fields are filled """
        logging.info('Inside validate required fields')

        if self.request.get_first_name() == '' or self.request.get_last_name().strip() == '' \
                or self.request.get_dob().strip() == '' \
                or self.request.get_gender().strip() == '' \
                or self.request.get_nationality().strip() == '' \
                or self.request.get_current_city().strip() == '' \
                or self.request.get_state().strip() == '' \
                or self.request.get_pin_code().strip() == '' \
                or self.request.get_qualification().strip() == '' \
                or self.request.get_salary().strip() == '' \
                or self.request.get_pan_number().strip() == '' \
                or self.request.get_request_time().strip() == '':
            self.response['Reason'] = 'Field cannot be empty'
            return False

        return True

    def validate_dob(self):
        """ Ensures format of DOB """
        logging.info('Inside validate DOB')
        date_string = self.request.get_dob().strip()

        # Length of string
        if len(date_string) < 8:
            self.response['Reason'] = 'Invalid format for DOB'
            return False

        # Format
        if not(date_string[4] == '-' and (date_string[6] == '-' or date_string[7] == '-')):
            self.response['Reason'] = 'Invalid format for DOB'
            return False

        # Three entities (YYYY, MM, DD)
        date_list = date_string.split('-')
        if not len(date_list) == 3:
            self.response['Reason'] = 'Invalid format for DOB'
            return False

        # All input values are numbers
        for each_date in date_list:
            if not each_date.isnumeric():
                self.response['Reason'] = 'Invalid input for DOB'
                return False

        # Input values are valid
        today = date.today()
        if int(date_list[0]) > today.year or int(date_list[0]) < 1920 or int(date_list[1]) > 12 \
                or int(date_list[2]) > 31:
            self.response['Reason'] = 'Invalid input for DOB'
            return False

        return True

    def validate_gender(self):
        """ Ensure valid genders are entered """
        logging.info('Inside validate gender')
        gender_string = self.request.get_gender().strip()

        if not len(gender_string) == 1:
            self.response['Reason'] = 'Invalid input for gender'
            return False

        if not gender_string.upper() in ('M', 'F'):
            self.response['Reason'] = 'Invalid input for gender'
            return False

        return True

    def validate_salary(self):
        """ Ensures valid number is entered"""
        logging.info('Inside validate salary')

        if not self.request.get_salary().strip().isnumeric():
            self.response['Reason'] = 'Invalid input for salary'
            return False

        return True

    def validate_pan(self):
        """ Ensures valid PAN number is entered """
        logging.info('Inside validate pan')

        if not len(self.request.get_pan_number().strip()) == 10:
            self.response['Reason'] = 'Invalid pan number'
            return False

        return True

    def eligible_age(self):
        """ Checks if age is above 21 for male and above 18 for female """
        logging.info('Inside eligible age')
        year, month, day = map(int, self.request.get_dob().split('-'))
        days_lapsed = date.today() - date(year, month, day)
        age = days_lapsed.days / 365
        if age < 21 and self.request.get_gender() == 'M':
            self.response['Reason'] = 'Age below 21'
            return False
        if age < 18 and self.request.get_gender() == 'F':
            self.response['Reason'] = 'Age below 18'
            return False
        return True

    def eligible_last_request(self):
        """ Ensures last request wasn't in last 5 days based on PAN number"""
        logging.info('Inside eligible_last_request')
        new_query = 'SELECT request_time FROM Request_info WHERE pan_number = %s ' \
                    'and Request_time != %s'
        parameter = (self.request.get_pan_number(), self.request.get_request_time())
        try:
            self.request.db_connection.db_cursor.execute(new_query, parameter)
            request_times = self.request.db_connection.db_cursor.fetchall()
            for each_tuple in request_times:
                days_lapse = date.today() - each_tuple[0].date()
                if days_lapse.days < 5:
                    self.response['Reason'] = 'Last request less than 5 days ago'
                    return False
        except mysql.connector.Error as err:
            print(err)
        return True

    def eligible_nationality(self):
        """ Ensures nationality is either American or Indian """
        logging.info('Inside eligible nationality')
        if self.request.get_nationality().lower() != 'indian' \
                and self.request.get_nationality().lower() != 'american':
            self.response['Reason'] = 'Nationality not eligible'
            return False
        return True

    def eligible_state(self):
        """ Ensures state is within given states list """
        logging.info('Inside eligible state')
        states = ['andhra pradesh', 'arunachal pradesh', 'assam',
                  'bihar', 'chhattisgarh', 'karnataka', 'madhya pradesh',
                  'odisha', 'tamil nadu', 'telangana', 'west bengal']
        if self.request.get_state().lower() not in states:
            self.response['Reason'] = 'State not eligible'
            return False
        return True

    def eligible_salary(self):
        """ Ensures salary is between 10000 and 90000"""
        logging.info('Inside eligible salary')
        if int(self.request.get_salary()) < 10000:
            self.response['Reason'] = 'Salary below 10000'
            return False
        if int(self.request.get_salary()) > 90000:
            self.response['Reason'] = 'Salary above 90000'
            return False
        return True

    def write_response_info(self):
        """ Writes response into database Response_info and prints json string """
        logging.info('Inside write response info')
        self.get_request_id()

        # Checking validity
        if not(self.validate_required_fields() and
               self.validate_pan() and self.validate_dob() and
               self.validate_gender() and self.validate_salary()):
            self.response['Response'] = 'Validation failure'

        # Checking eligibility if validation passed
        if not self.response['Response'] == 'Validation failure':
            if not(self.eligible_age() and self.eligible_last_request()
                   and self.eligible_nationality()
                   and self.eligible_state() and self.eligible_salary()):
                self.response['Response'] = 'Failed'

        response_json = json.dumps(self.response)
        print(response_json)

        new_query = 'INSERT INTO Response_info (request_id, response) VALUES (%s, %s)'
        parameters = (self.request_id, response_json)
        logging.info(parameters)
        self.request.db_connection.db_cursor.execute(new_query, parameters)
        self.request.db_connection.database.commit()
        logging.info('Successfully inserted into table Response Info')


if __name__ == '__main__':
    logging.basicConfig(filename='dev_logs.log', filemode='a', level=logging.INFO)
    user_request = Request()

    user_request.set_first_name(input('First name: '))
    user_request.set_middle_name(input('Middle name: '))
    user_request.set_last_name(input('Last name: '))
    user_request.set_dob(input('DOB (YYYY-MM-DD): '))
    user_request.set_gender(input('Gender (M/F): '))
    user_request.set_nationality(input('Nationality: '))
    user_request.set_current_city(input('Current city: '))
    user_request.set_state(input('State: '))
    user_request.set_pin_code(input('Pin code: '))
    user_request.set_qualification(input('Qualification: '))
    user_request.set_salary(input('Salary: '))
    user_request.set_pan_number(input('Pan number: '))

    user_request.write_request_info()

    user_response = Response(user_request)
    user_response.write_response_info()
