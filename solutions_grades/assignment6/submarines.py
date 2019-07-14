"""
__author__ = Hagai Har-Gil
"""
import numpy as np
from enum import Enum


class Signal(Enum):
    HIT = 'hit'
    MISS = 'miss'
    KILL = 'kill'
    END = 'end'


class GamePiece:
    """ Base class for all game pieces """
    def __init__(self, piece_id: int):
        self.piece_id = piece_id
        self.outline = np.array([0])
        self.locs = None

    @property
    def shape(self):
        return self.outline.shape

    @property
    def filled_outline(self):
        return self.outline * self.piece_id

    def __repr__(self):
        return f"{self.__class__.__name__}{self.piece_id}"


class General(GamePiece):
    """ The deciding piece of the game, num is given as input for compatibility """
    def __init__(self, piece_id: int):
        super().__init__(piece_id)
        self.outline = np.array([[1]], dtype=np.int16)
        self.plane = np.random.randint(3)

    def hit(self, coord):
        return Signal.END


class Jet(GamePiece):
    """ A flying piece in the "sky" plane """
    def __init__(self, piece_id: int):
        super().__init__(piece_id)
        self.outline = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0], [0, 1, 0]], dtype=np.int16)
        self.plane = 2  # air

    def hit(self, coord):
        return Signal.KILL


class Destroyer(GamePiece):
    """ A big battle ship """
    def __init__(self, piece_id: int):
        super().__init__(piece_id)
        self.outline = np.array([[1], [1], [1], [1]], dtype=np.int16)
        self.plane = 1  # Sea-level

    def hit(self, coor_to_pop: tuple):
        coor_to_pop = list(coor_to_pop)
        try:
            self.locs.remove(coor_to_pop)
        except ValueError:
            print(f"Problem with the coordinate {coor_to_pop} - it wasn't found, or was already targeted.")
            return Signal.MISS
        else:
            if len(self.locs) == 0:
                return Signal.KILL
            else:
                return Signal.HIT


class Submarine(GamePiece):
    """ Submerged vessel, a single hit sinks it """
    def __init__(self, piece_id: int):
        super().__init__(piece_id)
        self.outline = np.array([[1, 1, 1]], dtype=np.int16)
        self.plane = 0  # Under the sea

    def hit(self, coord):
        return Signal.KILL


class SubmarinesPieces(Enum):
    """ Allowed types of pieces in the Submarines game"""
    GENERAL = General
    JETS = Jet
    DESTROYERS = Destroyer
    SUBMARINES = Submarine


class ThreeDSubmarinesBoard(np.ndarray):
    """
    A 3D board to hold the pieces
    Inherits from numpy.ndarray to allow for indexing, but one
    could've easily used an array as an attribute of the class
    instead.
    There are 3 "planes" to the board, which are represented by the third dimension.
    Plane 0 is under the sea, plane 1 is at sea-level, and plane 2 is the air.
    The pieces attribute is a list containing all active pieces on the board. Once it's empty
    the game is over.
    """
    def __new__(subtype, shape: tuple=(10, 10, 3), dtype: np.dtype=np.object, *,
                pieces: list):
        if len(shape) != 3:
            return ValueError(f"Shape received was {shape}, but it must have exactly 3 items.")

        obj = super(ThreeDSubmarinesBoard, subtype).__new__(subtype, shape, dtype)
        obj.pieces = pieces
        obj[:] = 0
        return obj

    def __array_finalize__(self, obj):
        """ A unique method which is run after initialization """
        if obj is None: return
        default_pieces = [piece.value(piece_id) for piece_id, piece in enumerate(SubmarinesPieces)]
        self.pieces = getattr(obj, 'pieces', default_pieces)

    def place_pieces(self):
        """
        Place pieces on the board.
        Checks that the piece wasn't placed outside the boundaries of the board,
        and that the cells were empty.
        If indeed so, it places views of the piece object in each cell.
        """
        for piece in self.pieces:
            placed = False
            trial = 0
            while not placed and trial < 50:
                row_idx = np.random.choice(self.shape[0])
                col_idx = np.random.choice(self.shape[1])
                cur_slice = (slice(row_idx, row_idx + piece.shape[0]),
                             slice(col_idx, col_idx + piece.shape[1]),
                             slice(piece.plane, piece.plane + 1))
                try:
                    cur_subboard = self[cur_slice].copy()
                    assert cur_subboard.shape[:2] == piece.shape
                    assert np.all(cur_subboard == 0)  # empty part of the sub-board
                    placed = True
                except (IndexError, AssertionError):  # outside of board boundary
                    pass
                finally:
                    trial += 1

            if trial >= 50:
                raise UserWarning("Board is too small for all pieces.")

            self[cur_slice] += np.atleast_3d(piece.filled_outline)
            piece.locs = np.argwhere(self == piece.piece_id).tolist()
            self[self == piece.piece_id] = piece

    def check_if_hit(self, coord: tuple) -> Signal:
        """
        Receive a 3D coordinate of the location that was targeted.
        Then check the board which piece is there and return the signal.
        :param coord: Tuple of 3 coordinates
        :return: Signal
        """
        cell = self[coord]
        if cell != 0:
            sig = cell.hit(coord)
            if sig is Signal.KILL:
                self.pieces.remove(cell)
                if len(self.pieces) == 1:
                    sig = Signal.END
        else:
            sig = Signal.MISS
        return sig


