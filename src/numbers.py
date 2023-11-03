class mainDisplay:
    def __init__(self):
        self.mainList = []
        for rows in range(5):
            for columns in range(3):
                self.mainList.append('\033[30m█\033[0m')
            self.mainList.append('\n')
    def reset(self):
        self.mainList = []
        for rows in range(5):
            for columns in range(3):
                self.mainList.append('\033[30m█\033[0m')
            self.mainList.append('\n')
            
    def null(self):
        self.display = ""
        for _ in self.mainList:
            self.display += _
        return self.display
    def zero(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[1] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[4] = '\033[32m█\033[0m'
        self.mainList[6] = '\033[32m█\033[0m'
        self.mainList[8] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[12] = '\033[32m█\033[0m'
        self.mainList[14] = '\033[32m█\033[0m'
        self.mainList[16] = '\033[32m█\033[0m'
        self.mainList[17] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'

        for _ in self.mainList:
            self.display += _
        return self.display        
        
    def one(self):
        self.display = ""
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[6] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[14] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'
        for _ in self.mainList:
            self.display += _
        return self.display

    def two(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[1] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[6] = '\033[32m█\033[0m'
        self.mainList[8] = '\033[32m█\033[0m'
        self.mainList[9] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[12] = '\033[32m█\033[0m'
        self.mainList[16] = '\033[32m█\033[0m'
        self.mainList[17] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'
        for _ in self.mainList:
            self.display += _
        return self.display

    def three(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[1] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[6] = '\033[32m█\033[0m'
        self.mainList[8] = '\033[32m█\033[0m'
        self.mainList[9] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[14] = '\033[32m█\033[0m'
        self.mainList[16] = '\033[32m█\033[0m'
        self.mainList[17] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'
        for _ in self.mainList:
            self.display += _
        return self.display

    def four(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[4] = '\033[32m█\033[0m'
        self.mainList[6] = '\033[32m█\033[0m'
        self.mainList[8] = '\033[32m█\033[0m'
        self.mainList[9] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[14] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'
        for _ in self.mainList:
            self.display += _
        return self.display
    
    def five(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[1] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[4] = '\033[32m█\033[0m'
        self.mainList[8] = '\033[32m█\033[0m'
        self.mainList[9] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[14] = '\033[32m█\033[0m'
        self.mainList[16] = '\033[32m█\033[0m'
        self.mainList[17] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'
        for _ in self.mainList:
            self.display += _
        return self.display

    def six(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[1] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[4] = '\033[32m█\033[0m'
        self.mainList[8] = '\033[32m█\033[0m'
        self.mainList[9] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[12] = '\033[32m█\033[0m'
        self.mainList[14] = '\033[32m█\033[0m'
        self.mainList[16] = '\033[32m█\033[0m'
        self.mainList[17] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'

        for _ in self.mainList:
            self.display += _
        return self.display

    def seven(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[1] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[6] = '\033[32m█\033[0m'
        self.mainList[9] = '\033[32m█\033[0m'
        self.mainList[12] = '\033[32m█\033[0m'
        self.mainList[16] = '\033[32m█\033[0m'

        for _ in self.mainList:
            self.display += _
        return self.display

    def eight(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[1] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[4] = '\033[32m█\033[0m'
        self.mainList[6] = '\033[32m█\033[0m'
        self.mainList[8] = '\033[32m█\033[0m'
        self.mainList[9] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[12] = '\033[32m█\033[0m'
        self.mainList[14] = '\033[32m█\033[0m'
        self.mainList[16] = '\033[32m█\033[0m'
        self.mainList[17] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'

        for _ in self.mainList:
            self.display += _
        return self.display

    def nine(self):
        self.display = ""
        self.mainList[0] = '\033[32m█\033[0m'
        self.mainList[1] = '\033[32m█\033[0m'
        self.mainList[2] = '\033[32m█\033[0m'
        self.mainList[4] = '\033[32m█\033[0m'
        self.mainList[6] = '\033[32m█\033[0m'
        self.mainList[8] = '\033[32m█\033[0m'
        self.mainList[9] = '\033[32m█\033[0m'
        self.mainList[10] = '\033[32m█\033[0m'
        self.mainList[14] = '\033[32m█\033[0m'
        self.mainList[18] = '\033[32m█\033[0m'

        for _ in self.mainList:
            self.display += _
        return self.display