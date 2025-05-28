# utils.py
def get_counseling_tips(emotion):
    responses = {
        "Sad": [
            "It's okay to cry. That means your heart is working. When you're ready, take a few deep breaths and try to talk to someone who cares about you.",
            "You are not alone. Everyone feels sad sometimes. Try drawing or writing about what made you feel this way — it helps."
        ],
        "Angry": [
            "Feeling angry is normal. But it's important to let it out safely. Take a deep breath, count to 10, and squeeze something soft like a pillow.",
            "Try writing your feelings down or drawing them out. Let your anger walk away without hurting you or others."
        ],
        "Scared": [
            "You are safe now. Fear is your brain's way of trying to protect you. It's okay to feel afraid.",
            "Try closing your eyes and imagining your favorite safe place. Hold something soft, breathe in and out slowly — you're not alone."
        ],
        "Happy": [
            "You’re feeling happy — that’s amazing! Try to remember what made you feel this way and do more of it.",
            "You can share your happiness with someone else by giving them a smile, a drawing, or a kind word!"
        ],
        "Numb": [
            "It’s okay if you don’t know what you feel right now. Some days are just confusing, and that's normal.",
            "Try to take a small walk, stretch your arms, or color something. Let your heart have time to speak up when it's ready."
        ]
    }

    return responses.get(emotion, ["You're doing great. Keep going. You're stronger than you think."])
