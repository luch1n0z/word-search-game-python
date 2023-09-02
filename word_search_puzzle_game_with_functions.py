from random import randint
import time
import pygame

def print_grid(grid):
    separator = '+--+--+--+--+--+--+--+--+--+--+'
    bar = '|'
    for sep in range(10):
        print(separator)
        for col in range(10):
            print(bar, grid[sep][col], end='')
        print(bar)
        print(separator)

def generate_grid(grid):  # create the grid
    separator = '+--+--+--+--+--+--+--+--+--+--+'
    bar = '|'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'z']
    for sep in range(10):
        print(separator)
        for col in range(10):
            letter = letters[randint(0, len(letters) - 1)]
            grid[sep][col] = letter
            print(bar, grid[sep][col], end='')
        print(bar)
        print(separator)
    return grid

def increment_score():
    global total_score
    total_score += 1
    print('Score: ', total_score)

def calculate_row_length(grid):
    for row in grid:
        row_length = len(row)
    return row_length

def generate_grid_with_none(grid):
    for i in range(10):
        rows = [None] * 10
        grid.append(rows)

def last_character_index(word, word_length):
    j = 1
    for i in word:
        if j == word_length:
            return j
        j += 1

def check_word_in_columns(grid, word, victory_sound):
    # CHECK COLUMNS
    for rows in range(10):
        concatenation = ''
        for cols in range(10):
            concatenation += grid[cols][rows]

        if word in concatenation:
            start_row = concatenation.index(word)
            victory_sound.play()
            return [True, start_row]

    return [False, None]

def highlight_columns(grid, start_row, found_word_length, column_length, background_sound, time_up_sound, overall_general_time):
    for offset in range(found_word_length):
        grid[start_row + offset][column_length - found_word_length - start_row] = '*'
    print_grid(grid)
    elapsed_time = time.time()
    time_spent = elapsed_time - overall_general_time
    print('Elapsed time: ', time_spent)
    if time_spent > 10:
        background_sound.stop()
        time_up_sound.play()
        time.sleep(3)
        return True

    return False

def check_word_in_rows(grid, word, victory_sound):
    # CHECK ROWS
    for row in grid:
        concatenated_row = ''.join(row)
        if word in concatenated_row:
            row_index = grid.index(row)
            victory_sound.play()
            return [True, row_index, concatenated_row]

    return [False, None, None]

def highlight_rows(grid, word, victory_sound, overall_general_time):
    return_values = check_word_in_rows(grid, word, victory_sound)
    if return_values[0]:
        row_index = return_values[1]
        concatenated_row = return_values[2]
        victory_sound.play()
        start_col = concatenated_row.index(found_word)

        for row in grid:
            row_index = grid.index(row)
            for offset in range(found_word_length):
                if row_index == row_index:
                    grid[row_index][start_col + offset] = '*'
                else:
                    break
        print_grid(grid)
        elapsed_time = time.time()
        time_spent = elapsed_time - overall_general_time
        print('Elapsed time: ', time_spent)
        if time_spent > 10:
            background_sound.stop()
            time_up_sound.play()
            time.sleep(3)
            return True

    return False

def check_words_in_main_diagonal(grid, word):
    main_diag = ''
    for row in range(10):
        for col in range(10):
            if row == col:
                main_diag += grid[row][col]

    if word in main_diag:
        victory_sound.play()
        return [True, main_diag]

    return [False, None]

def highlight_main_diagonal(grid, word, overall_general_time):
    return_values_check_main_diagonal = check_words_in_main_diagonal(grid, word)

    start_row = return_values_check_main_diagonal[1].index(word)
    start_col = return_values_check_main_diagonal[1].index(word)

    for offset in range(found_word_length):
        grid[start_row + offset][start_col + offset] = '*'

    print_grid(grid)
    elapsed_time = time.time()
    time_spent = elapsed_time - overall_general_time
    print('Elapsed time: ', time_spent)
    if time_spent > 10:
        background_sound.stop()
        time_up_sound.play()
        time.sleep(3)
        return True

    return False

