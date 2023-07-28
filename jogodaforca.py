import random

def draw_hangman(attempts):
    # partes de desenho da forca
    hangman_parts =[
        """
           --------
          |       |
          |       O
          |      \\|/
          |       |
          |      / \\
          -
        """,
        """
           --------
          |       |
          |       O
          |      \\|/
          |       |
          |      /
          -
        """,
        """
           --------
          |       |
          |       O
          |      \\|/
          |       |
          |
          -
        """,
        """
           --------
          |       |
          |       O
          |      \\|
          |       |
          |
          -
        """,
        """
           --------
          |       |
          |       O
          |       |
          |       |
          |
          -
        """,
        """
           --------
          |       |
          |       O
          |
          |
          |
          -
        """,
        """
           --------
          |       |
          |
          |
          |
          |
          -
        """
    ]

    return hangman_parts[attempts]

def choose_random_word():
    words = ["python", "programming", "computer", "hangman", "game", "keyboard", "mouse", "monitor", "algorithm"]
    return random.choice(words)

def play_game():
    while True:
        secret_word = choose_random_word()
        guessed_letters = set()
        attempts = 6

        print("\nBem-vindo ao Jogo da Forca!")
        while attempts > 0:
            display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
            print("\nPalavra:", display_word)
            print("Letras tentadas:", ', '.join(sorted(guessed_letters)))

            guess = input("Digite uma letra: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Por favor, digite uma única letra.")
                continue

            if guess in guessed_letters:
                print("Você já tentou essa letra.")
                continue

            guessed_letters.add(guess)

            if guess not in secret_word:
                attempts -= 1
                print(draw_hangman(attempts))

            if all(letter in guessed_letters for letter in secret_word):
                print("\nParabéns! Você acertou a palavra:", secret_word)
                break
        else:
            print("\nVocê perdeu! A palavra correta era:", secret_word)

        play_again = input("\nDeseja jogar novamente? (s/n): ").lower()
        if play_again != "s":
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    play_game()