import tensorflow as tf
import numpy as np
import json
y=[]

a=json.loads(open('./a.txt','r').read())
b=json.loads(open('./b.txt','r').read())
c=json.loads(open('./c.txt','r').read())
d=json.loads(open('./d.txt','r').read())
e=json.loads(open('./e.txt','r').read())
f=json.loads(open('./f.txt','r').read())

data=a+b+c+d+e+f

for i in range(len(a)):
    y.append(tf.one_hot(0,6))
for i in range(len(b)):
    y.append(tf.one_hot(1,6))
for i in range(len(c)):
    y.append(tf.one_hot(2,6))
for i in range(len(d)):
    y.append(tf.one_hot(3,6))
for i in range(len(e)):
    y.append(tf.one_hot(4,6))
for i in range(len(f)):
    y.append(tf.one_hot(5,6))


data=np.asarray(data)
y=np.asarray(y)

print(y)


data=tf.convert_to_tensor(data)
y=tf.convert_to_tensor(y)





model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(21, 3)),
    tf.keras.layers.Dense(20, activation='relu'),
    #tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(3, activation='softmax'),
    tf.keras.layers.Reshape([3])
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])





model.fit(data,y , epochs=5)





