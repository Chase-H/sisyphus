import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pprint import pprint

PROJECT_ID = "sisyphus-4cbf4"
PATH_TO_SERVICE_ACCOUNT = "service-account-key.json"

class Firestore:
  '''
  db is gcp firestore client (https://googleapis.dev/python/firestore/latest/client.html)
  '''
  def __init__(self):   

      # Pass credentials to GCP and get a handle on Firestore client
      cred = credentials.Certificate(PATH_TO_SERVICE_ACCOUNT)
      firebase_admin.initialize_app(cred, {"projectId": PROJECT_ID})
      self.db = firestore.client()

  def add(self, collection, key, value):
    '''
    If value is not dict raise TypeError 
    Else add key with value in collection
    '''
    if type(value) is not dict:
      raise TypeError(f"firestore-add() - value must be dict but it is {type(value)}")
    ref = self.db.collection(collection).document(key)
    ref.set(value)

  def delete(self, collection, key):
    '''
    Delete key in collection
    '''
    ref = self.db.collection(collection).document(key)
    ref.delete()

  def update(self, collection, key, value):
    '''
    If value is not dict raise TypeError 
    Else update key with value in collection
    '''
    if type(value) is not dict:
      raise TypeError(f"firestore-update() - value must be dict but it is {type(value)}")

    ref = db.collection(collection).document(key)
    ref.update(updates)

  def lookup(self, collection, key):
    '''
    Return item if key in table else return False
    '''
    doc_ref = self.db.collection(collection).document(key)
    return doc_ref.get().exists

  def get(self, collection, key):
    '''
    If key in collection return value as dict 
    Else return None
    '''
    doc_ref = self.db.collection(collection).document(key)
    doc = doc_ref.get()
    if doc.exists:
      return doc.to_dict()
    return None

  def get_all(collection):
    '''
    '''
    pass