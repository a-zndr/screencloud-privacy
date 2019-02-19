import json
import requests

time = input_data['miliseconds']

# Array contain list of screens to disable. Use the get {{url}}/teams/{{teamID}}/screens to return screen list

array = ["screen1", "screen2", "screen3", "screenn"]

url = "https://signage-api.screen.cloud/api/v1/teams/<team ID>/screens/"

for x in array:
    payload = "{\n  \"content_id\": \"<conent id>\",\n  \"mime_type\": \"image/jpeg\",\n  \"duration\": %s\n}" % time
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic <key>",
        'cache-control': "no-cache",
        }

    response = requests.request("PUT", (url+x+"/takeover"), data=payload, headers=headers)

    print(response.text)
    print(payload)

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = 'https://hooks.slack.com/services/<webhook URL back to slack>'
slack_data = {
    "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#EC1075",
            "title": "Privacy Enabled",
            "text": ":red-flag: Sensitive screens around the office have been made :dark_sunglasses: for {} minutes".format(input_data['minutes']),



        }
    ]
}
print(slack_data)
response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
