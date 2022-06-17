#!/usr/bin/env python3

class Polynomial():
    """ Trida pracuje, provadi operace s polynomy """
    def __init__(self, *args, **keywords):
        """ Zapis hodnot """
        self.args = []
        for i in args:
            if type(i) is list: # zapis hodnot pro list type
                self.args = i
        if not self.args:
            if args: # zapis hodnot pro jednotliva cisla
                self.args = list(args)
            else: # zapis hodnot pres keywords
                for name,value in keywords.items():
                    for i in range(1 + int(name.split("x")[1]) - len(self.args)):
                        self.args.append(0)
                    self.args[int(name.split("x")[1])] = value
        for i in range(len(self.args) - 1, 0, -1):
            if self.args[i] == 0:
                del self.args[i]
            else:
                break      

    def __str__(self):
        """ Formatovani vypisu """
        string=""
        count = len(self.args)
        for i in reversed(range(len(self.args))):
            count -= 1
            if self.args[i] == 0:
                continue
            if self.args[i] > 0:
                string += ' + '
            else:
                string += ' - '
            if self.args[i] != 1 and self.args[i] != -1:
                string += str(abs(self.args[i]))
            if count == 1:
                string += 'x'
            elif count != 0:
                string += 'x^'
                string += str(count)

        return string[3:]

    def __eq__(self, other):
        """ Funkce porovnani """
        if self.args == other.args:
            return True
        return False

    def __add__(self, other):
        """ Funkce skladani """
        if len(self.args) < len(other.args):
            tmp = other.args
            for i in range(len(self.args)):
                tmp[i] = tmp[i] + self.args[i]
        else:
            tmp = self.args
            for i in range(len(other.args)):
                tmp[i] = tmp[i] + other.args[i]

        return Polynomial(tmp)

    def __pow__(self, value):
        """ Funkce umocneni, 
            ale nedokoncil jsem ji"""
        if value == 0:
            tmp = [1]
            return Polynomial(tmp)
        if value == 1:
            return self.args
        if value > 1:
            tmp = self.args
            for i in range(len(tmp)):
                tmp[i] =+ tmp[i] * value
        return Polynomial(tmp)

    def derivative(self):
        """ Funkce derivace """
        tmp = self.args
        count = len(self.args)

        for i in reversed(range(len(tmp))):
            count -= 1
            tmp[i] = tmp[i] * count
        tmp.pop(0)            

        return Polynomial(tmp)

    def at_value(self, value1, *value2):
        """ Funkce vypocta s uvedenym X """
        result = 0
        result2 = 0
        for i, value in enumerate(self.args):
            add = (value1 ** i) * value
            result = result + add
        if value2:
            for i, value in enumerate(self.args):
                add = (value2[0] ** i) * value
                result2 = result2 + add
            result = result2 - result
        return result