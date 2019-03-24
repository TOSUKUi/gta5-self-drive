
class PipeLine:
    # def add(self, procedure):
    #    return self.__init__(self.procedures + [procedure])

    def execute(self, procedures, inputs=None):
        if procedures:  
            next_inputs = procedures[0].run(inputs)
            return self.execute(procedures[1:], next_inputs)
        return inputs
