from random import randint

class RandomNumber:
    def __init__(self, low_num: int, high_num: int):
        """class initializer

        Arguments:
            low_num {int} -- [description]
            high_num {int} -- [description]
        """        
        self.low_num = low_num
        self.high_num = high_num

    def generate(self) -> int:
        """Generate rand number

        Arguments:

        Returns:
            int -- random in range
        """ 
        return randint(self.low_num, self.high_num)