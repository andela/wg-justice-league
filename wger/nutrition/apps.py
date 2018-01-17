# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

from django.apps import AppConfig


class NutritionPlanConfig(AppConfig):
    name = 'wger.nutrition'
    verbose_name = "NutritionPlan"

    def ready(self):
        import wger.nutrition.signals
