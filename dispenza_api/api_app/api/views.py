from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import list_route, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import  Response
from munch import *


from api_app.api.models import Prodotto_Dispensa, Spesa, Prodotto_Spesa
from api_app.api.serializers import UserSerializer, GroupSerializer, ProdottoDispensaSerializer, SpesaSerializer, \
    ProdottoSpesaSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProdottiDispensaViewSet(viewsets.ModelViewSet):
    queryset = Prodotto_Dispensa.objects.all()
    serializer_class = ProdottoDispensaSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )

class SpesaViewSet(viewsets.ModelViewSet):
    queryset = Spesa.objects.all()
    serializer_class = SpesaSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )

    #@action(methods=['post'], detail=True)
    #@list_route(methods=['post'])
    @action(methods=['post'],detail=False)
    def aggiungi_spesa(self, request):
        if 'titolo' in request.data  and 'prodotto' in request.data and 'prezzo_tot' in request.data:# and request.data.prezzo_tot> 0: #
            try:
                print("0")
                products = Prodotto_Spesa.objects.filter(pk__in=request.data['prodotto']).all()
                print(products)
                products = list(products)
                print(products)
                print(products[0])
                print("n")
                if products == None:
                    raise Exception()
                    #return Prodotto_Spesa(product)
            except:
                response = {"message" : "The product that you want to buy doesn't exist in our database yet!"}
                return Response(response,status=status.HTTP_400_BAD_REQUEST)

            title = request.data['titolo']
            price = request.data['prezzo_tot']

            try:
                print("1")
                #xs = Prodotto_Spesa.object.get(pk = 1)

                le_mie_spese = Spesa.objects.filter(prodotto__in=products, prezzo_tot=price).first()    #prodotto__in=products
                print(le_mie_spese, "post-inizializzazione")
                print(le_mie_spese.prodotto, "post-inizializzazione")
#
                le_mie_spese.titolo = title
                le_mie_spese.save()
                print("2")
                serializer = SpesaSerializer(le_mie_spese)
                print("Spesa Update serializzata")
                serializer2 = ProdottoSpesaSerializer(products, many=True)
                print("SpesaUpdate prodotto serializzato")
                #response = {"message": "Spesa updated"}
                response = {"message" : "Spesa updated", "result" : serializer.data, "Content of your grocery shopping:"
                : serializer2.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                le_mie_spese = Spesa.objects.create(titolo=title, prezzo_tot=price) #
                print(le_mie_spese , "except")
                print(le_mie_spese.titolo, "except")
                print(le_mie_spese.prezzo_tot, "except")
                for i in range(len(products)):
                    le_mie_spese.prodotto.add(products[i])
                print(le_mie_spese.prodotto, "except")
                serializer = SpesaSerializer(le_mie_spese)
                print("SpesaCreate Serializzata")
                serializer2 = ProdottoSpesaSerializer(products, many= True)
                print("SpesaCreate Prodotti Serializzati")
                response = {"message": "Spesa created", "result": serializer.data, "Content of your grocery shopping:" :
                    serializer2.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            if'titolo' in request.data and 'prodotto' in request.data:
                try:
                    products = Prodotto_Spesa.objects.filter(pk__in=request.data['prodotto']).all()
                    products = list(products)
                    if products == None:
                        raise Exception()
                except:
                    response = {"message": "The product that you want to buy doesn't exist in our database yet!"}
                    return Response(response, status=status.HTTP_404_NOT_FOUND)
                title = request.data['titolo']
                price = 0
                for i in range(len(products)):
                    price += products[i].calc_prezzo()
                try:
                    le_mie_spese = Spesa.objects.filter(prodotto__in=products, prezzo_tot=price).first()  #
                    le_mie_spese.titolo = title
                    le_mie_spese.save()
                    serializer = SpesaSerializer(le_mie_spese)
                    serializer2 = ProdottoSpesaSerializer(products, many=True)
                    response = {"message": "Spesa updated", "result": serializer.data,
                                "Content of your grocery shopping:"
                                : serializer2.data}
                    return Response(response, status=status.HTTP_200_OK)
                except:
                    le_mie_spese = Spesa.objects.create(titolo=title, prezzo_tot=price)
                    for i in range(len(products)):
                        le_mie_spese.prodotto.add(products[i])
                    serializer = SpesaSerializer(le_mie_spese)
                    serializer2 = ProdottoSpesaSerializer(products, many=True)
                    response = {"message": "Spesa created", "result": serializer.data, "Content of your grocery "
                                        "shopping:":serializer2.data}
                    return Response(response, status=status.HTTP_200_OK)
            else:
                response = {"message" : "You need at least to pass a title,a product and the total amount of the money "
                                        "that you have spent"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many=False, context={'request': self.request})
        return Response({'token': token.key, 'user': serializer.data})