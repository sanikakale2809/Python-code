tech={'os':'windows','language':'java','database':'oracle'}
print(tech)


tech['cloud']='aws'
print(tech)


tech['database']='mongodb'
print(tech)


tech.update({'framework':'springboot','aiplatform':'deepseek'})
print(tech)


tech['experience']=5
print(tech)

tech['experience']+=2
print(tech)


# Remove
del tech['os']
print(tech)


f=tech.pop('framework')
print(f)
print(tech)
tech.clear()
print(tech)
tech["language"]="python"
tech["framework"]="django"
tech["database"]="mysql"
print(tech)