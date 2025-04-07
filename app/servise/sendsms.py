from typing import Type, Any, Callable
import requests
import json
from config.settings import setting


class SendMassage:
    __slots__ = ('context', "phone_number", "pattern",)

    @staticmethod
    def _validation_field(field_type: Type,
                          value: Any,
                          default_value: Any = None,
                          validator: Callable = None, ) -> Any:
        assert not validator or callable(validator), 'Validator must be callable!'
        assert value or default_value is not None, 'default_value must be None !'
        value = value or default_value
        assert isinstance(value, field_type), 'value must be {}!'.format(field_type)
        assert not validator or validator(value), 'Validator Error'
        return value

    def __init__(self, massage: str,
                 phone: str,
                 pattern: str = setting.OTP_PATTERN_CODE):
        self.context = self._validation_field(str, massage)
        self.phone_number = self._validation_field(str, phone)
        self.pattern = self._validation_field(str, pattern)

    def send(self):
        payload = json.dumps({
            "code": self.pattern,
            "sender": setting.OTP_PHONE,
            "recipient": self.phone_number,
            "variable": {
                "massage": self.context
            }
        })
        headers = {
            'accept': '*/*',
            'apikey': setting.OTP_APIKEY,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", setting.OTP_UTL, headers=headers, data=payload)
        del self
        return response.text
