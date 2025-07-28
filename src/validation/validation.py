'''
This module is responsible for common validation methods.

Classes: 
    BaseValidation: A base class containing reusable validation methods.

Methods:
    exists:
        Check if all provided content are non-empty.
    min_length:
        Verifies whether content meets the minimum length requirement.
    equals:
        Verifies if all values in a list match a given reference value.
'''
class BaseValidation:
    '''
    A base class that provides common validation methods for reuse across the system.

    Methods:
        exists(*contents):
            Verifies whether all provided inputs are non-empty and not None.
        min_length(content, length):
            Validates if the content has at least the specified number of characters.
        equals(main_value, to_compare):
            Checks whether all values in a list are equal to a reference value.
    '''
    def exists(self, *contents):
        '''
        Checks whether all provided values are not empty or None.

        Parameters:
            *contents: variable number of inputs to check.

        Returns:
            bool: The result of verification.
        '''
        for content in contents:
            if not content:
                return False
        return True

    def min_length(self, content, length: int):
        '''
        Verifies whether the content meets the minimum legth requirement.

        Parameters:
            content: Input or any data to verify
            length (str): The minimum number of characters allowed.

        Returns:
            bool: True if content meets the length requirement, False otherwise.
        '''
        return len(content) >= length

    def equals(self, main_value, to_compare: list):
        '''
        Checks whether all values in the list are equal to the reference value.

        Parameters:
            main_value : The reference value to compare against.
            to_compare (list): A list of values to validate.

        Returns:
            bool : True if all values match the reference value, False otherwise.
        '''
        for item in to_compare:
            if item != main_value:
                return False
        return True
