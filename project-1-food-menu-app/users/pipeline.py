from social_core.backends.github import GithubOAuth2

def save_github_profile(backend, user, response, *args, **kwargs):

    # The snippet below does not work.  The relevant fields in the response dict
    # are all None.

    # if backend.name == 'github':
    #     email = response.get('email')
    #     name = response.get('name')
    #
    #     # Populate name and email fields
    #     if name:
    #         full_name = name.split(' ')
    #         user.first_name = full_name[0]
    #         if len(full_name) > 1:
    #             user.last_name = ' '.join(full_name[1:])
    #     if email:
    #         user.email = email
    #
    #     user.save()
    pass