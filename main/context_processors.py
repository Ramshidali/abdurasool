import datetime

from web.models import Description




def main_context(request):
      is_description = Description.objects.filter(is_deleted=False).count()
       
      return {
         "confirm_delete_message": "The associated datas will be removed",
         "is_description" : is_description,
    }
