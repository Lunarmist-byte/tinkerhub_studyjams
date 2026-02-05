'''
To use venv
set OPENROUTER_API_KEY=your_key_here   # Windows
# or
export OPENROUTER_API_KEY=your_key_here # Linux/Mac

'''

import numpy as np
from sklearn.linear_model import LogisticRegression
import requests
import os
import json

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_email(prompt):
    if not OPENROUTER_API_KEY:
        raise ValueError("API Key missing")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Recruiter Bot"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def recruiter():
    X = np.array([[1,3], [2,4], [1,5], [3,7], [5,8], [10,9], [4,9]])
    y = np.array([0, 0, 0, 1, 1, 1, 1])
    model = LogisticRegression()
    model.fit(X, y)
    exp = float(input("Years Exp: "))
    score = float(input("Test Score (0-10): "))
    hired = model.predict([[exp, score]])[0] == 1
    print(f"Decision: {'HIRE' if hired else 'REJECT'}")
    try:
        prompt = (
            f"Write a short {'job offer' if hired else 'rejection'} "
            f"email for a software developer with {exp} years of experience."
        )
        email = generate_email(prompt)
        print("\nGenerated Email:\n")
        print(email)

    except Exception as e:
        print("Error generating email:", e)


if __name__ == "__main__":
    recruiter()
