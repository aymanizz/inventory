from app.forms import (
    ActionForm,
    CreateOrUpdateItemForm,
    DeleteItemForm,
    CreateOrUpdateItemForm,
)
from flask import render_template, redirect, flash, url_for
from app import app, db
from app.models import Item
from app.repositories.items import create_items_repository


@app.route("/")
@app.route("/index")
def index():
    items = create_items_repository().get_all()
    return render_template(
        "index.html", title="Home Page", items=items, undelete_form=ActionForm()
    )


@app.route("/items/create", methods=["GET", "POST"])
def create_item():
    form = CreateOrUpdateItemForm()
    if form.validate_on_submit():
        create_items_repository().add(
            Item(
                name=form.name.data,
                description=form.description.data,
                unit=form.unit.data,
            )
        )
        db.session.commit()
        flash("New item created")
        return redirect(url_for("index"))

    return render_template(
        "routes/items/create_update_item.html",
        title="Create Item",
        item_form_type="Create",
        form=form,
        item=None,
    )


@app.route("/items/<item_id>", methods=["GET", "POST"])
def item(item_id):
    repo = create_items_repository()
    item = repo.get(item_id)
    form = CreateOrUpdateItemForm(obj=item)

    if item is None:
        flash("Item {} not found.".format(item_id))
        return redirect(url_for("index"), 404)

    if form.validate_on_submit():
        item.edit(
            name=form.name.data,
            description=form.description.data,
            quantity=form.quantity.data,
            unit=form.unit.data,
        )
        db.session.commit()
        flash("Item has been updated.".format(item.name, item.id))
        return redirect(url_for("item", item_id=item_id))

    return render_template(
        "routes/items/create_update_item.html",
        title=f"Item - {item.name}",
        item_form_type="Update",
        form=form,
        item=item,
        undelete_form=ActionForm(),
    )


@app.route("/items/<item_id>/delete", methods=["GET", "POST"])
def delete_item(item_id):
    form = DeleteItemForm()
    repo = create_items_repository()
    item = repo.get(item_id)

    if item is None:
        flash("Item {} not found.".format(item_id))
        return redirect(url_for("index"), 404)

    if form.validate_on_submit():
        item.mark_deleted(form.comment.data or None)
        db.session.commit()
        flash("Item {}({}) has been deleted.".format(item.name, item.id))
        return redirect(url_for("index"))

    return render_template(
        "routes/items/delete_item.html", title="Delete Item", form=form, item=item
    )


@app.route("/items/<item_id>/undelete", methods=["POST"])
def undelete_item(item_id):
    form = ActionForm()
    repo = create_items_repository()
    item = repo.get(item_id)

    if form.validate_on_submit():
        if item is None:
            flash("Item {} not found.".format(item_id))
            return redirect(url_for("index"), 404)

        item.undelete()
        db.session.commit()
        flash("Item {}({}) has been restored.".format(item.name, item.id))

    return redirect(url_for("index"))
