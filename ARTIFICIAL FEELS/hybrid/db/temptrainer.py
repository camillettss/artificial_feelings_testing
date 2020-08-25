import json
total=json.loads(open('dataset.json').read())
x=total['intents']['reply_usingfeelsIntent']['samples']
newx=[]
for i in x:
    newx.append(i.replace('?', ''))
    #print(i)
for item in x:
    newx.append(item)

for line in newx:
    print(line)

total['intents']['reply_usingfeelsIntent']['samples']=newx
print(total)

f=open('dataset.json', 'w+')
f.write(json.dumps(total))
f.close()
