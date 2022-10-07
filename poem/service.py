from .models import Poem 

def getAllPoems():
    return Poem.objects.all()

def getPoem(id):
    return Poem.objects.get(pk=id)

def addPoem(title, content):
    Poem.objects.create(title=title, content=content)

def deletePoem(id):
    poem = Poem.objects.get(pk=id)
    poem.delete()

def editPoem(id, title, content):
    poem = Poem.objects.get(pk=id)
    poem.title = title
    poem.content = content
    poem.save()
