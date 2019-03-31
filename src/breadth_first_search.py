from collections import deque


def person_is_seller(name):
    """Person is seller"""
    return name[-1] == 'm'


def breadth_first_search(graph):
    """Breadth first search"""
    search_queue = deque()
    search_queue.extend(graph.get('you', []))

    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_is_seller(person):
                return person
            else:
                search_queue.extend(graph.get(person, []))
                searched.append(person)


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

assert breadth_first_search(graph) == 'thom'

graph = {}
assert breadth_first_search(graph) is None
