import strawberry
from api.graphql.mutation import Mutation
from api.graphql.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
