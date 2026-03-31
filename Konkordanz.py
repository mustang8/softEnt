#  18:30-20:45 
import sys

def create_concordance(file_path, min_word_length, context_size):
    dict_concordance = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for row, line in enumerate(file, start=1):
            line = line.strip()
            words = line.split()
            words = [w.lower() for w in words]
            words = [w.strip('.,!?;:"()') for w in words]

            for index, word in enumerate(words):
                if len(word) >= min_word_length:
                    if word not in dict_concordance:
                        dict_concordance[word] = []
                    start = max(0, index - context_size)
                    end = min(len(words), index + context_size + 1)
                    context = ' '.join(words[start:end])
                    dict_concordance[word].append((row, context))
    return dict_concordance

def print_concordance(concordance):
    for word in sorted(concordance):
        print(f"{word}:")
        for row, context in concordance[word]:
            print(f"{' ':4}Zeile {row}: {context}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    min_word_length = 3
    context_size = 1
    input_file = sys.argv[1]
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '-w':
            min_word_length = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == '-c':
            context_size = int(sys.argv[i + 1])
            i += 2
        else:
            i += 1
concordance = create_concordance(input_file, min_word_length=min_word_length, context_size=context_size)
print_concordance(concordance)
