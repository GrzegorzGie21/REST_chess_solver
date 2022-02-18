from abc import ABC, abstractmethod
import chess


class Figure(ABC):
    board = chess.Board(fen=None)

    def __init__(self, position):
        if position not in chess.SQUARE_NAMES:
            self.position = None
        else:
            self.position = position

    @abstractmethod
    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        if not self.position or dest_field not in chess.SQUARE_NAMES:
            return "Field does not exist."
        move = chess.Move(
            chess.parse_square(self.position), chess.parse_square(dest_field)
        )
        return move in self.board.legal_moves


class Pawn(Figure):
    pawn = chess.Piece(1, True)

    def list_available_moves(self):
        if not self.position:
            return []
        square = chess.parse_square(self.position)
        self.board.set_piece_at(square, self.pawn)
        print(self.board)
        available_moves = [move.uci()[2:4] for move in self.board.legal_moves]
        return available_moves


class Knight(Figure):
    knight = chess.Piece(2, True)

    def list_available_moves(self):
        if not self.position:
            return []
        square = chess.parse_square(self.position)
        self.board.set_piece_at(square, self.knight)
        available_moves = [move.uci()[2:4] for move in self.board.legal_moves]
        return available_moves


class Bishop(Figure):
    bishop = chess.Piece(3, True)

    def list_available_moves(self):
        if not self.position:
            return []
        square = chess.parse_square(self.position)
        self.board.set_piece_at(square, self.bishop)
        available_moves = [move.uci()[2:4] for move in self.board.legal_moves]
        return available_moves


class Rook(Figure):
    rook = chess.Piece(4, True)

    def list_available_moves(self):
        if not self.position:
            return []
        square = chess.parse_square(self.position)
        self.board.set_piece_at(square, self.rook)
        available_moves = [move.uci()[2:4] for move in self.board.legal_moves]
        return available_moves


class Queen(Figure):
    queen = chess.Piece(5, True)

    def list_available_moves(self):
        if not self.position:
            return []
        square = chess.parse_square(self.position)
        self.board.set_piece_at(square, self.queen)
        available_moves = [move.uci()[2:4] for move in self.board.legal_moves]
        return available_moves


class King(Figure):
    king = chess.Piece(6, True)

    def list_available_moves(self):
        if not self.position:
            return []
        square = chess.parse_square(self.position)
        self.board.set_piece_at(square, self.king)
        available_moves = [move.uci()[2:4] for move in self.board.legal_moves]
        return available_moves
