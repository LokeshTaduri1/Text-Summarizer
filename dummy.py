import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": 'Bearer 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'}

minL=int(input())
maxL=int(input())
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
data='''The title "Father of the Nation" of Cambodia is commonly attributed to King Norodom Sihanouk. He played a pivotal role in the country's independence from French colonial rule in 1953 and significantly influenced Cambodia's modern history.
King Norodom Sihanouk was born on October 31, 1922, and served as the King of Cambodia from 1941 to 1955 and again from 1993 to 2004. He was a prominent figure in the country's political scene, serving in various capacities, including as head of state, prime minister, and president. His efforts in leading the movement for Cambodia's independence and his enduring influence on the nation's political and cultural landscape earned him the title of the "Father of the Nation."
'''
output = query({
	"inputs": data,
	"parameters":{"min_length":minL, "max_length":maxL},
})
print(output)