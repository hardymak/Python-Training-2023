# What is a QuerySet ? Write program to create a new Post object in database:
"""
=>  A QuerySet in Django is a representation of a collection of database queries.
    It allows you to retrieve and manipulate data from the database using Python syntax. 

    class User(models.Model):
        email = models.EmailField(unique=True,max_length=30)
        password = models.CharField(max_length=30)
        role = models.CharField(max_length=30)
        
        def __str__(self):
            return self.email

            
"""