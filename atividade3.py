#Complete a solução de modo que ela inverta todas as palavras da string passada por parâmetro


def reverseWords(str):
    return " ".join(str.split(" ")[::-1])