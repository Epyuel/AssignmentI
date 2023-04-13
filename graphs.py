import graph_generator as gg
class Romenia:
    def __init__(self):
        self.romenia=gg.Graph()
        
    def add(self):
        self.romenia.add("Oradea","Zerind",71)
        self.romenia.add("Oradea","Sibiu",151)
        self.romenia.add("Zerind","Arad",75)
        self.romenia.add("Arad","Timisoara",118)
        self.romenia.add("Arad","Sibiu",140)
        self.romenia.add("Sibiu","Fagaras",99)
        self.romenia.add("Sibiu","Rimnicu Vilcea",80)
        self.romenia.add("Fagaras","Bucharest",211)
        self.romenia.add("Timisoara","Lugoj",111)
        self.romenia.add("Rimnicu Vilcea","Craiova",146)
        self.romenia.add("Rimnicu Vilcea","Pitesti",97)
        self.romenia.add("Lugoj","Mehadia",70)
        self.romenia.add("Pitesti","Bucharest",101)
        self.romenia.add("Pitesti","Craiova",138)
        self.romenia.add("Urziceni","Bucharest",85)
        self.romenia.add("Urziceni","Hirsova",98)
        self.romenia.add("Urziceni","Vaslui",142)
        self.romenia.add("Hirsova","Eforie",86)
        self.romenia.add("Mehadia","Drobeta",75)
        self.romenia.add("Drobeta","Craiova",120)       
        self.romenia.add("Bucharest","Giurgiu",90)
        self.romenia.add("Vaslui","Iasi",92)
        self.romenia.add("Iasi","Neamt",87)


# a=Romenia()
# a.add()
# print(a.romenia.graph)


