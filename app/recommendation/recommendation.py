import numpy as np
from app.user_interactions.controller import get_user_interactions
from app.articles.controller import (
    get_articles,
    get_articles_for_user,
    get_articles_with_interactions,
    get_article,
)


def cosine_similarity(dict_a, dict_b):
    # Приводим слова к множеству
    all_terms = set(dict_a.keys()).union(set(dict_b.keys()))

    # Создаем векторы для каждого документа
    vector_a = np.array([dict_a.get(term, 0) for term in all_terms])
    vector_b = np.array([dict_b.get(term, 0) for term in all_terms])

    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


def get_recommendations(
    db,
    left: int,
    right: int,
    user_id,
):

    # Получение TF-IDF для всех документов

    all_documents = get_articles(db)
    # print(all_documents)

    liked_documents = get_articles_for_user(db, user_id)
    # print(liked_documents)

    recommendations = []

    # Получение TF-IDF для документов, которые пользователь лайкнул
    liked_tfidf_vectors = {article.id: article.key_words for article in liked_documents}

    """
    liked_tfidf_vectors = {}
    for article in liked_documents:
        if article[1]:
            updated_data = {
                key: value + (1 - value) / 2
                for key, value in article[0].key_words.items()
            }

            article[0].key_words = updated_data
        else:
            updated_data = {key: value for key, value in article[0].key_words.items()}
            article[0].key_words = updated_data
    """

    # Вычисление косинусного сходства
    if liked_tfidf_vectors:
        for article in all_documents:
            for liked_doc_id, liked_vector in liked_tfidf_vectors.items():
                if liked_doc_id != article.id:
                    similarity = cosine_similarity(liked_vector, article.key_words)
                    if similarity < 0.9999999999:
                        recommendations.append((article.id, similarity))

        # нужны не id а запросы
        recommendations.sort(key=lambda x: x[1], reverse=True)
        # print(recommendations)
        recs = []
        for id, val in recommendations:
            # если мы его еще не лайкнули
            recs.append(get_article(db, id))
        recommendations = recs

    else:
        popular_articles = get_articles_with_interactions(db)
        recommendations = popular_articles
        # холодный старт

    top_n = recommendations[left:right]
    # print(top_n)
    return top_n