def check_words_in_secondary_diagonal(grid, word):
    # CHECK SECONDARY DIAGONAL
    row_length = calculate_row_length(grid)
    secondary_diag = ''
    for d in range(10):
        secondary_diag += grid[d][row_length - d - 1]

    if word in secondary_diag:
        return [True, secondary_diag]

    return [False, None]

def highlight_secondary_diagonal(grid, word, overall_general_time):
    return_values_check_secondary_diagonal = check_words_in_secondary_diagonal(grid, word)

    start_row = return_values_check_secondary_diagonal[1].index(word)
    start_col = 9 - return_values_check_secondary_diagonal[1].index(word)
    for i in range(found_word_length):
        grid[start_row + i][start_col - i] = '*'

    print_grid(grid)
    elapsed_time = time.time()
    time_spent = elapsed_time - overall_general_time
    print('Elapsed time: ', time_spent)
    if time_spent > 10:
        background_sound.stop()
        time_up_sound.play()
        time.sleep(3)
        return True

    return False

def check_words_in_diagonals_right_of_main_from_top_left_to_bottom_right(grid, word):
    # CHECK DIAGONALS (RIGHT OF MAIN), FROM TOP LEFT TO BOTTOM RIGHT
    for offset in range(1, 10):
        general_diagonal_concatenation_from_left_to_right = ''
        for row in range(10 - offset):
            col = row + offset
            general_diagonal_concatenation_from_left_to_right += grid[row][col]

            if word in general_diagonal_concatenation_from_left_to_right:
                return [True, general_diagonal_concatenation_from_left_to_right]

    return [False, None]

# WORK IN PROGRESS
def highlight_diagonals_right_of_main_from_top_left_to_bottom_right(grid, overall_general_time, word, word_length):
    return_values_check_diagonals_right_of_main_from_top_left_to_bottom_right = \
        check_words_in_diagonals_right_of_main_from_top_left_to_bottom_right(grid, word)
    general_diagonal_concatenation_from_left_to_right = \
        return_values_check_diagonals_right_of_main_from_top_left_to_bottom_right[1]
    last_index = last_character_index(word, word_length)
    indices = []
    start_row = general_diagonal_concatenation_from_left_to_right.index(word)

    start_row = general_diagonal_concatenation_from_left_to_right.index(word) + 1
    end_row = general_diagonal_concatenation_from_left_to_right.rindex(word)
    for i in range(start_row, end_row + 1):
        if i >= start_row + 1 and i <= end_row - 1:
            grid[i][i + 1] = '*'

    print_grid(grid)
    elapsed_time = time.time()
    time_spent = elapsed_time - overall_general_time
    print('Elapsed time: ', time_spent)
    if time_spent > 10:
        background_sound.stop()
        time_up_sound.play()
        time.sleep(3)
        return True

    return False

def check_diagonals_left_of_main(grid, word):
    for offset in range(1, 10):
        general_diagonal_concatenation_from_left_to_right_2 = ''
        for row in range(10 - offset):
            col = row + offset
            general_diagonal_concatenation_from_left_to_right_2 += grid[col][row]

            if word in general_diagonal_concatenation_from_left_to_right_2:
                start_row = general_diagonal_concatenation_from_left_to_right_2.index(word)
                return [True, general_diagonal_concatenation_from_left_to_right_2, start_row]

    return [False, None, None]

