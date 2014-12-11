# -*- coding: utf-8 -*-

class Block:
    blocks = []
    from_id = {}

    def __init__(self, ID, rep='█'):
        self.ID = ID
        self.rep = rep

        Block.blocks.append(self)
        Block.from_id[ID] = self

    def __str__(self):
        return self.rep

    def __repr__(self):
        return self.rep

    def __bool__(self):
        return bool(self.ID)


class Mineral(Block):
    blocks = []
    probs = []

    def __init__(self, ID, strat=range(0, 0), prob=1.0, rep='█'):
        super().__init__(ID, rep)
        self.strat = strat
        self.prob = prob

        Mineral.add_block(self)

    @classmethod
    def add_block(cls, block):
        cls.blocks.append(block)
        cls.probs = []
        for block in cls.blocks:
            cls.probs += [block] * block.prob
        while len(cls.probs) < 1000:
            cls.probs.append(STONE)

# Base blocks
AIR = Block(ID=0, rep=' ')
STONE = Block(ID=1, rep='█')
DIRT = Block(ID=2, rep='▒')
GRASS = Block(ID=3, rep='▓')
COBBLE = Block(ID=4)
STEM = Block(ID=5, rep='H')
LEAVES = Block(ID=6, rep='░')

# Minerals
SAPHIR = Mineral(ID=7, strat=range(0, 10), prob=3, rep='S')
EMERALD = Mineral(ID=8, strat=range(0, 10), prob=3, rep='E')
RUBY = Mineral(ID=9, strat=range(0, 10), prob=3, rep='R')
DIAMOND = Mineral(ID=10, strat=range(0, 3), prob=1, rep='D')
GOLD = Mineral(ID=11, strat=range(0, 7), prob=2, rep='G')