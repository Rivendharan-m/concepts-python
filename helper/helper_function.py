class HelperFunction():

    @staticmethod
    def user_sum(a, b):
        """
        Function to add two numbers.
        
        For docstring test
        >>> HelperFunction.user_sum(2, 3)
        5
        >>> HelperFunction.user_sum(-2, -3)
        5
        """
        
        added_value =  a + b
        if (added_value < 1 ):
            added_value = added_value * -1
        return added_value
    
    @staticmethod   
    def user_multiply(a, b):
        """
        Function to mulitply two numbers 
        
        For docstring test
        >>> HelperFunction.user_multiply(2, 3)
        6
        >>> HelperFunction.user_multiply(-2, -3)
        6
        """
        return a * b
