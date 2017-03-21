import argparse
import sys

punction_marks = [',', '.', '?', '!', '-', ':', '\'']


def is_punction_mark(character):
    for mark in punction_marks:
        if character == mark:
            return True
    return False


def stream_read(stream):
    # При считывании сразу разобьем текст на абзацы
    s = []
    paragraph = ""
    for line in stream:
        line = line.strip()
        if line == '':
            if paragraph == '':
                continue
            s.append(paragraph)
            paragraph = ""
        else:
            paragraph += ' ' + line
    s.append(paragraph)
    return s


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    parser.add_argument("-l", "--line-length", type=int, default=0)
    parser.add_argument("-p", "--paragraph-spaces", type=int, default=0)
    args = parser.parse_args()
    if args.paragraph_spaces < 0 or args.line_length < 0:
        raise "Invalid arguments"
    return args


def main():
    # Парсим аргументы командной строки
    args = parse_arguments()

    # Читаем текст
    if args.input:
        try:
            paragraphs = stream_read(open(args.input))
        except IOError:
            print("IOError")
            sys.exit(1)
    else:
        paragraphs = stream_read(sys.stdin)

    answer = []
    for par in paragraphs:
        # Ставим пробелы вокруг знаков препинания
        for mark in punction_marks:
            par = par.replace(mark, ' ' + mark + ' ')

        # Разделяем текст на куски без пробелов
        words = par.split()

        word_with_punction_marks = ""
        previous_word = ""
        new_list_of_words = []
        num_spaces = args.paragraph_spaces
        for word in words:
            # К первому слову в каждом абзаце добавляем пробелы
            if previous_word == "":
                for i in range(0, num_spaces):
                    previous_word += " "
                previous_word += word
                word_with_punction_marks = previous_word
                continue
            # Присоединяем знаки препинания к словам слева от них
            if (not (is_punction_mark(word)) and
                    is_punction_mark(previous_word)):
                new_list_of_words.append(word_with_punction_marks)
                word_with_punction_marks = word
            elif (is_punction_mark(word) and is_punction_mark(previous_word)):
                word_with_punction_marks += word
            elif (is_punction_mark(word) and not
            (is_punction_mark(previous_word))):
                word_with_punction_marks += word
            else:
                new_list_of_words.append(previous_word)
                word_with_punction_marks = word
            previous_word = word
        new_list_of_words.append(word_with_punction_marks)

        words = new_list_of_words
        max_line_length = args.line_length
        result = ""
        # Соединяем слова в абзац
        for word in words:
            if len(word) > max_line_length:
                raise "Too long word"
            if len(result) + len(word) + 1 <= max_line_length:
                if result == "":
                    result = word
                else:
                    result += " " + word
            else:
                answer.append(result)
                result = word
        answer.append(result)

    # Соединяем абзацы переносами строк
    answer = '\n'.join(answer)

    if args.output:
        try:
            out = open(args.output, "w")
            out.write(answer)
        except IOError:
            print("IOError")
            sys.exit(1)
    else:
        sys.stdout.write(answer)

if __name__ == 'main':
    main()
