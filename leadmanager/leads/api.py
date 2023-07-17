from leads.models import Lead
from leads.serailzer import LeadSerializer
from rest_framework import permission,viewsets

class LeadViewSet(viewsets.ModelViewSet):
    query_set=Lead.objects.all()
    '''
     the permission_classes attribute is set to 
     [permission.AllowAny], which means that any 
     user, whether authenticated or not, will be 
     allowed to access the API endpoints 
    '''
    permission_classes=[
        permission.AllowAny
    ]
    seializer_class=LeadSerializer

