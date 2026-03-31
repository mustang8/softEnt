#  18:30
import sys

def create_concordance(file_path, min_word_length, context_size):
    dict_concordance = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        words = [w.lower() for w in words]
        words = [w.strip('.,!?;:"()') for w in words]

        for row, word in enumerate(words):
            if len(word) >= min_word_length:
                if word not in dict_concordance:
                    dict_concordance[word] = []
                start = max(0, row - context_size)
                end = min(len(words), row + context_size + 1)
                context = ' '.join(words[start:end])
                dict_concordance[word].append((row, context))
    return dict_concordance

def print_concordance(concordance):
    for word in sorted(concordance):
        print(f"{word}:")
        for index, context in concordance[word]:
            print(f"{' ':4}Zeile {index+1}: {context}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    input_file = sys.argv[1]
    if sys.argv[2] == '-w' and sys.argv[4] == '-c':
        min_word_length = int(sys.argv[3])
        context_size = int(sys.argv[5])
    else:
        sys.exit(1)
    concordance = create_concordance(input_file, min_word_length=min_word_length, context_size=context_size)
    print_concordance(concordance)
