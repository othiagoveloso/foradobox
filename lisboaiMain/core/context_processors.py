from lisboaiMain.core.models import Categories,Social


def categories(request):

    objCategories = Categories.objects.all()
    objSocial = Social.objects.all()


    return {'category':objCategories,'social':objSocial} 


