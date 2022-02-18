from abc import ABC, abstractmethod
import chess

board = chess.Board(fen=None)


class Figure(ABC):
    board = chess.Board(fen=None)

    def __init__(self, position):
        if position not in chess.SQUARE_NAMES:
            self.position = None
        else:
            self.position = position

    @property
    @abstractmethod
    def get_piece(self) -> None:
        return

    def list_available_moves(self) -> list:
        if not self.position:
            return []
        square = chess.parse_square(self.position)
        board.clear_board()
        board.set_piece_at(square, self.get_piece)
        available_moves = [move.uci()[2:4] for move in board.legal_moves]
        return available_moves

    def validate_move(self, dest_field):
        move = "valid" if dest_field in self.list_available_moves() else "invalid"
        return move


class Pawn(Figure):
    def __init__(self, position: str, type: int) -> None:
        super().__init__(position)
        self.type = type

    @property
    def get_piece(self) -> chess.Piece:
        return chess.Piece(self.type, True)


class Knight(Figure):
    def __init__(self, position: str, type: int) -> None:
        super().__init__(position)
        self.type = type

    @property
    def get_piece(self) -> chess.Piece:
        return chess.Piece(self.type, True)


class Bishop(Figure):
    def __init__(self, position: str, type: int) -> None:
        super().__init__(position)
        self.type = type

    @property
    def get_piece(self) -> chess.Piece:
        return chess.Piece(self.type, True)


class Rook(Figure):
    def __init__(self, position: str, type: int) -> None:
        super().__init__(position)
        self.type = type

    @property
    def get_piece(self) -> chess.Piece:
        return chess.Piece(self.type, True)


class Queen(Figure):
    def __init__(self, position: str, type: int) -> None:
        super().__init__(position)
        self.type = type

    @property
    def get_piece(self) -> chess.Piece:
        return chess.Piece(self.type, True)


class King(Figure):
    def __init__(self, position: str, type: int) -> None:
        super().__init__(position)
        self.type = type

    @property
    def get_piece(self) -> chess.Piece:
        return chess.Piece(self.type, True)
