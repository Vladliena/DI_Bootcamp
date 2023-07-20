def decrypt_matrix(matrix):
    rows = matrix.split('\n')
    num_rows = len(rows)
    num_cols = len(rows[0])

    alpha_chars = [''] * num_cols
    
    for col in range(num_cols):
        for row in range(num_rows):
            char = rows[row][col]
            if char.isalpha():
                alpha_chars[col] += char
    
    for col in range(num_cols):
        alpha_chars[col] = ' '.join([word if word.isalpha() else ' ' for word in alpha_chars[col].split()])
    
    secret_message = ''.join(alpha_chars)
    
    return secret_message

matrix_string = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

secret_message = decrypt_matrix(matrix_string)
print(secret_message)