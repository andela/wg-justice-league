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


class Command(BaseCommand):

    help = 'Lists all users created via the API'

    def handle(self, *args, **options):
        self.stdout.write(
            '** Listing users created via API as id:username:email...'
        )
        users_via_api = []
        users = User.objects.all()
        for user in users:
            if user.userprofile.created_via_api is True:
                users_via_api.append(user)
        if len(users_via_api) > 0:
            for user in users_via_api:
                self.stdout.write(
                    '{}: {}: {}'.format(user.id, user.username, user.email)
                )
