class Player:
    def retrive(self, cha, username, password, vic, los, eve):
        self.cha = cha
        self.password, self.name = password, username
        self.vic, self.los, self.eve = vic, los, eve
        return self

    def reg(self, cha, password, username):
        if not self.isUserExist(cha, username):
            self.cha = cha
            self.name, self.password = username, password
            self.vic, self.los, self.eve = 0, 0, 0
            with open('players.csv', 'a') as f: #w - change, a - add, x - new
                f.writelines(f'{cha},{username},{password},0,0,0\n')
            return True
        return False

    def isUserExist(self, cha, username):
        with open('players.csv') as f:
            line = f.readline()
            while line != '':
                line = line[:-1 if line[-1]=='\n' else None].split(',') #this gureantee that the last line would be all read
                if line[0] == cha or line[1] == username:
                    return True
                line = f.readline()
        return False

    def log(self, username, password):
        with open('players.csv') as f:
            line = f.readline()
            while line != '':
                line = line[:-1 if line[-1]=='\n' else None].split(',') #this gureantee that the last line would be all read
                if line[1] == username and line[2] == password:
                    self.cha, self.name, self.password = line[0], line[1], line[2]
                    self.vic, self.los, self.eve = int(line[3]), int(line[4]), int(line[5])
                    return True
                line = f.readline()
        return False
    
    def updateData(self):
        f = open('players.csv')
        lines = f.readlines()
        for m in range(len(lines)):
            ate = lines[m][:-1 if lines[m][-1]=='\n' else None].split(',') #this gureantee that the last line would be all read
            if ate[0] == self.cha:
                lines[m] = f'{self.cha},{self.name},{self.password},{self.vic},{self.los},{self.eve}\n'
                f = open('players.csv', 'w')
                f.writelines(lines)
                f.close()
                return True
        return False
        
    def rank(self):
        nick = self.name + "(" + self.cha + ")"
        return f'{nick}{(25-len(nick))*"."}{self.vic}' 

    def __str__(self):
        return self.name + "(" + self.cha + ")"