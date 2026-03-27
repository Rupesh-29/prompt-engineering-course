from helper import get_completion

prompt = """
Summarize the following sentence into 5 Bullet points:
The U.S.A has many different types of climates, including tropical, dry, temperate, continental, and polar. The climate in the U.S.A can vary greatly depending on the region, with some areas experiencing hot summers and cold winters, while others have mild temperatures year-round. The country also experiences a wide range of weather phenomena, such as hurricanes, tornadoes, and blizzards. Overall, the diverse climates in the U.S.A contribute to its rich natural beauty and variety of ecosystems.

"""

response = get_completion(prompt)
print(response)