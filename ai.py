import yake
from duckduckgo_search import DDGS

user_input = input("Mời đặt câu hỏi: ")
kw_extractor = yake.KeywordExtractor(top=1, stopwords=None)
keywords = kw_extractor.extract_keywords(user_input)
for kw, v in keywords:
  print("Key",kw, ": Score", v)
#Ducky search keywords
  abc = user_input + "'" + "'" + " && " +"'" + kw + "'"
with DDGS() as ddgs:
    results = [r for r in ddgs.text(abc, max_results=1)]
    print(results[0]['body'])
