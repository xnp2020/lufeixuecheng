class Dog:
    def __init__(self, name, type, master, age) -> None:
        self.name = name
        self.type = type
        self.master = master
        self.age = age
        self.say_hi()

    def say_hi(self):
        print(f'我是{self.name}，我的主人是{self.master.name}')


class Person:
    def __init__(self, name, age, sex, relation=None) -> None:
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation


p1 = Person('xxx', 30, 'M')
p2 = Person('yyy', 30, 'F')
d1 = Dog('小黄', '土狗', p1, 2)


class Relationship:
    def __init__(self) -> None:
        self.couple = []

    def make_couple(self, obj1, obj2):
        self.couple.append(obj1)
        self.couple.append(obj2)
        print(f'{obj1.name}和{obj2.name}交往了。')

    def break_up(self, obj):
        if self.couple:

            print(f'{self.couple[0].name}和{self.couple[1].name}分手了。')
            self.couple.clear()
        else:
            print('你没对象你分啥手啊！')

    def get_parter(self, obj):
        if self.couple:
            for i in self.couple:
                if i != obj:
                    return i.name
        else:
            return '你有没有对象你心里没点数吗？还问！'


relation = Relationship()
print(relation.couple)
relation.make_couple(p1, p2)
p1.relation = relation
p2.relation = relation
print(p1.relation.get_parter(p1))
print(p2.relation.get_parter(p2))
relation.break_up(p1)
relation.break_up(p1)

print(p1.relation.get_parter(p1))
# print(p2.relation.get_parter(p2))
