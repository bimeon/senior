from wordcloud import WordCloud
import matplotlib.pyplot as plt

TEXT = """
Python python java c java python programming language
Python python java c
"""

word_cloud = WordCloud().generate(TEXT)

plt.figure(figsize=(5, 5))
plt.imshow(word_cloud)
plt.axis('off')
plt.show()