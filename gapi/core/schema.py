import graphene
from graphene_django import DjangoObjectType
from .models import Producto, Categoria

class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto

class CategoriaType(DjangoObjectType):
    class Meta:
        model = Categoria

class Query(graphene.ObjectType):
    productos = graphene.List(ProductoType)

    categorias = graphene.List(CategoriaType)

    def resolve_productos(self, info, **kwargs):
        return Producto.objects.all()

    def resolve_categorias(self, info, **kwargs):
        return Categoria.objects.all()


class CreateCategoria(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        name = graphene.String(required=True)

    # Class attributes define the response of the mutation
    categoria = graphene.Field(CategoriaType)

    @classmethod
    def mutate(cls, root, info, name):
        categoria = Categoria()
        categoria.name = name
        categoria.save()
        
        return CreateCategoria(categoria=categoria)


class CategoriaMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    categoria = graphene.Field(CategoriaType)

    @classmethod
    def mutate(cls, root, info, name, id):
        categoria = Categoria.objects.get(id=id)
        categoria.name = name
        categoria.save()
        return CategoriaMutation(categoria=categoria)

class CategoriaDelete(graphene.Mutation):

    class Arguments:
        id = graphene.ID()


    categoria = graphene.Field(CategoriaType)

    @classmethod
    def mutate(cls, root, info, id):
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        return

class Mutation(graphene.ObjectType):
    create_categoria = CreateCategoria.Field()
    update_categoria = CategoriaMutation.Field()
    delete_categoria = CategoriaDelete.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)