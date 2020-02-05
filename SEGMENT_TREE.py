#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import sys


class SegmentTree:

    def __init__(self, data):
        self._data = data

        tree_length = self._compute_tree_length()

        self._tree = [0] * tree_length

        self._built_tree(0, len(self._data) - 1, 0)

    def update(self, i, val):
        self._data[i] = val
        self._update(i, 0, len(self._data) - 1, 0)

    def query(self, start, end):
        return self._query(start, end, 0, len(self._data) - 1, 0)

    def _compute_tree_length(self):
        data_length = len(self._data)
        next_power_of_two = int(2 ** math.ceil(math.log(data_length,
                                2)))
        return 2 * next_power_of_two - 1

    def _built_tree(
        self,
        start,
        end,
        position,
        ):
        if start == end:
            self._tree[position] = self._data[start]
        else:
            mid = start + (end - start) / 2
            self._built_tree(start, mid, position * 2 + 1)
            self._built_tree(mid + 1, end, position * 2 + 2)

            self._tree[position] = min(self._tree[position * 2 + 1],
                    self._tree[position * 2 + 2])

    def _query(
        self,
        start,
        end,
        node_start,
        node_end,
        position,
        ):
        if start <= node_start and end >= node_end:

            return self._tree[position]
        elif end < node_start or start > node_end:

            return sys.maxint
        else:

            node_mid = node_start + (node_end - node_start) / 2

            res_left = self._query(start, end, node_start, node_mid,
                                   position * 2 + 1)
            res_right = self._query(start, end, node_mid + 1, node_end,
                                    position * 2 + 2)

            return min(res_left, res_right)

    def _update(
        self,
        i,
        node_start,
        node_end,
        position,
        ):
        if i == node_start and i == node_end:

            self._tree[position] = self._data[i]
        elif node_start <= i <= node_end:

            node_mid = node_start + (node_end - node_start) / 2

            self._update(i, node_start, node_mid, position * 2 + 1)
            self._update(i, node_mid + 1, node_end, position * 2 + 2)

            self._tree[position] = min(self._tree[position * 2 + 1],
                    self._tree[position * 2 + 2])


def test(i, j, st):
    print a[i:j + 1], st.query(i, j)


a = [5, 9, 8, 10, 3]
tree = SegmentTree(a)
test(0, 2, tree)
test(2, 4, tree)
test(0, 4, tree)
test(1, 3, tree)
test(0, 3, tree)
test(1, 4, tree)
test(2, 3, tree)
test(3, 4, tree)
test(0, 1, tree)
test(1, 2, tree)
test(0, 0, tree)
test(1, 1, tree)
test(2, 2, tree)
test(3, 3, tree)
test(4, 4, tree)

tree.update(2, -1)
test(0, 2, tree)
test(2, 4, tree)
test(0, 4, tree)
test(1, 3, tree)
test(0, 3, tree)
test(1, 4, tree)
test(2, 3, tree)
test(3, 4, tree)
test(0, 1, tree)
test(1, 2, tree)
test(0, 0, tree)
test(1, 1, tree)
test(2, 2, tree)
test(3, 3, tree)
test(4, 4, tree)

			
