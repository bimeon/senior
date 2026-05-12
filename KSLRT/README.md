# 🤟 Korean Sign Language Recognition & Translation

> **Transformer + Mediapipe-based Korean Sign Language Recognition and Translation System**

---

## 📌 Overview

Korea has approximately **430,000 registered deaf and hard-of-hearing individuals** (16.4% of all registered people with disabilities), yet sign language interpreters remain critically scarce. Despite the enactment of the Korean Sign Language Act, the supply of qualified interpreters fails to meet demand — leaving many hearing-impaired people unable to access essential administrative and medical services.

This project addresses that gap by developing an **AI-powered Korean Sign Language Recognition (SLR) and Translation system** using Transformer architecture and Google Mediapipe. Rather than focusing on fingerspelling (which prior research heavily emphasized), this system targets **everyday Korean sign language phrases**, making it genuinely useful for real-world communication.

---

## 🏆 Awards

| Date | Competition | Award | Level |
|------|------------|-------|-------|
| Nov 9, 2024 | 2024 Korea Multimedia Society Autumn Conference | **Best Paper Award** | National (~200 teams) |
| Dec 18, 2024 | 2024 Graduation Project Exhibition | **Outstanding Award** | School-wide (30 teams) |

> Presented at the **2024 Korea Multimedia Society Autumn Academic Conference** held at Jeju National University (Nov 7–9, 2024)

---

## 👩‍💻 Authors

**Eunsu Kim, Seohyun Lee, Helen Hong**  
Dept. of Software Convergence, Seoul Women's University  
`{kimes00, seohyunlee, hlhong}@swu.ac.kr`

---

## 🔧 System Architecture

The system consists of two main components:

```
Korean Sign Language Video
        │
        ▼
┌─────────────────────────────────────┐
│         1. Sign Language            │
│           Recognition (SLR)         │
│                                     │
│  Frame Slicing → Coordinate         │
│  Extraction (Mediapipe) →           │
│  Transformer (Encoder + Decoder)    │
│  → Classifier → English Phrase      │
└─────────────────┬───────────────────┘
                  │ English SLR Output
                  ▼
┌─────────────────────────────────────┐
│         2. Sign Language            │
│          Translation (SLT)          │
│                                     │
│  Fine-tuned mBART →                 │
│  Korean Sentence Output             │
└─────────────────────────────────────┘
```

### Why English as an Intermediate Representation?

Korean's complex syllabic structure (consonant + vowel combinations) makes direct syllable-level prediction difficult. By first translating Korean SL phrases to English, then using the SLR model's English output as input to a Korean translation model, we effectively bypass this complexity while maintaining accuracy.

---

## 📦 Module 1: Sign Language Recognition (SLR)

### Data Preprocessing
<img width="1920" height="1080" alt="슬라이드3" src="https://github.com/user-attachments/assets/410d9a82-4d33-4573-8c39-09b17df3f558" />


