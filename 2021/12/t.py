#!/usr/bin/env python3

node = "test"
visited = {"A", "b"}
print(visited | {node} if node == node.lower() else visited, True)

