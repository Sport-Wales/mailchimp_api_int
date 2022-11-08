import mailchimp_marketing
from mailchimp_marketing.api_client import ApiClientError
import json

try:
  # config api
  mc = mailchimp_marketing.Client()
  mc.set_config({
    "api_key": API_KEY,
    "server": "us4"
  })

  def searchMailchimpCampaign():
    query = input("Please enter your search term: ")
    # retreive data as a dict
    returnedSearchQuery = mc.searchCampaigns.search(query)
    print(returnedSearchQuery)
  
  searchMailchimpCampaign()

  # dump data to json file
  # response_json = json.dumps(response)
  # file = open("lottery2.json", "w")
  # file.write(response_json)
  # file.close

except ApiClientError as error:
  print("Error: {}".format(error.text))
