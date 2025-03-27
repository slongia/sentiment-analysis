# Cosine Similarity in Text

## Vectors and Cosine Similarity in Text Analysis

In text analysis, documents are often represented as vectors in a high-dimensional space, where each dimension corresponds to a unique word or feature from the vocabulary. The value in each dimension typically indicates how frequently or significantly a word occurs in a document.

## How Vectors Represent Text

Consider two simple documents:

Document 1: `"I love artificial intelligence"`

Document 2: `"I enjoy machine learning"`

To convert these documents into vector form, we first identify a vocabulary consisting of all unique words from both documents:

`["I", "love", "enjoy", "artificial", "intelligence", "machine", "learning"]`

We then represent each document by counting the frequency of each word:

| Word         | Doc 1 | Doc 2 |
|--------------|-------|-------|
| I            | 1     | 1     |
| love         | 1     | 0     |
| enjoy        | 0     | 1     |
| artificial   | 1     | 0     |
| intelligence | 1     | 0     |
| machine      | 0     | 1     |
| learning     | 0     | 1     |

Thus, the document vectors are:
- Doc 1 Vector = `[1, 1, 0, 1, 1, 0, 0]`
- Doc 2 Vector = `[1, 0, 1, 0, 0, 1, 1]`

## Cosine Similarity

Cosine similarity measures how similar two vectors are by calculating the cosine of the angle between them. The formula for cosine similarity is:

```math
Cosine Similarity = \frac{A \cdot B}{||A|| \, ||B||} = \frac{\sum_{i=1}^n A_i B_i}{\sqrt{\sum_{i=1}^n A_i^2} \sqrt{\sum_{i=1}^n B_i^2}}
```

Where:
- A and B are vectors
- A · B is the dot product of vectors A and B
- ||A|| and ||B|| are the magnitudes (Euclidean lengths) of vectors A and B

## Calculating Cosine Similarity (Example)

Using the vectors we defined earlier:

### Step 1: Dot Product
Doc 1 Vector = `[1, 1, 0, 1, 1, 0, 0]`

Doc 2 Vector = `[1, 0, 1, 0, 0, 1, 1]`

```
(1 × 1) + (1 × 0) + (0 × 1) + (1 × 0) + (1 × 0) + (0 × 1) + (0 × 1) = 1
```

### Step 2: Magnitudes
Magnitude of Doc 1 Vector:
```math
\sqrt{1^2 + 1^2 + 0^2 + 1^2 + 1^2 + 0^2 + 0^2} = \sqrt{4} = 2
```

Magnitude of Doc 2 Vector:
```math
\sqrt{1^2 + 0^2 + 1^2 + 0^2 + 0^2 + 1^2 + 1^2} = \sqrt{4} = 2
```

### Step 3: Cosine Similarity Calculation
```math
Cosine Similarity = \frac{1}{2 \times 2} = 0.25
```

## Interpretation of Results

Cosine similarity ranges from 0 to 1 (for vectors with non-negative elements):
- 1: Identical vectors (angle = 0°, completely similar)
- 0: Orthogonal vectors (angle = 90°, completely dissimilar)

A cosine similarity of 0.25 indicates these two documents share minimal commonality and are somewhat different but still have a minor overlap (the common word "I").