- **Frame Slicing**: Frames extracted at 0.025-second intervals
- **Coordinate Extraction** via [Google Mediapipe Holistic API](https://github.com/google-ai-edge/mediapipe):
  - Face: **468 landmarks**
  - Each hand (left/right): **21 landmarks**
  - Full body pose: **33 landmarks**
- **Lip Coordinate Extraction**: 40 lip landmarks stored separately — lip shape is a critical cue in sign language interpretation
- **Data Cleaning**: Sentences exceeding the **90th percentile** of total sentence length distribution are removed to reduce noise

### Model: ASLFR Transformer

Based on the [Kaggle ASLFR Competition model](https://www.kaggle.com/competitions/asl-fingerspelling) by Mark Wijkhuizen, adapted for Korean sign language via transfer learning.

<img width="1920" height="1080" alt="슬라이드4" src="https://github.com/user-attachments/assets/7fb4516b-39a9-466e-9162-9a4c8cd0f11b" />


### Transfer Learning Strategy

1. **Pre-training** on English fingerspelling data (Kaggle ASLFR dataset)
2. **Fine-tuning** on translated Korean sign language data (AI Hub dataset)

### Hyperparameters

| Parameter | Value |
|-----------|-------|
| Batch size | 64 |
| Epochs | 100 |
| Weight decay | 0.05 |
| Max learning rate | 0.001 |
| Encoder embedding dim | 384 |
| Decoder embedding dim | 256 |
| Encoder blocks | 4 |
| Decoder blocks | 2 |
| Attention heads | 4 |
| MLP dropout | 30% |
| Attention dropout | 20% |
| Classifier dropout | 10% |

---

## 📦 Module 2: Sign Language Translation (SLT)

<img width="1920" height="1080" alt="슬라이드5" src="https://github.com/user-attachments/assets/4aac71ae-ae0f-4c87-ab04-76f905ea17f1" />


### Model: mBART Fine-Tuning

Uses Facebook's [mBART-large-50-many-to-many-mmt](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt) — a multilingual Transformer pre-trained with a **denoising autoencoder** objective, making it naturally suited to handling noisy (imperfect SLR) inputs.

### Fine-Tuning Strategy

To bridge the gap between clean English sentences and the noisy output of the SLR model:

1. Take the **English ground-truth** sentences from the Korean sign language dataset
2. **Inject random noise** into them (simulating SLR prediction errors)
3. Fine-tune mBART to translate these noisy English sentences → correct Korean sentences

This enables the model to robustly handle the inevitable character-level errors in SLR output.

---

## 📊 Datasets

### SLR Training Data

| Dataset | Training | Validation | Test | Total |
|---------|----------|------------|------|-------|
| English phrases | 38,304 | 7,236 | 16,415 | 71,134 |
| Korean phrases | 8,155 | 2,437 | 3,495 | 14,087 |

- **Pre-training**: [Kaggle Google ASLFR Dataset](https://www.kaggle.com/competitions/asl-fingerspelling) — 100+ deaf signers filmed across varied backgrounds and lighting with smartphone front cameras
- **Fine-tuning**: [AI Hub Korean Sign Language Dataset](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=103) — 15,000 videos of 3,000 sign words from 5 signers in studio conditions

### SLT Training Data

| Dataset | Total |
|---------|-------|
| Fine-tuning dataset (Eng→Kor) | 2,094 |
| SLR output test set | 3,495 |

---

## 📈 Results

### Sign Language Recognition

| Split | Top-1 Accuracy | Top-5 Accuracy | Mean Levenshtein Distance |
|-------|---------------|---------------|--------------------------|
| Train | 0.9998 | 1.0000 | 4.0804 |
| Validation | 0.9539 | 0.9862 | 5.0616 |
| **Test** | **0.9336** | **0.9764** | **5.2581** |

**Key findings:**
- Test Top-1 accuracy of **93.36%** demonstrates strong recognition performance
- Mean Levenshtein Distance of ~5 indicates the model correctly predicts the beginning of phrases but sometimes over-generates characters at phrase end — the model does not always accurately learn the termination point of a sentence

**Prediction examples:**

| Ground Truth | Predicted | Levenshtein Distance |
|---|---|---|
| holding one's tongue | holding one's tongue | 0 |
| headlight | headlightha | 2 |
| optician's shop | optician's shopesen | 4 |

### Sign Language Translation

| Method | BLEU Score |
|--------|-----------|
| Baseline mBART (no fine-tuning) | 0.0513 |
| **Fine-tuned mBART** | **0.4660** |

Fine-tuning with noisy English data yielded a **~9× improvement** in BLEU score (41.17%p absolute gain).

**Translation examples:**

| English True | Korean True | SLR Output | Baseline SLT | Fine-tuned SLT |
|---|---|---|---|---|
| obituary | 부고 | obituaryneye | 장례식 | **부고** |
| qualification | 적격 | qualificationesce | 숙련 | **적격** |
| pepper | 고추 | pepperjuterny | 옥수수 | **고추** |

---

## 🔬 Evaluation Metrics

- **Top-K Accuracy**: Checks whether the correct class is within the top K predicted classes
- **Levenshtein Distance**: Edit distance between predicted and ground-truth strings — measures string-level similarity
- **BLEU Score**: N-gram overlap between machine-translated and reference translations — standard MT evaluation metric

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11.7 |
| Pose Estimation | Google Mediapipe Holistic API 0.10.14 |
| SLR Model | Transformer (ASLFR-based) |
| SLT Model | mBART-large-50-many-to-many-mmt |
| Translation API | Google Translate API (pygoogletrans) |
| Environment | Jupyter Notebook 7.0.8 |

---

## 🔭 Future Work

- Incorporate **gloss2text** techniques to translate sign gloss sequences into natural Korean sentences
- Extend training to cover **longer, complex sentences** beyond words and short phrases
- Integrate SLR + SLT into a unified real-time **Sign Language Translation (SLT)** pipeline
- Address the **auto-regressive termination problem** in the decoder to eliminate spurious character generation

---

## 📌 Presentation Slide

<img width="1920" height="1080" alt="슬라이드1" src="https://github.com/user-attachments/assets/7b2f0410-0437-4813-a578-178b80f1738b" />
<img width="1920" height="1080" alt="슬라이드2" src="https://github.com/user-attachments/assets/e08d7b9e-8825-4fd1-a748-e46e0b5398d2" />
<img width="1920" height="1080" alt="슬라이드3" src="https://github.com/user-attachments/assets/d54543e7-438e-44b6-b869-4b0e587693da" />
<img width="1920" height="1080" alt="슬라이드4" src="https://github.com/user-attachments/assets/566bff10-b0ec-4539-91d1-75ca40fb7666" />
<img width="1920" height="1080" alt="슬라이드5" src="https://github.com/user-attachments/assets/e838df50-11e5-4a23-915e-42d648f045ba" />
<img width="1920" height="1080" alt="슬라이드6" src="https://github.com/user-attachments/assets/ca34dc92-799f-4359-ab3a-e808ee2e3eee" />
<img width="1920" height="1080" alt="슬라이드8" src="https://github.com/user-attachments/assets/86e7fea3-ebff-4509-8dd5-18d8e22e20dc" />
<img width="1920" height="1080" alt="슬라이드7" src="https://github.com/user-attachments/assets/d599e5c4-8a04-48c8-9d6f-4541aa49e04b" />
<img width="1920" height="1080" alt="슬라이드9" src="https://github.com/user-attachments/assets/f3f4d847-85ce-4e11-bee9-6e53200251b2" />
<img width="1920" height="1080" alt="슬라이드10" src="https://github.com/user-attachments/assets/e2dee546-baaa-4e03-ae8d-3c403074df05" />


<div align="center">
  <sub>Dept. of Software Convergence, Seoul Women's University · 2024</sub>
</div>
