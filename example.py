import requests

url = "https://api.bishopi.io/domain_seo_analysis/?domain=bishopi.io"

headers = {
  'Authorization': 'Api-Key 1234'
}

response = requests.request("GET", url, headers=headers)

print(response.text)


# Response 
# {
#   "status": "success",
#   "code": 200,
#   "data": {
#     "seo_difficulty": 30,
#     "off_page_difficulty": 94,
#     "on_page_difficulty": 85,
#     "indexed_pages": 64,
#     "domain_authority": 39,
#     "page_authority": 42,
#     "popularity_score": 4.2,
#     "domain_rank": "6770708",
#     "citation_flow": "23",
#     "trust_flow": "7",
#     "traffic": "12",
#     "traffic_costs": "63",
#     "organic_keywords": "88",
#     "backlinks": "79",
#     "equity": 1123,
#     "cpc": "0.00",
#     "search_volume": 50,
#     "paid_competition": 0,
#     "referring_domains": "28",
#     "search_trend_data": [
#       {
#         "month": "January",
#         "year": 2023,
#         "value": 50
#       },
#       {
#         "month": "February",
#         "year": 2023,
#         "value": 40
#       },
#       {
#         "month": "March",
#         "year": 2023,
#         "value": 50
#       },
#       {
#         "month": "April",
#         "year": 2023,
#         "value": 50
#       },
#       {
#         "month": "May",
#         "year": 2023,
#         "value": 70
#       },
#       {
#         "month": "June",
#         "year": 2023,
#         "value": 70
#       },
#       {
#         "month": "July",
#         "year": 2023,
#         "value": 70
#       },
#       {
#         "month": "August",
#         "year": 2023,
#         "value": 50
#       },
#       {
#         "month": "September",
#         "year": 2023,
#         "value": 50
#       },
#       {
#         "month": "October",
#         "year": 2023,
#         "value": 50
#       },
#       {
#         "month": "November",
#         "year": 2023,
#         "value": 70
#       },
#       {
#         "month": "December",
#         "year": 2023,
#         "value": 70
#       }
#     ]
#   }
# }