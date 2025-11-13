def calculate_score(word, attempts_used, max_attempts, difficulty):
    """Расчет очков"""
    base_score = len(word) * 10
    attempts_bonus = (max_attempts - attempts_used) * 5
    multiplier = {'легкий': 1, 'средний': 2, 'сложный': 3}[difficulty]
    return (base_score + attempts_bonus) * multiplier


def save_score(player, score, word, difficulty):
    """Сохранение счета"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open('scores.txt', 'a', encoding='utf-8') as f:
            f.write(f"{timestamp} | {player} | {difficulty} | {word} | {score}\n")
    except Exception as e:
        print(f"Не удалось сохранить счет: {e}")

def main():
    """Главное меню"""
    show_welcome()

    while True:
        print("\n=== ВИСЕЛИЦА ===")
        print("1 - Новая игра")
        print("2 - Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()