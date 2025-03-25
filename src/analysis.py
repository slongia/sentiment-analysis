import math

# Step 1: Dataset Preparation
positive_sentences = [
    "I love this movie",
    "This is fantastic",
    "Excellent service and great atmosphere",
]

negative_sentences = [
    "I hate this movie",
    "This is terrible",
    "Horrible experience will never return",
]


# Step 2: Tokenization
def tokenize(sentence):
    return sentence.lower().split()


# Build Vocabulary
def build_vocab(sentences):
    vocab = {}
    idx = 0
    for sentence in sentences:
        for word in tokenize(sentence):
            if word not in vocab:
                vocab[word] = idx
                idx += 1
    return vocab


all_sentences = positive_sentences + negative_sentences
vocab = build_vocab(all_sentences)


# Step 3: Embedding Initialization
# (Random embeddings initialization)
def initialize_embeddings(vocab, dim=3):
    embeddings = {}
    for word in vocab:
        # simple deterministic "pseudo-random" embeddings
        embeddings[word] = [(len(word) + i) % 5 * 0.1 for i in range(dim)]
    return embeddings


embeddings = initialize_embeddings(vocab)


# Step 4: Convert sentence to embedding - average embeddings
def sentence_embedding(sentence, embeddings):
    tokens = tokenize(sentence)
    embed_dim = len(next(iter(embeddings.values())))
    embed_sum = [0.0] * embed_dim
    for token in tokens:
        if token in embeddings:
            for i in range(embed_dim):
                embed_sum[i] += embeddings[token][i]
    return [x / len(tokens) for x in embed_sum]


# Step 5: Training - building class centroids
def compute_centroid(sentences, embeddings):
    centroid = [0.0] * len(next(iter(embeddings.values())))
    for sentence in sentences:
        emb = sentence_embedding(sentence, embeddings)
        for i in range(len(emb)):
            centroid[i] += emb[i]
    return [x / len(sentences) for x in centroid]


positive_centroid = compute_centroid(positive_sentences, embeddings)
negative_centroid = compute_centroid(negative_sentences, embeddings)


# Step 6: Prediction - Cosine Similarity
def cosine_similarity(vec1, vec2):
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    mag1 = math.sqrt(sum(v1**2 for v1 in vec1))
    mag2 = math.sqrt(sum(v2**2 for v2 in vec2))
    if mag1 * mag2 == 0:
        return 0
    return dot_product / (mag1 * mag2)


def predict(sentence, embeddings, pos_centroid, neg_centroid):
    emb = sentence_embedding(sentence, embeddings)
    pos_score = cosine_similarity(emb, pos_centroid)
    neg_score = cosine_similarity(emb, neg_centroid)
    return "Positive" if pos_score >= neg_score else "Negative"


# Step 7: Deployment
def deploy():
    print("Sentiment Analysis (Type 'exit' to quit)")
    while True:
        user_input = input("\nEnter sentence: ")
        if user_input.lower() == "exit":
            break
        sentiment = predict(
            user_input, embeddings, positive_centroid, negative_centroid
        )
        print(f"Sentiment: {sentiment}")


# Run deployment
if __name__ == "__main__":
    deploy()
