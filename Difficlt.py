# Словари для разных уровней сложности
WORD_LISTS = {
    'легкий': ['кот', 'дом', 'сад', 'нос', 'рот', 'сон', 'мир', 'час', 'брат', 'цвет'],
    'средний': ['программа', 'компьютер', 'библиотека', 'телефон', 'солнце', 'погода'],
    'сложный': ['электричество', 'достопримечательность', 'самостоятельность', 'благополучие']
}

# Максимальное количество ошибок для каждого уровня
MAX_ATTEMPTS = {'легкий': 8, 'средний': 6, 'сложный': 4}


def get_difficulty():
    """Выбор сложности"""
    print("\nВыберите сложность:")
    print("1 - Легкий (8 попыток)")
    print("2 - Средний (6 попыток)")
    print("3 - Сложный (4 попытки)")

    while True:
        choice = input("Ваш выбор (1-3): ")
        difficulties = {'1': 'легкий', '2': 'средний', '3': 'сложный'}
        if choice in difficulties:
            return difficulties[choice]
        print("Неверный выбор! Введите 1, 2 или 3.")


def display_word(word, guessed_letters):
    """Отображение слова с угаданными буквами"""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

Мизев Евгений, [13.11.2025 22:43]
def play_game():
    """Основная функция игры"""
    difficulty = get_difficulty()
    player_name = input("\nВведите ваше имя: ") or "Игрок"

    word = random.choice(WORD_LISTS[difficulty]).upper()
    max_attempts = MAX_ATTEMPTS[difficulty]
    attempts = 0
    guessed_letters = set()

    print(f"\nИгра началась! Слово из {len(word)} букв. Попыток: {max_attempts}")

    while attempts < max_attempts:
        print(f"\nСлово: {display_word(word, guessed_letters)}")
        print(f"Осталось попыток: {max_attempts - attempts}")
        show_hangman(max_attempts - attempts, max_attempts)

        guess = input("Введите букву: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Верно!")

            # Проверка победы
            if all(letter in guessed_letters for letter in word):
                score = calculate_score(word, attempts, max_attempts, difficulty)
                print(f"\nПоздравляем! Вы угадали слово: {word}")
                print(f"Ваш счет: {score} очков")
                save_score(player_name, score, word, difficulty)
                return
        else:
            attempts += 1
            print("Не угадали!")

    # Проигрыш
    print(f"\nИгра окончена! Загаданное слово: {word}")
    show_hangman(0, max_attempts)
    save_score(player_name, 0, word, difficulty)