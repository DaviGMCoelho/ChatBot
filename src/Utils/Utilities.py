'''
This module contains utility methods that are not directly related to any specific entity
but are still useful across the aplication.

It includes functionalities such as generating requisition messages.

Classes:
    Utilities: Contains all utils-related methods.

Methods:
    generate_message: 
        Creates a message describing the result
'''
class Utilities:
    '''
    Provides utility methods for general operations
    '''
    def generate_message(self, status: bool, description: str):
        '''
        Generates a requisition message:

        Parameters:
            status (bool): True if the requisition succeeded, False otherwise.
            description (str): Description of what happened.
        Returns:
            dict: Dictionary with the status and description.
        '''
        message = {'status': status, 'message': description}
        return message
