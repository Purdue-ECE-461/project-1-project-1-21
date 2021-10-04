import unittest
from Package import *
import json


class PackageTests(unittest.TestCase):

    def test_valid_package_1(self):
        package_json_string = '{\"id\":3955647,\"node_id\":\"MDEwOlJlcG9zaXRvcnkzOTU1NjQ3\",\"name\":\"lodash\",\"full_name\":\"lodash\/lodash\",\"private\":false,\"owner\":{\"login\":\"lodash\",\"id\":2565403,\"node_id\":\"MDEyOk9yZ2FuaXphdGlvbjI1NjU0MDM=\",\"avatar_url\":\"https:\/\/avatars.githubusercontent.com\/u\/2565403?v=4\",\"gravatar_id\":\"\",\"url\":\"https:\/\/api.github.com\/users\/lodash\",\"html_url\":\"https:\/\/github.com\/lodash\",\"followers_url\":\"https:\/\/api.github.com\/users\/lodash\/followers\",\"following_url\":\"https:\/\/api.github.com\/users\/lodash\/following{\/other_user}\",\"gists_url\":\"https:\/\/api.github.com\/users\/lodash\/gists{\/gist_id}\",\"starred_url\":\"https:\/\/api.github.com\/users\/lodash\/starred{\/owner}{\/repo}\",\"subscriptions_url\":\"https:\/\/api.github.com\/users\/lodash\/subscriptions\",\"organizations_url\":\"https:\/\/api.github.com\/users\/lodash\/orgs\",\"repos_url\":\"https:\/\/api.github.com\/users\/lodash\/repos\",\"events_url\":\"https:\/\/api.github.com\/users\/lodash\/events{\/privacy}\",\"received_events_url\":\"https:\/\/api.github.com\/users\/lodash\/received_events\",\"type\":\"Organization\",\"site_admin\":false},\"html_url\":\"https:\/\/github.com\/lodash\/lodash\",\"description\":\"A modern JavaScript utility library delivering modularity, performance, & extras.\",\"fork\":false,\"url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\",\"forks_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/forks\",\"keys_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/keys{\/key_id}\",\"collaborators_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/collaborators{\/collaborator}\",\"teams_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/teams\",\"hooks_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/hooks\",\"issue_events_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/issues\/events{\/number}\",\"events_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/events\",\"assignees_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/assignees{\/user}\",\"branches_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/branches{\/branch}\",\"tags_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/tags\",\"blobs_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/git\/blobs{\/sha}\",\"git_tags_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/git\/tags{\/sha}\",\"git_refs_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/git\/refs{\/sha}\",\"trees_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/git\/trees{\/sha}\",\"statuses_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/statuses\/{sha}\",\"languages_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/languages\",\"stargazers_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/stargazers\",\"contributors_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/contributors\",\"subscribers_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/subscribers\",\"subscription_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/subscription\",\"commits_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/commits{\/sha}\",\"git_commits_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/git\/commits{\/sha}\",\"comments_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/comments{\/number}\",\"issue_comment_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/issues\/comments{\/number}\",\"contents_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/contents\/{+path}\",\"compare_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/compare\/{base}...{head}\",\"merges_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/merges\",\"archive_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/{archive_format}{\/ref}\",\"downloads_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/downloads\",\"issues_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/issues{\/number}\",\"pulls_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/pulls{\/number}\",\"milestones_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/milestones{\/number}\",\"notifications_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/notifications{?since,all,participating}\",\"labels_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/labels{\/name}\",\"releases_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/releases{\/id}\",\"deployments_url\":\"https:\/\/api.github.com\/repos\/lodash\/lodash\/deployments\",\"created_at\":\"2012-04-07T04:11:46Z\",\"updated_at\":\"2021-10-04T02:04:52Z\",\"pushed_at\":\"2021-10-03T23:48:12Z\",\"git_url\":\"git:\/\/github.com\/lodash\/lodash.git\",\"ssh_url\":\"git@github.com:lodash\/lodash.git\",\"clone_url\":\"https:\/\/github.com\/lodash\/lodash.git\",\"svn_url\":\"https:\/\/github.com\/lodash\/lodash\",\"homepage\":\"https:\/\/lodash.com\/\",\"size\":47581,\"stargazers_count\":50917,\"watchers_count\":50917,\"language\":\"JavaScript\",\"has_issues\":true,\"has_projects\":false,\"has_downloads\":true,\"has_wiki\":true,\"has_pages\":false,\"forks_count\":6012,\"mirror_url\":null,\"archived\":false,\"disabled\":false,\"open_issues_count\":295,\"license\":{\"key\":\"other\",\"name\":\"Other\",\"spdx_id\":\"NOASSERTION\",\"url\":null,\"node_id\":\"MDc6TGljZW5zZTA=\"},\"allow_forking\":true,\"visibility\":\"public\",\"forks\":6012,\"open_issues\":295,\"watchers\":50917,\"default_branch\":\"master\",\"temp_clone_token\":null,\"organization\":{\"login\":\"lodash\",\"id\":2565403,\"node_id\":\"MDEyOk9yZ2FuaXphdGlvbjI1NjU0MDM=\",\"avatar_url\":\"https:\/\/avatars.githubusercontent.com\/u\/2565403?v=4\",\"gravatar_id\":\"\",\"url\":\"https:\/\/api.github.com\/users\/lodash\",\"html_url\":\"https:\/\/github.com\/lodash\",\"followers_url\":\"https:\/\/api.github.com\/users\/lodash\/followers\",\"following_url\":\"https:\/\/api.github.com\/users\/lodash\/following{\/other_user}\",\"gists_url\":\"https:\/\/api.github.com\/users\/lodash\/gists{\/gist_id}\",\"starred_url\":\"https:\/\/api.github.com\/users\/lodash\/starred{\/owner}{\/repo}\",\"subscriptions_url\":\"https:\/\/api.github.com\/users\/lodash\/subscriptions\",\"organizations_url\":\"https:\/\/api.github.com\/users\/lodash\/orgs\",\"repos_url\":\"https:\/\/api.github.com\/users\/lodash\/repos\",\"events_url\":\"https:\/\/api.github.com\/users\/lodash\/events{\/privacy}\",\"received_events_url\":\"https:\/\/api.github.com\/users\/lodash\/received_events\",\"type\":\"Organization\",\"site_admin\":false},\"network_count\":6012,\"subscribers_count\":882}'
        package_dict = json.loads(package_json_string)
        package = Package(**package_dict)
        self.assertIsNotNone(package)

    def test_valid_package_2(self):
        package_json_string = '{\"id\":408862724,\"node_id\":\"R_kgDOGF7ABA\",\"name\":\"GNU-LGPL-Test\",\"full_name\":\"Project-1-21\/GNU-LGPL-Test\",\"private\":false,\"owner\":{\"login\":\"Project-1-21\",\"id\":90574379,\"node_id\":\"MDEyOk9yZ2FuaXphdGlvbjkwNTc0Mzc5\",\"avatar_url\":\"https:\/\/avatars.githubusercontent.com\/u\/90574379?v=4\",\"gravatar_id\":\"\",\"url\":\"https:\/\/api.github.com\/users\/Project-1-21\",\"html_url\":\"https:\/\/github.com\/Project-1-21\",\"followers_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/followers\",\"following_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/following{\/other_user}\",\"gists_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/gists{\/gist_id}\",\"starred_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/starred{\/owner}{\/repo}\",\"subscriptions_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/subscriptions\",\"organizations_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/orgs\",\"repos_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/repos\",\"events_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/events{\/privacy}\",\"received_events_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/received_events\",\"type\":\"Organization\",\"site_admin\":false},\"html_url\":\"https:\/\/github.com\/Project-1-21\/GNU-LGPL-Test\",\"description\":\"This is a dummy repo with GNU LGPL license.\",\"fork\":false,\"url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\",\"forks_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/forks\",\"keys_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/keys{\/key_id}\",\"collaborators_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/collaborators{\/collaborator}\",\"teams_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/teams\",\"hooks_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/hooks\",\"issue_events_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/issues\/events{\/number}\",\"events_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/events\",\"assignees_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/assignees{\/user}\",\"branches_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/branches{\/branch}\",\"tags_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/tags\",\"blobs_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/git\/blobs{\/sha}\",\"git_tags_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/git\/tags{\/sha}\",\"git_refs_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/git\/refs{\/sha}\",\"trees_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/git\/trees{\/sha}\",\"statuses_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/statuses\/{sha}\",\"languages_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/languages\",\"stargazers_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/stargazers\",\"contributors_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/contributors\",\"subscribers_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/subscribers\",\"subscription_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/subscription\",\"commits_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/commits{\/sha}\",\"git_commits_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/git\/commits{\/sha}\",\"comments_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/comments{\/number}\",\"issue_comment_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/issues\/comments{\/number}\",\"contents_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/contents\/{+path}\",\"compare_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/compare\/{base}...{head}\",\"merges_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/merges\",\"archive_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/{archive_format}{\/ref}\",\"downloads_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/downloads\",\"issues_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/issues{\/number}\",\"pulls_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/pulls{\/number}\",\"milestones_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/milestones{\/number}\",\"notifications_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/notifications{?since,all,participating}\",\"labels_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/labels{\/name}\",\"releases_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/releases{\/id}\",\"deployments_url\":\"https:\/\/api.github.com\/repos\/Project-1-21\/GNU-LGPL-Test\/deployments\",\"created_at\":\"2021-09-21T14:55:47Z\",\"updated_at\":\"2021-09-21T14:55:51Z\",\"pushed_at\":\"2021-09-21T14:55:48Z\",\"git_url\":\"git:\/\/github.com\/Project-1-21\/GNU-LGPL-Test.git\",\"ssh_url\":\"git@github.com:Project-1-21\/GNU-LGPL-Test.git\",\"clone_url\":\"https:\/\/github.com\/Project-1-21\/GNU-LGPL-Test.git\",\"svn_url\":\"https:\/\/github.com\/Project-1-21\/GNU-LGPL-Test\",\"homepage\":null,\"size\":11,\"stargazers_count\":0,\"watchers_count\":0,\"language\":null,\"has_issues\":true,\"has_projects\":true,\"has_downloads\":true,\"has_wiki\":true,\"has_pages\":false,\"forks_count\":0,\"mirror_url\":null,\"archived\":false,\"disabled\":false,\"open_issues_count\":0,\"license\":{\"key\":\"lgpl-2.1\",\"name\":\"GNU Lesser General Public License v2.1\",\"spdx_id\":\"LGPL-2.1\",\"url\":\"https:\/\/api.github.com\/licenses\/lgpl-2.1\",\"node_id\":\"MDc6TGljZW5zZTEx\"},\"allow_forking\":true,\"visibility\":\"public\",\"forks\":0,\"open_issues\":0,\"watchers\":0,\"default_branch\":\"main\",\"temp_clone_token\":null,\"organization\":{\"login\":\"Project-1-21\",\"id\":90574379,\"node_id\":\"MDEyOk9yZ2FuaXphdGlvbjkwNTc0Mzc5\",\"avatar_url\":\"https:\/\/avatars.githubusercontent.com\/u\/90574379?v=4\",\"gravatar_id\":\"\",\"url\":\"https:\/\/api.github.com\/users\/Project-1-21\",\"html_url\":\"https:\/\/github.com\/Project-1-21\",\"followers_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/followers\",\"following_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/following{\/other_user}\",\"gists_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/gists{\/gist_id}\",\"starred_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/starred{\/owner}{\/repo}\",\"subscriptions_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/subscriptions\",\"organizations_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/orgs\",\"repos_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/repos\",\"events_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/events{\/privacy}\",\"received_events_url\":\"https:\/\/api.github.com\/users\/Project-1-21\/received_events\",\"type\":\"Organization\",\"site_admin\":false},\"network_count\":0,\"subscribers_count\":0}'
        package_dict = json.loads(package_json_string)
        package = Package(**package_dict)
        self.assertIsNotNone(package)

    def test_invalid_package_1(self):
        package_json_string = '{}'
        package_dict = json.loads(package_json_string)

        with self.assertRaises(TypeError):
            Package(**package_dict)

    def test_invalid_package_2(self):
        package_json_string = '{\"id\":408862724}'
        package_dict = json.loads(package_json_string)

        with self.assertRaises(TypeError):
            Package(**package_dict)


if __name__ == '__main__':
    unittest.main()