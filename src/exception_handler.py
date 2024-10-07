# Custom exception will be create once and can be used anywhere we want inside our project
import sys


def error_message_details(error,error_details:sys):
    # exc_tb will store the result in which file, which line error has occured.
    _,_,exc_tb=error_details.exc_info() #exc_info has the information about execution
    filename=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno
    error=error
    error_message=f"Error occured in- [{filename}] ,line number- [{line_no}] ,error message- [{error}]"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details)

    def __str__(self) -> str:
        return self.error_message