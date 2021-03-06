from .ChessPiece import ChessPiece, find_chess_piece  

class Bishop(ChessPiece):
  def __init__(self,x,y,color):
    super().__init__(x,y,color)

  def __check_northeast(self, chess_pieces):
    for x in range(self.x+1,len(chess_pieces)):
      y = self.y + abs(self.x-x)

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return 1
        else:
          return 0

    return 0

  def __check_southeast(self, chess_pieces):
    for x in range(self.x+1,len(chess_pieces)):
      y = self.y - abs(self.x-x)

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return 1
        else:
          return 0

    return 0
  
  def __check_southwest(self, chess_pieces):
    for x in range(self.x-1,-1,-1):
      y = self.y - abs(self.x-x)

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return 1
        else:
          return 0

    return 0

  def __check_northwest(self, chess_pieces):
    for x in range(self.x-1,-1,-1):
      y = self.y + abs(self.x-x)

      chess_piece = find_chess_piece(chess_pieces,x,y)
      if (chess_piece != None):
        if (self.is_color_different(chess_piece)):
          return 1
        else:
          return 0

    return 0

  def count_attacked_pawns(self,chess_pieces):
    attacked_pawns = 0
    attacked_pawns += self.__check_northeast(chess_pieces)
    attacked_pawns += self.__check_southeast(chess_pieces)
    attacked_pawns += self.__check_northwest(chess_pieces)
    attacked_pawns += self.__check_southwest(chess_pieces)

    return attacked_pawns