# WORK IN PROGRESS
def highlight_diagonals_left_of_main(grid, overall_general_time, word, word_length):
    return_values_check_diagonals_left_of_main = check_diagonals_left_of_main(grid, word)
    diagonal_concatenation_from_left_to_right_2 = return_values_check_diagonals_left_of_main[1]
    start_row = return_values_check_diagonals_left_of_main[2] - 1

    print('start_row:', start_row)
    if check_diagonals_left_of_main(grid, word):
        for i in range(1, word_length + start_row):
            for j in range(start_row, word_length + start_row):
                if j == i + 1:
                    grid[j][i] = '*'
                    print('i: ', i, 'j', j)
                if start_row == 2:
                    if j == i + 2:
                        print('Hello')
                        grid[i][j] = '*'

    print_grid(grid)
    elapsed_time = time.time()
    time_spent = elapsed_time - overall_general_time
    print('Elapsed time: ', time_spent)
    if time_spent > 10:
        time.sleep(3)
        return True

total_score = 0
grid = []
column_length = 10
iteration = 0
pygame.init()
background_sound = pygame.mixer.Sound('C:\\Users\\lucag\\Downloads\\file_example_WAV_1MG.wav')
time_up_sound = pygame.mixer.Sound('C:\\Users\\lucag\\Downloads\\mixkit-retro-arcade-lose-2027.wav')
victory_sound = pygame.mixer.Sound('C:\\Users\\lucag\\Downloads\\short-success-sound-glockenspiel-treasure-video-game-6346 (1).mp3')
background_sound.play(loops=-1)

generate_grid_with_none(grid)
full_grid = generate_grid(grid)  # modify the previous grid with random letters
overall_general_time = time.time()

while True:
    choice = int(input('Enter 0 to play, 1 to exit.\n'))

    if choice == 0:
        overall_time = time.time()
        found_word = input('Enter the word you found\n').lower()

        found_word_length = len(found_word)

        column_word_check_result = check_word_in_columns(full_grid, found_word, victory_sound)
        row_word_check_result = check_word_in_rows(full_grid, found_word, victory_sound)
        main_diagonal_word_check_result = check_words_in_main_diagonal(grid, found_word)
        secondary_diagonal_word_check_result = check_words_in_secondary_diagonal(grid, found_word)
        right_diagonals_word_check_result = check_words_in_diagonals_right_of_main_from_top_left_to_bottom_right(
            grid, found_word)
        left_diagonals_word_check_result = check_diagonals_left_of_main(grid, found_word)
        row_highlight_values = highlight_rows(full_grid, found_word, victory_sound, overall_time)

        if column_word_check_result[0]:
            print('Word found in a column!')
            increment_score()

            if highlight_columns(full_grid, column_word_check_result[1], found_word_length, column_length,
                                 background_sound, time_up_sound, overall_general_time):
                print('Time is up. Exiting the game...')
                break

        elif row_word_check_result[0]:
            print('Word found in a row!')
            increment_score()

            if row_highlight_values:
                print('Time is up. Exiting the game...')
                break

        elif main_diagonal_word_check_result[0]:
            print('Word found in the main diagonal!')
            increment_score()

            if highlight_main_diagonal(full_grid, found_word, overall_general_time):
                print('Time is up. Exiting the game...')
                break

        elif secondary_diagonal_word_check_result[0]:
            print('Word found in the secondary diagonal!')
            increment_score()

            if highlight_secondary_diagonal(full_grid, found_word, overall_general_time):
                print('Time is up. Exiting the game...')
                break

        elif right_diagonals_word_check_result[0]:
            print('Word found in diagonals (right of main) from top left to bottom right!')
            increment_score()

            if highlight_diagonals_right_of_main_from_top_left_to_bottom_right(full_grid, overall_general_time,
                                                                             found_word, found_word_length):
                print('Time is up. Exiting the game...')
                break

        elif left_diagonals_word_check_result[0]:
            print('Word found in diagonals left of the main diagonal!')
            increment_score()

            if highlight_diagonals_left_of_main(full_grid, overall_general_time, found_word, found_word_length):
                print('Time is up. Exiting the game...')
                break

        else:
            print('Word not present in the grid, try again!')
            time_up_sound.play()

    elif choice == 1:
        print('End, total score: ', total_score)
        break

    else:
        time_up_sound.play()
        print('Enter 0 or 1')
        iteration += 1
