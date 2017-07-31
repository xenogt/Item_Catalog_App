from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catagory, Item


#Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#JSON APIs to view Catagory Information
@app.route('/catagory/<int:catagory_id>/item/JSON')
def catagoryItemJSON(catagory_id):
    catagory = session.query(Catagory).filter_by(id = catagory_id).one()
    items = session.query(Item).filter_by(catagory_id = catagory_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/catagory/<int:catagory_id>/item/<int:item_id>/JSON')
def itemJSON(catagory_id, item_id):
    Item = session.query(Item).filter_by(id = item_id).one()
    return jsonify(Item = Item.serialize)

@app.route('/catagory/JSON')
def catagoriesJSON():
    catagories = session.query(Catagory).all()
    return jsonify(catagories= [c.serialize for c in catagories])


#Show all catagories
@app.route('/')
@app.route('/catagory/')
def showCatagories():
  catagories = session.query(Catagory).order_by(asc(Catagory.name))
  return render_template('catagories.html', catagories = catagories)

#Create a new catagory
@app.route('/catagory/new/', methods=['GET','POST'])
def newCatagory():
  if request.method == 'POST':
      newCatagory = Catagory(name = request.form['name'])
      session.add(newCatagory)
      flash('New Catagory %s Successfully Created' % newCatagory.name)
      session.commit()
      return redirect(url_for('showCatagories'))
  else:
      return render_template('newCatagory.html')

#Edit a catagory
@app.route('/catagory/<int:catagory_id>/edit/', methods = ['GET', 'POST'])
def editCatagory(catagory_id):
  editedCatagory = session.query(Catagory).filter_by(id = catagory_id).one()
  if request.method == 'POST':
      if request.form['name']:
        editedCatagory.name = request.form['name']
        flash('Catagory Successfully Edited %s' % editedCatagory.name)
        return redirect(url_for('showCatagories'))
  else:
    return render_template('editCatagory.html', catagory = editedCatagory)


#Delete a catagory
@app.route('/catagory/<int:catagory_id>/delete/', methods = ['GET','POST'])
def deleteCatagory(catagory_id):
  catagoryToDelete = session.query(Catagory).filter_by(id = catagory_id).one()
  if request.method == 'POST':
    session.delete(catagoryToDelete)
    flash('%s Successfully Deleted' % catagoryToDelete.name)
    session.commit()
    return redirect(url_for('showCatagories', catagory_id = catagory_id))
  else:
    return render_template('deleteCatagory.html',catagory = catagoryToDelete)

#Show a catagory item
@app.route('/catagory/<int:catagory_id>/')
@app.route('/catagory/<int:catagory_id>/item/')
def showItem(catagory_id):
    catagory = session.query(Catagory).filter_by(id = catagory_id).one()
    items = session.query(Item).filter_by(catagory_id = catagory_id).all()
    return render_template('item.html', items = items, catagory = catagory)
     


#Create a new item
@app.route('/catagory/<int:catagory_id>/item/new/',methods=['GET','POST'])
def newItem(catagory_id):
  catagory = session.query(Catagory).filter_by(id = catagory_id).one()
  if request.method == 'POST':
      newItem = Item(name = request.form['name'], description = request.form['description'], catagory_id = catagory_id)
      session.add(newItem)
      session.commit()
      flash('New Item %s Item Successfully Created' % (newItem.name))
      return redirect(url_for('showItem', catagory_id = catagory_id))
  else:
      return render_template('newitemitem.html', catagory_id = catagory_id)

#Edit a item
@app.route('/catagory/<int:catagory_id>/item/<int:item_id>/edit', methods=['GET','POST'])
def editItem(catagory_id, item_id):

    editedItem = session.query(Item).filter_by(id = item_id).one()
    catagory = session.query(Catagory).filter_by(id = catagory_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit() 
        flash('Item Successfully Edited')
        return redirect(url_for('showItem', catagory_id = catagory_id))
    else:
        return render_template('edititem.html', catagory_id = catagory_id, item_id = item_id, item = editedItem)


#Delete a item item
@app.route('/catagory/<int:catagory_id>/item/<int:item_id>/delete', methods = ['GET','POST'])
def deleteItem(catagory_id,item_id):
    catagory = session.query(Catagory).filter_by(id = catagory_id).one()
    itemToDelete = session.query(Item).filter_by(id = item_id).one() 
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Item Successfully Deleted')
        return redirect(url_for('showItem', catagory_id = catagory_id))
    else:
        return render_template('deleteItem.html', item = itemToDelete)




if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
