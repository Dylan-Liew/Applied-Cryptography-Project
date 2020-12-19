# 190312k, Dylan Liew, DSF1901
def encrypt(plaintext, key):
    # create the matrix to cipher
    # length(text) = columns ( Number of character in one nested list )
    # plain text key = rows  ( Number of list nested in matrix )
    matrix = [["\n" for i in range(len(plaintext))] for j in range(key)]

    # Add in characters to the matrix
    dir_down = False
    row = 0
    col = 0
    for i in range(len(plaintext)):
        if row == 0 or row == key - 1:
            # Reverse Direction
            dir_down = not dir_down
        matrix[row][col] = plaintext[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    # Obtain Ciphertext from the matrix
    ciphertext= ""
    for i in range(key):
        for j in range(len(plaintext)):
            if matrix[i][j] != '\n':
                ciphertext += matrix[i][j]
    return(ciphertext)


def decrypt(ciphertext, key):
    # create the matrix to cipher
    # length(text) = columns ( Number of character in one nested list )
    # plain text key = rows  ( Number of list nested in matrix )
    matrix = [['\n' for i in range(len(ciphertext))] for j in range(key)]

    dir_down = False
    row, col = 0, 0
    # mark '*' to the places supposed to have character
    for i in range(len(ciphertext)):
        # Adjust Direction Base on Row
        if row == 0 or row == key - 1 :
            # Reverse Direction
            dir_down = not dir_down
        # place the marker
        matrix[row][col] = '*'
        col += 1
        # Adjust Row Base on Direction
        if dir_down:
            row += 1
        else:
            row -= 1

    # fill in the matrix
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if matrix[i][j] == '*' and index < len(ciphertext):
                matrix[i][j] = ciphertext[index]
                index += 1

    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    plainttext = ""
    row, col = 0, 0
    for i in range(len(ciphertext)):
        # Change Direction Base on Current Row
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        # Retrieve the Plaintext Characters
        if matrix[row][col] != '*':
            plainttext += matrix[row][col]
            col += 1
        # Adjust Row Base on Direction
        if dir_down:
            row += 1
        else:
            row -= 1
    return(plainttext)
