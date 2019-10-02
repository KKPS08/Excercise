# The script test.py fetches the newly published gist by querying the Github API and returns with the last updated
# gist for the publicly available github gists.
import requests
import json


class GistList:
    repo_url = 'https://api.github.com/gists'
    github_session = requests.session()

    def get_gist_list(self):
        result = json.loads(self.github_session.get(self.repo_url).text)
        print("Total Number of gist available are ==> ", len(result))
        for gist in result:
            if str(gist['public']) == 'True':
                gist_id = gist['url'].split("/")
                print("The gist", gist_id[4], "is Public and updated at ", gist['updated_at'])
            else:
                print("The gist is NOT public")


list_details = GistList()
list_details.get_gist_list()
