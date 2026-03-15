from helper import get_completion

prompt = """
Summarize the following sentence in 10 words:

In IPL 2020, Chennai Super kings didn't qualify for the playoffs for the first time in the history of IPL. They Finished at the bottom of the points table but in the very next year,they secured the title by defeating Kolkata Knight Riders in the final. In IPL 2022, they again qualified for the playoffs but lost to Gujarat Titans in the final. In IPL 2023, they again qualified for the playoffs but lost to Gujarat Titans in the final.
"""

response = get_completion(prompt)
print(response)