class SubmarinesGame:
    """
    Play a Submarines game for two players. Run it with the start() method.
    Supply a tuple defining the 3D board size, and adictionary of unit names (from SubmarinesPieces) and values,
    corresponding to the number of units you wish to have of that size.
    At each turn you're prompted to enter a length-3 tuple with the coordinate you're targeting.
    You'll be notified if you missed, hit or killed a unit. You can also write "show" to show the board,
    and "quit" to stop the game.
    """

    def __init__(self, board_shape: tuple=(10, 10, 3), pieces: dict=None):
        self.board_shape = board_shape
        self.pieces = pieces
        self.piece_list_1 = []
        self.piece_list_2 = []

        self.__validate_input()
        self.__generate_pieces_list()

        self.board1 = ThreeDSubmarinesBoard(self.board_shape, pieces=self.piece_list_1)
        self.board2 = ThreeDSubmarinesBoard(self.board_shape, pieces=self.piece_list_2)

        self.players = ("Player 1", "Player 2")
        self.boards = (self.board2, self.board1)
        self.move = 0

    def __validate_input(self):
        assert len(self.board_shape) == 3
        assert self.board_shape[2] == 3  # only 3D inputs
        assert self.board_shape[0] >= 4 and self.board_shape[1] >= 4
        if self.pieces is not None:
            for piece, val in self.pieces.items():
                assert piece in SubmarinesPieces
                assert isinstance(val, int)
                assert val >= 0 and val <= 50
            assert SubmarinesPieces.GENERAL in self.pieces
            assert self.pieces[SubmarinesPieces.GENERAL] == 1

    def __generate_pieces_list(self):
        """ Populate the list of pieces """
        if self.pieces is not None:
            piece_id = 1
            for piece, num in self.pieces.items():
                for cur_instance in range(num):
                    self.piece_list_1.append(piece.value(piece_id))
                    self.piece_list_2.append(piece.value(piece_id))
                    piece_id += 1

    def __assert_coor_in_board(self, coord):
        coor_list = []
        for char in coord:
            if char.isdigit():
                coor_list.append(int(char))
        coord = tuple(coor_list)
        try:
            assert len(coord) == 3
            assert coord[0] < self.board1.shape[0] \
                and coord[1] < self.board1.shape[1] \
                and coord[2] < self.board1.shape[2]
        except AssertionError:
            print(f"Coordinate {coord} is located outside the board. Board shape is {self.board1.shape}.")
            return False
        else:
            return coord

    def __parse_input(self):
        """ Helper function to parse the input from the user """
        coor = input(f"{self.players[self.move % 2]}, what is the coordinate you're targeting (x, y, z)?")
        if coor == 'quit':
            raise SystemExit("Quitting")
        if coor == 'show':
            board = self.boards[(self.move-1) % 2]
            print("Deep:\n", board[..., 0])
            print("Sea-level:\n", board[..., 1])
            print("Air:\n", board[..., 2])
            return False
        coor = self.__assert_coor_in_board(coor)
        return coor

    def start(self):
        """ Start a Submarines game """

        print("Welcome to another game of Submarines!\n")
        print(f"The shape of today's board is {self.board1.shape}.")
        print("You can type 'show' to show your board, and 'quit' to exit the game prematurely.")
        for board in self.boards:
            board.place_pieces()
        print("The pieces were set (randomly), let the game begin!")

        ret_signal = 0

        while ret_signal !=  Signal.END:
            coor = False
            while not coor:
                coor = self.__parse_input()

            ret_signal = self.boards[self.move % 2].check_if_hit(coor)
            print(ret_signal)
            self.move += 1

        print(f"The game is over! The winner is {self.players[(self.move - 1) % 2]}.")


if __name__ == '__main__':
    pieces = {SubmarinesPieces.GENERAL: 1,
              SubmarinesPieces.JETS: 1,
              SubmarinesPieces.DESTROYERS: 1,
              SubmarinesPieces.SUBMARINES: 1}
    subgame = SubmarinesGame(board_shape=(4, 4, 3), pieces=pieces)
    subgame.start()
