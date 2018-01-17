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
def np_triggered_cache_reset(sender, instance, **kwargs):
    cache.delete(cache_mapper.get_nutritional_info(instance.pk))

@receiver([pre_save, post_save, post_delete], sender=Meal)
def meal_triggered_cache_reset(sender, instance, **kwargs):
    cache.delete(cache_mapper.get_nutritional_info(instance.pk))

@receiver([post_save, post_delete], sender=MealItem)
def meal_item_triggered_cache_reset(sender, instance, **kwargs):
    cache.delete(cache_mapper.get_nutritional_info(instance.pk))
