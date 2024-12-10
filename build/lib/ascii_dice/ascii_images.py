ascii_sides = {
    20: {side: f"""
        _______
      /         \\
     /           \\
    |    {side:2}       |
     \\           /
      \\_________/
    """ for side in range(1, 21)},
    16: {side: f"""
        _______
      /         \\
     /           \\
    |    {side:2}       |
     \\           /
      \\_________/
    """ for side in range(1, 17)},
    12: {side: f"""
        _______
      /         \\
     /    {side:2}     \\
    |             |
     \\           /
      \\_________/
    """ for side in range(1, 13)},
    10: {side: f"""
         ______
        /      \\
       /   {side:2}   \\
      |          |
       \\________/
    """ for side in range(1, 11)},
    8: {side: f"""
        _______
       /       \\
      /    {side:2}    \\
      \\         /
       \\_______/
    """ for side in range(1, 9)},
    6: {side: f"""
      _______
     |       |
     |   {side:1}   |
     |_______|
    """ for side in range(1, 7)},
    4: {side: f"""
         ____
        /    \\
       /  {side:1}   \\
      /_______\\
    """ for side in range(1, 5)}
}
