from django.core.cache import cache
from django.db.models.signals import (
    pre_save,
    post_save,
    post_delete
)

from django.dispatch import receiver

from wger.nutrition.models import (
    NutritionPlan,
    Meal,
    MealItem
)

from wger.utils.cache import cache_mapper


@receiver([post_save, post_delete], sender=NutritionPlan)
@receiver([pre_save, post_save, post_delete], sender=Meal)
@receiver([post_save, post_delete], sender=MealItem)
def reset_nutrition_info_cache(sender, instance, **kwargs):
    cache.delete(cache_mapper.get_nutritional_info(instance.pk))
