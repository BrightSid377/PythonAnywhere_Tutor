
# this is a test script to view a list of Models in our program
# but it doesn't seem to work mjl 6/27

from django.apps import apps
model_list = apps.get_models()

for model in model_list:
    print(model.__name__)