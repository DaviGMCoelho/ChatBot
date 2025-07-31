'''
This module contains utility methods that are not directly related to any specific entity
but are still useful across the application.

It includes functionalities such as generating requisition messages.

Classes:
    Utilities: Contains all general-purpose utility methods.
'''
class Utilities:
    '''
    Provides utility methods for the application.

    Methods:
        generate_message(status, description): 
            Generate a dictionary containing the status and description of a request.
    '''
    def generate_message(self, status: bool, description: str):
        '''
        Generates a dictionary representing the result of an operation.

        Parameters:
            status (bool): True if the requisition was successful, False otherwise.
            description (str): A description of the result or issue.

        Returns:
            dict: A dictionary with the status and description.
        '''
        message = {'status': status, 'message': description}
        return message
