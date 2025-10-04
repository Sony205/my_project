words = ["python", "Java", "c++", "Rust", "go"]

new_words = [w.upper() for w in words if len(w) > 3]
print('Слова с верхним регистром и длиннее 3', new_words)