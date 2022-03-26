import models


def test_pawn():
    pawn = models.Pawn("g4", 1)
    assert pawn.position == "g4"
    assert pawn.type == 1


def test_knight():
    knight = models.Knight("a5", 2)
    assert knight.position == "a5"
    assert knight.type == 2


def test_bishop():
    bishop = models.Bishop("g4", 3)
    assert bishop.position == "g4"
    assert bishop.type == 3


def test_rook():
    rook = models.Rook("g4", 4)
    assert rook.position == "g4"
    assert rook.type == 4


def test_queen():
    queen = models.Queen("g4", 5)
    assert queen.position == "g4"
    assert queen.type == 5


def test_king():
    king = models.King("g4", 6)
    assert king.position == "g4"
    assert king.type == 6
