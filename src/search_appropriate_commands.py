import re

from collections import defaultdict
from load_from_yaml import import_data_from_yaml_file

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children: return False
            cur = cur.children[c]
        return cur.endOfWord
    

def search_command_by_name(command_name_input: str) -> bool:
    yaml_data = import_data_from_yaml_file()
    commands_trie = Trie()

    for command in yaml_data:
        commands_trie.insert(command)

    command_existence: bool = commands_trie.search(command_name_input)
    return True if command_existence else False


def create_commands_and_description_dict(yaml_data: dict = import_data_from_yaml_file()) -> dict:
    commands_and_description_dict = {}
    for command, details in yaml_data.items():
        command_description: str = details['description'].lower()
        commands_and_description_dict[command] = command_description
    
    return commands_and_description_dict

def initialize_inverted_index() -> dict:
    commands_and_description_dict = create_commands_and_description_dict()

    #building inverted index
    inverted_index = defaultdict(list)

    for command_name, command_description in commands_and_description_dict.items():
        words = command_description.lower().split()
        for word in set(words):
            inverted_index[word].append(command_name)

    return inverted_index

def search_for_commands(user_query_input: str) -> list:
    query_words = user_query_input.lower().split()
    results = None
    inverted_index = initialize_inverted_index()

    for word in query_words:
        if word in inverted_index:
            if results is None: results = set(inverted_index[word])
            else: results &= set(inverted_index[word])
        else: return []

    return list(results) if results else []