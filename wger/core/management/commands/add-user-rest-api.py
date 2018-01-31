# -*- coding: utf-8 *-*

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from optparse import make_option

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from wger.gym.helpers import get_user_last_activity


class Command(BaseCommand):
    '''
    Enables a user to create other users via the API
    '''

    option_list = BaseCommand.option_list + (
        make_option(
            '--username',
            action='store_true',
            dest='username',
            default=False,
            help='username of user to receive permissions'
        ),
        make_option(
            '--email',
            action='store_true',
            dest='email',
            default=False,
            help='email of user to receive permissions'
        )
    )

    help = """
        Grant a user permission to create other users via the API.
        This command takes the username or email of the user to gain permission.

        Example:
        python manage.py add-user-rest-api <username> --username

        python manage.py add-user-rest-api <email> --email
    """

    def handle(self, *args, **options):
        self.stdout.write('** Updating User permissions...')
        if (options.get('email') ^ options.get('username')) is False:  # only one flag  # noqa
            self.stdout.write('Please select one of --email or --username')
            return
        if options.get('email'):
            user_email = str(args[0])
            self.stdout.write('Email: {}'.format(user_email))
            if user_email:
                try:
                    user = User.objects.get(email=user_email)
                    user_profile = user.userprofile
                    user_profile.can_create_users_via_api = True
                    user_profile.save()
                    self.stdout.write(
                        'User permissions for {} successfully updated'.format(
                            user_email
                        )
                    )
                except User.DoesNotExist:
                    self.stdout.write('Please supply valid email')
                    return
        if options.get('username'):
            user_username = str(args[0])
            if user_username:
                try:
                    user = User.objects.get(username=user_username)
                    user_profile = user.userprofile
                    user_profile.can_create_users_via_api = True
                    user_profile.save()
                    self.stdout.write(
                        'User permissions for {} successfully updated'.format(
                            user_username
                        )
                    )
                    return
                except User.DoesNotExist:
                    self.stdout.write('Please supply a valid username')
                    return
