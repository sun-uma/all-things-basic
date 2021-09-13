from main import Request, Response
import pytest


@pytest.fixture()
def request_obj(request):
    obj = Request()
    obj.set_first_name('XXX')
    obj.set_last_name('YYY')
    obj.set_dob(request.param)
    obj.set_salary('20000')
    obj.set_gender('F')
    obj.set_pan_number('12345')
    obj.set_qualification('MS')
    obj.set_state('Odisha')
    obj.set_nationality('Indian')
    obj.set_current_city('chennai')
    obj.set_pin_code('1234521')
    obj.write_request_info()
    return obj


class TestIt:
    @pytest.mark.parametrize('request_obj', ['2021-09-12', '1974-03-21', '1988-1-1', '1981-04-4', '1982-4-01'])
    def test_validate_DOB_true(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert response_obj.validate_DOB()

    @pytest.mark.parametrize('request_obj', ['0000-00-00', '    -  -  ', '2000/12/12', '2022-02-11', '2012-13-41'],
                             indirect=True)
    def test_validate_DOB(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert not response_obj.validate_DOB()

    @pytest.mark.parametrize('request_obj', ['M', 'F', '  F', 'M   '], indirect=True)
    def test_validate_gender_true(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert response_obj.validate_gender()

    @pytest.mark.parametrize('request_obj', ['Male', 'Female', '1', '$%*(  '], indirect=True)
    def test_validate_gender(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert not response_obj.validate_gender()

    @pytest.mark.parametrize('request_obj', ['20000', '5', '3100000000', '45000    '], indirect=True)
    def test_validate_salary_true(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert response_obj.validate_salary()

    @pytest.mark.parametrize('request_obj', ['10,000', 'abc', '99.99', '-10000'], indirect=True)
    def test_validate_salary(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert not response_obj.validate_salary()

    @pytest.mark.parametrize('request_obj', ['1234512345', 'abcdefabcdef', '@#$%^@#$%^'], indirect=True)
    def test_validate_pan_number_true(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert response_obj.validate_pan()

    @pytest.mark.parametrize('request_obj', ['12345', '#$*@(', 'abcdefghijklmnop'], indirect=True)
    def test_validate_pan_number(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert not response_obj.validate_pan()

    @pytest.mark.parametrize('request_obj', [('M', '2000-1-1'), ('F', '2003-1-1')], indirect=True)
    def test_eligible_age_true(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert response_obj.eligible_age()

    @pytest.mark.parametrize('request_obj', ['2021-09-12', '2016-03-21', '2020-4-01'], indirect=True)
    def test_eligible_age(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert not response_obj.eligible_age()

    @pytest.mark.parametrize('request_obj', ['indian', 'INDIAN', 'American'], indirect=True)
    def test_eligible_nationality_true(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert response_obj.eligible_nationality()

    @pytest.mark.parametrize('request_obj', ['ind', 'US', 'European'], indirect=True)
    def test_eligible_nationality(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert not response_obj.eligible_nationality()

    @pytest.mark.parametrize('request_obj', ['andhra pradesh', 'arunachal Pradesh', 'assam',
                                             'bihar', 'Chhattisgarh', 'KARNATAKA', 'madhya pradesh',
                                             'Odisha', 'tamil  nadu', 'telangana', 'west bengal'], indirect=True)
    def test_eligible_state_true(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert response_obj.eligible_nationality()

    @pytest.mark.parametrize('request_obj', ['AP', 'himachal pradesh', 'TN'], indirect=True)
    def test_eligible_state(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert not response_obj.eligible_state()

    @pytest.mark.parametrize('request_obj', ['10000', '90000', '45000', '10001', '89999'], indirect=True)
    def test_eligible_salary_true(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert response_obj.eligible_salary()

    @pytest.mark.parametrize('request_obj', ['9999', '90001', '0', '100000'], indirect=True)
    def test_eligible_salary(self, request_obj):
        response_obj = Response(request_obj)
        response_obj.get_request_id()
        response_obj.write_response_info()
        assert not response_obj.eligible_salary()
