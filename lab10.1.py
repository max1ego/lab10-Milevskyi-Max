import re

file_path = "story.txt"

file = open(file_path, 'r', encoding='utf-8')
text = file.read()
file.close()
    
words = re.findall(r'\b\w+\b', text.lower())  
word_count = len(words)
    
sentences = re.split(r'[.!?]', text) 
sentence_count = len([s for s in sentences if s.strip()])
    
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
    
most_common_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:4]
  
file = open('word_count.txt', 'w', encoding='utf-8')
file.write(f"Кількість слів: {word_count}\n")
file.close()
    
file = open('sentence_count.txt', 'w', encoding='utf-8')
file.write(f"Кількість речень: {sentence_count}\n")
file.close()
    
file = open('most_common_words.txt', 'w', encoding='utf-8')
file.write("4 найчастіших слова:\n")
for word, freq in most_common_words:
    file.write(f"{word}: {freq}\n")
file.close()
