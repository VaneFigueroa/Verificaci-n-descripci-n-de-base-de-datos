#!/usr/bin/env python
# coding: utf-8

# ## Verificación y descripción del contenido de la base de datos
# Nos familiarizamos con la base de datos: Verificamos tablas y campos. Resulta útil contar con diagrama relación-entidad (ER) y esquema relacional de la base de datos.
# 

# Al trabajar con la interface de Jupyter que se ejecuta con lenguaje python, debemos cargar la librería SQL para poder ejecutar las consultas:
# 

# In[13]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[14]:


get_ipython().run_line_magic('sql', 'mysql://studentuser:studentpw@localhost/dognitiondb')


# Conectados a la base de datos, el siguiente paso cuando se comienza a trabajar con una nueva base de datos: es familiarícese con los datos. Lo que se aconseja es ejecutar las consultas con cuidado para evitar colgar o esperar minutos para obtener los datos incluso si se cuenta con un diagrama relación-entidad (ER) y un esquema relacional. 
# Verificamos las tablas de la base de datos, limitando las salidas.
# En el esquema y diagrama nos anticipaba 6 tablas, acá podemos corroborarlo y además verificar el nombre asignado a cada una. 

# In[15]:


get_ipython().run_line_magic('sql', 'SHOW tables')


# Ahora, procedemos a verificar por tabla, la cantidad campos, tipo de datos, si admite o no valores nulos en las columnas, si son valores únicos o no y si hay algún campo declarado como clave primaria.
# *Los tipos de datos* que encontramos en esta base son para datos enteros int, tinyintde menor espacio que int, para datos de caracteres varch y text, para fechas datetime con el formato YYYY-MM-DD hh: mm: ss.
# Podemos observar que no hay claves primarias declaradas, por lo que los campos de enlace pueden contener valores NULL o filas duplicadas. Se pueden usar para vincular tablas (aquellos campor ccon valor "MUL" en la columna "Clave" de la salida DESCRIBE).
# 

# In[16]:


get_ipython().run_line_magic('sql', 'SHOW columns FROM dognitiondb.users')


# In[17]:


get_ipython().run_line_magic('sql', 'DESCRIBE site_activities')


# In[ ]:


get_ipython().run_line_magic('sql', 'DESCRIBE reviews;')


# In[ ]:


get_ipython().run_line_magic('sql', 'DESCRIBE exam_answers;')


# In[ ]:


get_ipython().run_line_magic('sql', 'DESCRIBE dogs;')


# In[ ]:


get_ipython().run_line_magic('sql', 'DESCRIBE complete_tests;')


# Si tiene varias bases de datos cargadas:
# ```mySQL
# SHOW columns FROM (enter table name here) FROM (enter database name here)
# ```

# Una vez que tenga una idea de cómo se ven sus tablas y cómo podrían interactuar, es una buena idea mirar algunos de los datos sin procesar para estar al tanto de cualquier anomalía que pueda plantear problemas para su análisis o interpretaciones, es decir se explora algunos registros.
# 
# Recuperamos la columna raza de la tabla perros. cada fila de la salida enumera el nombre de la raza del perro representado por esa entrada, algunos nombres de razas se enumeran varias veces, porque varios perros de esa raza han participado en las pruebas. Podemos limitar la salida a las 5 primeras filas

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT breed\nFROM dogs\nLIMIT 5;')


# También puede seleccionar filas de datos de diferentes partes de la tabla de salida, en lugar de comenzar siempre desde el principio, Para hacer esto, use la cláusula OFFSET después de LIMIT. El número después de la cláusula OFFSET indica desde qué fila comenzará la consulta de salida o bien de la siguiente manera:

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT breed, breed_type, breed_group\nFROM dogs LIMIT 5, 10;')


# Considermos todos los campos:a

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM dogs LIMIT 4;')

