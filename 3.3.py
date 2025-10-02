words = ["python", "Java", "c++", "Rust", "go"]

new_words = [w.upper() for w in words if len(w) > 3]
print(new_words)