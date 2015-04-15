#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wangyc'


class Node:
    nodeCount = 0

    def __init__(self, data):
        self.id = int(data['id'])
        self.number = int(data['number'])
        self.name = data['name']
        self.parent = int(data['parent'])
        self.depth = int(data['depth'])
        self.label = int(data['label']) + 1

        if 'vector' in data:
            self.vector = {}
            for pair in data['vector']:
                self.vector[pair[0]] = pair[1]
        else:
            self.vector = {}

        if 'emoji' in data:
            self.emoji = data['emoji']
        else:
            self.emoji = []

        if 'mention' in data:
            self.mention = data['mention']
        else:
            self.mention = []

        if 'hashtag' in data:
            self.hashtag = data['hashtag']
        else:
            self.hashtag = []

        Node.nodeCount += 1

    def setVector(self, _vector):
        self.vector = _vector

    def setEmoji(self, _emoji):
        self.emoji = _emoji

    def setMention(self, _mention):
        self.mention = _mention

    def setHashTag(self, _hashtag):
        self.hashtag = _hashtag

    def toVector(self, length):
        vec = [0 for i in range(length)]
        for index in self.vector:
            assert index - 1 < length
            vec[index - 1] = self.vector[index]
        return vec
