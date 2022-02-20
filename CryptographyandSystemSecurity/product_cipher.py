import streamlit as st


# This function generates the key in a cyclic manner until it's length isn't equal to the length of original text

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


# This function returns the encrypted text generated with the help of the key


def cipherText(string, key):

    #------------------------------------Encryption Using Vigenere Cipher------------------------------------#

    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    # return("" . join(cipher_text))
    vignere_cipher = "" . join(cipher_text)
    text = vignere_cipher

    #------------------------------------ Encryption Using Rail Fence Depth = 3 ------------------------------------#

    key = 3
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix
    # to distinguish filled
    # spaces from blank ones
    rail = [['\n'for i in range(len(text))]
            for j in range(key)]

    # to find the direction
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):

        # check the direction of flow reverse the direction if we've just filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1

        # find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))


# This function decrypts the encrypted text and returns the original text

def decryption(cipher, key):

    #------------------------------------ Decryption Using Rail Fence Depth = 3 ------------------------------------#

    key = 3
    # create the matrix to cipher plain text key = rows, length(text) = columns filling the rail matrix to distinguish filled spaces from blank ones
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        # find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

    # now we can construct the fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    # now read the matrix in zig-zag manner to construct the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        # find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # return("".join(result))
    dec_text = "".join(result)

    #------------------------------------Decryption Using Vigenere Cipher------------------------------------#

    cipher_text = dec_text
    keyword = generateKey(cipher_text, "DECEPTIVE")
    orig_text = []
    for i in range(len(cipher_text)):
        x = ((ord(cipher_text[i]) - ord(keyword[i])) + 26) % 26
        x += ord('A')

        orig_text.append(chr(x))
    return("" . join(orig_text))


# Driver code

def main():
    st.title("Text Encryption")
    #st.subheader("Using Vignere Cipher and Rail Fence Technique")
    st.markdown("---")
    st.markdown("### Enter Plaintext ")
    string = st.text_input(label="")
    keyword = "deceptive"           
    string = string.upper()
    keyword = keyword.upper()
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)

    if(st.button("Encrypt")):
        st.write('The Cipher Text is : ', cipher_text)

    st.title("")
    st.title("")
    st.title("Text Decryption")
    #st.subheader("Using Vignere Cipher and Rail Fence Technique")
    st.markdown("---")
    st.markdown("### Enter Ciphertext ")
    cipher_text = st.text_input(label="", key="decryption")

    key = 3
    decryp_text = decryption(cipher_text, key)

    if(st.button("Decrypt")):
        st.write('The Plain Text is : ', decryp_text)


if __name__ == "__main__":
    main()
