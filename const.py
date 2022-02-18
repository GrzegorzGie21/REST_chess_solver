import models

HORIZONTAL_ROWS = ["a", "b", "c", "d", "e", "f", "g", "h"]
VERTICAL_ROWS = [str(i) for i in range(1, 9)]

CHESS_FIELDS = [x + y for x in HORIZONTAL_ROWS for y in VERTICAL_ROWS]

CHESS_FIGURES = {
    "pawn": (1, models.Pawn),
    "knight": (2, models.Knight),
    "bishop": (3, models.Bishop),
    "rook": (4, models.Rook),
    "queen": (5, models.Queen),
    "king": (6, models.King),
}
