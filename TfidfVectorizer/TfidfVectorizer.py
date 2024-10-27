from collections import defaultdict
from math import log
import numpy as np
import math


def calculate_tfidf_old(text, num_of_tags, mongo):
    # Приводим текст к нижнему регистру и разбиваем на слова
    words = text.lower().split()
    total_words = len(words)

    # Подсчет частоты терминов (TF)
    term_freq = defaultdict(int)
    for word in words:
        # Пропускаем слова длиной 3 символа или меньше
        if len(word) > 3:
            term_freq[word] += 1

    # Подсчет обратной частоты документа (IDF)
    # В данном случае устанавливаем IDF = 1 для всех слов
    idf = {word: 1.0 for word in term_freq}  # Используем IDF = 1

    # Подсчет TF-IDF
    tfidf_scores = {}
    for word, count in term_freq.items():
        tf = count / total_words  # Частота термина
        tfidf_scores[word] = tf * idf[word]  # TF-IDF значение

    # Сортировка по значению TF-IDF
    top_tfidf = []
    for word, score in tfidf_scores.items():
        if len(top_tfidf) < num_of_tags:
            top_tfidf.append((word, score))
        else:
            # Найдем минимальный элемент в текущем списке top_tfidf
            min_index = min(range(len(top_tfidf)), key=lambda i: top_tfidf[i][1])
            # Если текущее значение больше, чем минимальное, заменяем его
            if score > top_tfidf[min_index][1]:
                top_tfidf[min_index] = (word, score)

    return top_tfidf


def calculate_tfidf(text, mongo):
    # Подсчет TF для данного текста
    words = text.lower().split()
    total_words = len(words)
    term_freq = defaultdict(int)

    for word in words:
        if len(word) > 3:  # Пропускаем короткие слова
            term_freq[word] += 1

    tf_scores = {word: count / total_words for word, count in term_freq.items()}
    # print(tf_scores)

    # Подсчет IDF для каждого слова на основе всех документов в базе данных
    idf_scores = {}
    num_documents = mongo.count_documents(
        {}
    )  # Подсчитываем общее количество документов
    # print(num_documents)
    for word in tf_scores.keys():
        # Количество документов, содержащих слово
        doc_count = mongo.count_documents(
            {"text": {"$regex": f"\\b{word}\\b", "$options": "i"}}
        )
        # Вычисляем IDF с добавлением 1 к числителю и знаменателю, чтобы избежать деления на 0
        idf_scores[word] = (
            math.log((num_documents + 1) / (doc_count + 1)) + 1
        )  # +1 к IDF для минимизации 0

    # Подсчет TF-IDF
    tfidf_scores = {word: tf_scores[word] * idf_scores[word] for word in tf_scores}
    print(tfidf_scores)
    return tfidf_scores


def approximate_normal_form(word):
    # 1. Существительные
    # Множественное число, творительный падеж ("ами", "ями")
    if word.endswith("ами") or word.endswith("ями"):
        return word[:-3]
    # Именительный падеж, множественное число ("ы", "и")
    elif word.endswith("ы") or word.endswith("и"):
        return word[:-1]
    # Дательный падеж, единственное число ("е", "у")
    elif word.endswith("е") or word.endswith("у"):
        return word[:-1]
    # Творительный падеж, единственное число ("ой", "ей")
    elif word.endswith("ой") or word.endswith("ей"):
        return word[:-2]

    # 2. Прилагательные
    # Окончания для мужского рода (именительный падеж) - "ый", "ий", "ой"
    elif word.endswith("ый") or word.endswith("ий") or word.endswith("ой"):
        return word[:-2]
    # Окончания для женского рода (именительный падеж) - "ая", "яя"
    elif word.endswith("ая") or word.endswith("яя"):
        return word[:-2] + "ий"  # Например, "красивая" -> "красив"
    # Окончания для среднего рода (именительный падеж) - "ое", "ее"
    elif word.endswith("ое") or word.endswith("ее"):
        return word[:-2] + "ий"  # Например, "красивое" -> "красив"
    # Множественное число, прилагательные - "ые", "ие"
    elif word.endswith("ые") or word.endswith("ие"):
        return word[:-2] + "ий"

    # 3. Глаголы
    # Инфинитивы - "ть", "ти", "чь"
    elif word.endswith("ть") or word.endswith("ти") or word.endswith("чь"):
        return word[:-2]
    # Глаголы настоящего времени, 1-е лицо - "ю", "у"
    elif word.endswith("ю") or word.endswith("у"):
        return word[:-1] + "ть"  # Например, "делаю" -> "дела"
    # Глаголы настоящего времени, 3-е лицо - "ет", "ит", "ют", "ат"
    elif (
        word.endswith("ет")
        or word.endswith("ит")
        or word.endswith("ют")
        or word.endswith("ат")
    ):
        return word[:-2] + "ть"  # Например, "делает" -> "дела"
    # Прошедшее время, мужской род - "л"
    elif word.endswith("л"):
        return word[:-1] + "ть"  # Например, "делал" -> "дела"
    # Прошедшее время, женский и средний род - "ла", "ло"
    elif word.endswith("ла") or word.endswith("ло"):
        return word[:-2] + "ть"  # Например, "делала" -> "дела"
    # Прошедшее время, множественное число - "ли"
    elif word.endswith("ли"):
        return word[:-2] + "ть"  # Например, "делали" -> "дела"

    # Если ни одно правило не подошло, возвращаем исходное слово
    return word
