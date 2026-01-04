def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
profile(name="Satyam", skill="Python", experience=2)
